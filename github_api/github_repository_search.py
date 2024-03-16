import requests
from file_handler import FileHandler


class GitHubRepositorySearch:
    def search_repositories(self, query, owner, headers):
        repositories = []
        page = 1
        url = "https://api.github.com/search/repositories"
        
        while True:
            params = {"q": query, "per_page": 100, "page": page}
            response = requests.get(url, headers=headers, verify=False, params=params)
            
            if response.status_code == 200:
                data = response.json()
                if len(data['items']) == 0:
                    return FileHandler.save_results(repositories)
                for item in data['items']:
                    if item['owner']['login'] == owner:
                        repositories.append(item['full_name'])
                page += 1
            
            elif response.status_code == 422 and response.reason == 'Unprocessable Entity':
                print(f"1000 requests were made: {response.text}")
                return FileHandler.save_results(repositories)
            
            else:
                print(f"Error: {response.text}")
                return []
