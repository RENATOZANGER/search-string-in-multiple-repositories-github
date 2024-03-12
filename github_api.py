import os
import time
import requests


class GitHubAPI:
    def __init__(self, token):
        self.headers = {"Authorization": f"Bearer {token}"}

    def search_repositories(self, query, owner):
        repositories = []
        page = 1
        
        while True:
            params = {"q": query,
                      "per_page": 100,
                      "page": page
                      }
            url = "https://api.github.com/search/repositories"
            response = self._send_request(url, params)
            
            if response.status_code == 200:
                data = response.json()
                if len(data['items']) == 0:
                    return self._save_results(repositories)
                for item in data['items']:
                    if item['owner']['login'] == owner:
                        repositories.append(item['full_name'])
                page += 1
            elif response.status_code == 422:
                print(f"1000 requests were made: {response.text}")
                return self._save_results(repositories)
            else:
                print(f"Error: {response.text}")
                return []

    def search_code(self, repo, string):
        url = f"https://api.github.com/search/code?q={string}+in:file+repo:{repo}"
        response = self._send_request(url)
        
        if response.status_code == 200:
            result = response.json()
            for item in result["items"]:
                print(f"Text found in the file: {item['html_url']}")
                self._save_search_results(f"Results/{string}.txt", item['html_url'])
        else:
            print(f"Error: {response.status_code}, {response.text}")

    def _send_request(self, url, params=None):
        while True:
            response = requests.get(url, headers=self.headers, verify=False, params=params)
            remaining = response.headers.get("X-RateLimit-Remaining")
            
            if remaining == "0":
                print("RateLimit reached, awaiting release...")
                self._wait_for_release(url)
            return response

    def _wait_for_release(self, url):
        inicio = time.time()
        
        while True:
            response = requests.get(url, headers=self.headers, verify=False)
            remaining = response.headers.get("X-RateLimit-Remaining")
            
            if remaining != "0":
                fim = time.time()
                tempo_execucao = fim - inicio
                horas = int(tempo_execucao // 3600)
                minutos = int(tempo_execucao % 3600 // 60)
                segundos = int(tempo_execucao % 60)
                print(f"RateLimit reached, waiting time: {horas:02d}h {minutos:02d}m {segundos:02d}s")
                break

    def _save_results(self, repo):
        if len(repo):
            folder_path = "Results"
            
            if not os.path.exists(folder_path):
                os.makedirs("Results")
            with open(f"{folder_path}/Repositories.txt", "w") as file:
                for item in repo:
                    file.write(f"{item}\n")
            return repo
        else:
            print('Empty repository')
            exit()

    def _save_search_results(self, file_path, result):
        with open(file_path, "a") as file:
            file.write(f"{result}\n")
