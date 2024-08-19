import redis
from config import *
class Cache:
    def __init__(self):
        self.client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

    def get(self, key):
        try:
            value = self.client.get(key)
            if value is not None:
                return value.decode('utf-8')  
            return None
        except redis.RedisError as e:
            print(f"Error getting key {key} from Redis: {e}")
            return None

    def set(self, key, value):
        try:
            self.client.set(key, value)
            print(f"Key '{key}' set in Redis.")
        except redis.RedisError as e:
            print(f"Error setting key {key} in Redis: {e}")