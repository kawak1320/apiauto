"""
(c) Copyright Jalasoft. 2023

projects.py
    configuration of logger file
"""
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN_TODO = os.getenv("TOKEN")

HEADERS = {
    "Authorization": f"Bearer {TOKEN_TODO}"
}
ABS_PATH = os.path.abspath(__file__ + "../../../")
