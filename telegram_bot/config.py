import yaml
import os

DEBUG = os.getenv("DEBUG") == 'true'
BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_API_URL = os.getenv('BASE_API_URL', '')
BASE_API_KEY = os.getenv('API_KEY', '')

with open('./localization.yaml', 'r', encoding='utf-8') as file:
    texts = yaml.safe_load(file)
    admins_texts = texts['ru']['admins']['texts']
    admins_buttons = texts['ru']['admins']['buttons']
    users_texts = texts['ru']['users']['texts']
    users_buttons = texts['ru']['users']['buttons']

