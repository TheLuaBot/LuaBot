from dotenv import load_dotenv
import logging
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
database_token = os.getenv("MONGODB_TOKEN")

def DiscordTokenManager():
    if not token:
        logging.CRITICAL("[SHIH TOKEN MANAGER] O DISCORD_TOKEN não existe! Coloque o novo token")

def MongoDBTokenManager():
    if not database_token:
        logging.CRITICAL("[SHIH TOKEN MANAGER]  O MONGODB_TOKEN não existe! Precisamo de um novo token")