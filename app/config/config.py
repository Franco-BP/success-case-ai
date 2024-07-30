import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    GENIE_API_KEY = os.getenv('GENIE_API_KEY')
