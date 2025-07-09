# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class DBConfig:
    # Select DB
    DB_BACKEND = os.getenv("DB_BACKEND", "cosmos")  # could be "mongo" or "cosmos"

    # Cosmos DB Configuration
    COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT")
    COSMOS_KEY = os.getenv("COSMOS_KEY")
    COSMOS_DATABASE = os.getenv("COSMOS_DATABASE", "servantdb")