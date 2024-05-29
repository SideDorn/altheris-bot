import discord
from discord.ext import commands
import os
from fishing import fish_helper
from dotenv import load_dotenv
import re
import random
load_dotenv()

token = os.getenv('DISCORD_TOKEN')
#gives perms to bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)



@bot.hybrid_command()
async def test(ctx: commands.Context):
    await ctx.send(f'Hello, {ctx.author}, how may I help you? Have you been doing well?')

@bot.hybrid_command()
async def fish(ctx: commands.Context):
    fishing_results = fish_helper(0, "Nilgiri")
    number = fishing_results[0]
    catch = fishing_results[1]
    await ctx.send(f'{ctx.author} rolled {number}. You got a {catch}')

@bot.event
async def on_ready():
    print(f'{bot.user} kidou shimasu!')

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel.name)
    if channel == "bot-spam" and user_message[0] != bot.command_prefix:
        print(f'{username} said {user_message} in #{channel}, {message.author}')
        await message.channel.send(f"hi {username}")

    await bot.process_commands(message)
    


bot.run(token)