import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = os.getenv("SUPERBENCHMARK_DEBUG", "False").lower() in ("true", "1")


config = Config()
