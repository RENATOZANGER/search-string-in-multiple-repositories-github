import requests
from ratelimit_waiter import RateLimitWaiter


class GitHubCodeSearch:
    def search_code(self, repo, string, headers):
        url = f"https://api.github.com/search/code?q={string}+in:file+repo:{repo}"
        response = self._send_request(url, headers)
        
        if response.status_code == 200:
            result = response.json()
            return [item['html_url'] for item in result["items"]]
        else:
            print(f"Error: {response.status_code}, {response.text}")
    
    def _send_request(self, url, headers):
        while True:
            response = requests.get(url, headers=headers, verify=False)
            remaining = response.headers.get("X-RateLimit-Remaining")
            
            if remaining == "0":
                RateLimitWaiter.wait_for_release(url, headers)
                response = requests.get(url, headers=headers, verify=False)
            return response
