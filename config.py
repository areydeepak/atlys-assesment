import os
from dotenv import load_dotenv

load_dotenv()

STATIC_TOKEN = os.getenv("STATIC_TOKEN")
BASE_URL = os.getenv("BASE_URL")
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
