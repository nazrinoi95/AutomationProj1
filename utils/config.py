import os
from dotenv import load_dotenv

load_dotenv()

def get_config(key, default=None):
    """Read a config value from .env file or environment variables."""
    return os.getenv(key, default)