#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "26367102"))
API_HASH = environ.get("API_HASH", "8016bf66f0ebe4d33583eb896e1a1068")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "6908710065"))
CREDIT = "𝄟⃝‌🐬𝙆𝙐𝙉𝙒𝘼𝙍 𝙎𝘼 𝙎𝙊𝘿𝙃𝘼🌹𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '6908710065').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
