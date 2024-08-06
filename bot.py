from telethon import TelegramClient, events
from dotenv import load_dotenv
import requests
import os
from telegram import Update

load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')
FASTAPI_URL = os.getenv('FASTAPI_URL')


if api_id is None or api_hash is None:
    print('API ID and hash are not set correctly. Refer to README.md for further information.')
    exit(1)

try:
    api_id = int(api_id)
except ValueError:
    print('API ID is not an integer. Refer to README.md for more information.')
    exit(1)

client = TelegramClient('session_bot', api_id=api_id, api_hash=api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hello! Use /search <keyword> to find users.')


@client.on(events.NewMessage(pattern='/search (.+)'))
async def search(event):
    keyword = event.pattern_match.group(1)

    try:
        response = requests.get(FASTAPI_URL, params={'keyword': keyword})
        response.raise_for_status()
        data = response.json()        
        if data != None:
            for group in data['groups']:
                print(f"Title: {group['title']}, Link: {group['link']}")
                await event.respond(f"Title: {group['title']}, Link: {group['link']}")
            
        elif data == None :
            Update.message.reply_text("No groups found.")

    except requests.exceptions.RequestException as e:
        Update.message.reply_text(f"An error occurred: {e}")


client.start()
client.run_until_disconnected()