import discord
from discord.ext import commands
import os
from fishing import fish_helper
from dotenv import load_dotenv
import re
import random
import json
from gacha import character_gacha
from economy_helper import get_profile_data
from economy_helper import open_account
from fishing import add_fish
from fishing import create_inventory

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
async def fish(ctx: commands.Context, region):
    regions = ["horimmia", "triptych_lux", "sharnoth", "iskald", "lhodikess", "phronesis", "cloudfish", "alqafar"]

    @fish.error
    async def flip_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'I am sorry, {ctx.author}, you are missing an argument. You require a region. The list of regions are: {regions}')
    if region.lower() not in regions:
        await ctx.send(f"That region is not available. Please use one of the following: {regions}")
    
    fishing_results = fish_helper(0, region)
    number = fishing_results[0]
    catch = fishing_results[1]

    add_fish(ctx.author, catch)
    await ctx.send(f'{ctx.author} rolled {number}. You got {catch}')

@bot.hybrid_command()
async def gacha(ctx: commands.Context, pulls = 1):

       
    if pulls < 1:
        await ctx.send('Please pull more than once.')
    elif pulls > 10:
        await ctx.send(f'{ctx.author}, we need to talk about your gambling addiction. 10 pulls at most, please.')
    else:
        gacha_result = character_gacha(pulls)
        await ctx.send(f'{ctx.author} pulled {pulls} time/s and got the following:\n {gacha_result}')

@bot.hybrid_command()
async def bal(ctx: commands.Context):
    user = ctx.author
    open_account(user)
    users = get_profile_data()
    user_string = str(user.id)


    balance = users[user_string]["Balance"]
    prismatic_shards = users[user_string]["Prismatic Shards"]

    coin_emoji = '\U0001FA99'
    diamond_emoji = '\U0001F48E'
    economy_embed = discord.Embed(title = f'**{user}**',
                          description = f'{coin_emoji} {balance} \n {diamond_emoji} {prismatic_shards}')

    await ctx.send(embed = economy_embed)

@bot.hybrid_command()
async def inv(ctx: commands.Context):
    user = ctx.author
    create_inventory(user)
    users = get_profile_data()
    user_string = str(user.id)
    inventory_embed = discord.Embed(title = f"{user}'s Inventory", description = "")
    inventory = users[user_string]["Inventory"]
    embed_description = inventory_embed.description

    fish_inventory = inventory["Fish Inventory"]
    item_inventory = inventory["Item Inventory"]
    if fish_inventory == {} and item_inventory == {}:
        embed_description = f'**{user}** has nothing in their inventory.'
    if fish_inventory != {}:
        embed_description += f"**Fishes in {user}'s inventory**"
        for element in fish_inventory:
            count = fish_inventory[element]["Count"]
            inventory_embed.description += f'{element}: {count}\n'
    if item_inventory != {}:
        embed_description += f"**Items in {user}'s inventory**"
        for element in item_inventory:
            count = item_inventory[element]["Count"]
            inventory_embed.description += f'{element}: {count}\n'
        
    
    await ctx.send(embed = inventory_embed)


@bot.hybrid_command()
async def claim(ctx: commands.Context):
    user = ctx.author
    open_account(user)
    users = get_profile_data()
    user_string = str(user.id)

    users[user_string]["Balance"] += 100

    with open("la_economia.json", "w") as f:
        json.dump(users, f)

 

    await ctx.send("Your allowance. 100 gold. Don't spend it all in one place, okay?")


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

    await bot.process_commands(message)
    


bot.run(token)