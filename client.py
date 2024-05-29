import discord
import os
from dotenv import load_dotenv
import re

load_dotenv()

token = os.getenv('DISCORD_TOKEN')
#gives perms to bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
client = discord.Client(intents=intents)




@client.event
async def on_ready():
    print(f'{client.user} kidou shimasu!')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel.name)
    if channel == "bot-spam":
        print(f'{username} said {user_message} in #{channel}, {message.author}')
        await message.channel.send(f"hi {username}")

    


client.run(token)