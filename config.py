import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "27400172"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "56d0a75c5f9a9de6beb5452aa63c2d36")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7985176101:AAGhvKufmurt5X5zsdcUrJTnz7MAR_GmGdk")

OWNER_ID = int(os.environ.get("OWNER_ID", "7540570087"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "7540570087").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://greenhornet63603:CvnxnjzknPLxYOfo@cluster0.qif4g18.mongodb.net/?appName=Cluster0")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003301075022"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1003301075022")  # Optional here you'll get all logs
