import requests
import os
import json

from dotenv import load_dotenv, dotenv_values 
load_dotenv() 

url = "https://api.github.com/user/repos"
token = os.getenv(PAT_KEY)