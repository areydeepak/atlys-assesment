import time
import requests

def retry(func):
    def wrapper(*args, **kwargs):
        for i in range(3):  
            try:
                return func(*args, **kwargs)
            except requests.exceptions.RequestException as e:
                print(f"Retrying in 5 seconds... ({i+1}/3)")
                time.sleep(5)
        raise Exception("Failed after 3 retries")
    return wrapper
