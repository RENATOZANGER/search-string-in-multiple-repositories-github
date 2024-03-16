import time
import requests


class RateLimitWaiter:
    RATELIMIT_WAIT_MESSAGE = "RateLimit reached, awaiting release..."
    
    @staticmethod
    def wait_for_release(url, headers):
        inicio = time.time()
        while True:
            response = requests.get(url, headers=headers, verify=False)
            remaining = response.headers.get("X-RateLimit-Remaining")
            
            if remaining != "0":
                fim = time.time()
                runtime = fim - inicio
                hours = int(runtime // 3600)
                minutes = int(runtime % 3600 // 60)
                seconds = int(runtime % 60)
                print(RateLimitWaiter.RATELIMIT_WAIT_MESSAGE)
                print(f"Waiting time: {hours:02d}h {minutes:02d}m {seconds:02d}s")
                break
