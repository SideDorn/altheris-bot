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
from item_name_formatter import format
from racing import golem_race
from slots import slotmachine
from time import sleep
from casino_helper import bet_checker
load_dotenv()


token = os.getenv('DISCORD_TOKEN')
#gives perms to bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
coin_emoji = '\U0001FA99'
diamond_emoji = '\U0001F48E'
with open("fish_prices.json", 'r') as f:
    fish_prices = json.load(f)
with open("shop_items.json", "r") as f:
    shop_prices = json.load(f)
with open("rod_modifiers.json", "r") as f:
    rod_modifiers = json.load(f)



#schizo
@bot.hybrid_command()
async def test(ctx: commands.Context):
    await ctx.send(f'Hello, {ctx.author}, how may I help you? Have you been doing well?')

#fishing
@bot.hybrid_command()
async def fish(ctx: commands.Context, region):
    regions = ["horimmia", "triptych_lux", "sharnoth", "iskald", "lhodikess", "phronesis", "cloudfish", "alqafar"]

    user = ctx.author
    users = get_profile_data()
    user_string = str(user.id)
    if "Equipped" not in users[user_string]:
        users[user_string]["Equipped"] = "Default Rod"

    equipped_rod = users[user_string]["Equipped"]

    @fish.error
    async def flip_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'I am sorry, {ctx.author}, you are missing an argument. You require a region. The list of regions are: {regions}')
    if region.lower() not in regions:
        await ctx.send(f"That region is not available. Please use one of the following: {regions}")
    
    modifier = rod_modifiers[equipped_rod]
    print(rod_modifiers)
    fishing_results = fish_helper(modifier, region)
    number = fishing_results[0]
    catch = fishing_results[1]

    add_fish(ctx.author, catch)
    await ctx.send(f'{user} rolled {number} ({number - modifier} + {modifier}). You got {catch}')





#economy stuff here 
@bot.hybrid_command()
async def gacha(ctx: commands.Context, pulls = 1):
    user = ctx.author
    open_account(user)
    users = get_profile_data()
    user_string = str(user.id)


    balance = users[user_string]["Balance"]
    prismatic_shards = users[user_string]["Prismatic Shards"]


    

    if 130*pulls > prismatic_shards:
        await ctx.send(f'{ctx.author}, you do not have enough shards for this transaction. Come back when you have enough.')   
    else: 
        if pulls < 1:
            await ctx.send('Please pull more than once.')
        elif pulls > 10:
            await ctx.send(f'{ctx.author}, we need to talk about your gambling addiction. 10 pulls at most, please.')
        else:
            gacha_result = character_gacha(pulls)
            pull = ""
            ctr = 0
        for element in gacha_result:
            ctr+=1
            if ctr % 2 == 0:
                pull += f"{element}\n"
            else:
                pull += f"{element}\n"


        #Unused Code for Embed
                #pull += f"{element}\t\t\t\t\t\t" 
        # gacha_embed = discord.Embed(title = f'**{user}**',
        #         description = f' {balance} \n {prismatic_shards}', )          
        # await ctx.send(embed = gacha_embed)



        await ctx.send(f"{ctx.author} pulled {pulls} time/s and got the following:\n{pull}")
        users[user_string]["Prismatic Shards"] -= 130*pulls

        with open("la_economia.json", "w") as f:
            json.dump(users, f)


@bot.hybrid_command()
async def bal(ctx: commands.Context):
    user = ctx.author
    open_account(user)
    users = get_profile_data()
    user_string = str(user.id)


    balance = users[user_string]["Balance"]
    prismatic_shards = users[user_string]["Prismatic Shards"]


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
        embed_description += f"**{user}** has nothing in their inventory."
    else:
        if fish_inventory != {}:
            embed_description += f"**Fishes in {user}'s inventory**\n"
            for element in fish_inventory:
                count = fish_inventory[element]["Count"]
                embed_description += f'**{element}**: {count}\n'
        if item_inventory != {}:
            embed_description += f"\n**Items in {user}'s inventory**\n"
            for element in item_inventory:
                count = item_inventory[element]["Count"]
                embed_description += f'**{element}**: {count}\n'
    
    inventory_embed.description = embed_description
        
    await ctx.send(embed = inventory_embed)

@bot.hybrid_command()
async def sell(ctx: commands.Context, item, amount = 1):
    user = ctx.author
    open_account(user)
    users = get_profile_data()
    user_string = str(user.id)
    inventory = users[user_string]["Inventory"]
    item = format(item)

    
    if item not in fish_prices:
        await ctx.send(f"I'm sorry, {user}, {item} is not an item.")
    elif amount <= 0:
        await ctx.send("...Huh?")
    else:
        fish_inventory = inventory["Fish Inventory"]
        item_inventory = inventory["Item Inventory"]
        in_inventory = item in item_inventory or item in fish_inventory
        
        fish_count = fish_inventory[item]["Count"]
        # item_count = item_inventory[item]["Count"]

        if item in fish_prices:
            count = fish_count
        #elif item in item_prices:
            # count = item_count
        #add item prices if it gets added

        if not in_inventory:
            await ctx.send(f"I'm sorry, {user}, you do not have any {item} at the moment")
        #add or item count when items get implemented :3
        elif fish_count >= amount:
            price = fish_prices[item] * amount
            users[user_string]["Balance"] += price
            users[user_string]["Inventory"]["Fish Inventory"][item]["Count"] -= amount

            with open("la_economia.json", "w") as f:
                json.dump(users, f)
            await ctx.send(f"{amount} {item}/s sold for {price} {coin_emoji}!")
        else:
            await ctx.send(f"I'm sorry, {user}, you don't have enough of {item}. Currently, you have {count} {item}s")

@bot.hybrid_command()
async def buy(ctx: commands.Context, item, amount = 1):
    user = ctx.author
    open_account(user)
    create_inventory(user)
    users = get_profile_data()
    user_string = str(user.id)
    inventory = users[user_string]["Inventory"]
    item = format(item)

    if item not in shop_prices:
        await ctx.send(f"I'm sorry., {user}, we don't have {item} at the moment. Please check again later!")
    elif amount < 0:
        await ctx.send("Are you trying to scam me?")
    else:
        cost = shop_prices[item] * amount
        

        if cost > users[user_string]["Balance"]:
            await ctx.send("You do not have enough money for this transaction.")
        
        else:  
            if item not in inventory:
                users[user_string]["Inventory"]["Item Inventory"][item] = {"Count": 0}
            
            users[user_string]["Balance"] -= cost
            users[user_string]["Inventory"]["Item Inventory"][item]["Count"] += amount

            with open("la_economia.json", "w") as f:
                json.dump(users, f)
            await ctx.send(f"{amount} {item}/s bought for {cost} {coin_emoji}!")
    
@bot.hybrid_command()
async def shop(ctx:commands.Context):
    embed = discord.Embed(title = "**Altheris' Shop**", description = "")
    for element in shop_prices:
        embed.description += f"**{element}** ({shop_prices[element]} G) \n"

    await ctx.send(embed = embed)



        
# casino commands here 

@bot.hybrid_command()
async def race(ctx: commands.Context, golem, bet = 5):
    user = ctx.author
    open_account(user)
    user = ctx.author
    users = get_profile_data()
    user_string = str(user.id)
    golem = format(golem)
    
    is_valid_bet = await bet_checker(ctx, bet, user_string)
    if golem not in ["Wood", "Stone", "Metal", "Magma"]:
        await ctx.send("Please bet on a proper golem: Wood, Stone, Metal, and Magma.")
    elif is_valid_bet:
        users[user_string]["Balance"] -= bet
        results = golem_race()
        print(results)
        first_place = results[0]
        second_place = results[1]
        third_place = results[2]
        fourth_place = results[3]

        if golem == first_place:
            winnings = 10 * bet
            await ctx.send(f"Congratulations, your {golem} Golem won first place! You won {winnings} {coin_emoji}!")
        elif golem == second_place:
            winnings = 2 * bet
            await ctx.send(f"Congratulations, your {golem} Golem won second place! You won {winnings} {coin_emoji}!")
        elif golem == third_place:
            winnings = -2 * bet
            await ctx.send(f"Unlucky, your {golem} Golem got third place. You lost {-winnings} {coin_emoji}.")       
        elif golem == fourth_place:
            winnings = -10 * bet
            await ctx.send(f"Ouch, your {golem} Golem got last. You lost {-winnings} {coin_emoji}.") 


        users[user_string]["Balance"] += winnings

        with open("la_economia.json", "w") as f:
            json.dump(users, f)   

        await ctx.send(f"Final standings for {user}'s race: \n **{results}**")

@bot.hybrid_command()
async def slots(ctx:commands.Context, bet = 5):
    user = ctx.author
    open_account(user)
    users = get_profile_data()
    user_string = str(user.id)
    is_valid_bet = await bet_checker(ctx, bet, user_string)

    if is_valid_bet:
        users[user_string]["Balance"] -= bet
        results, reward, message = slotmachine(bet)
        await ctx.send("Loading results...")
        sleep(2)
        await ctx.send(results)
        if reward != 0:
            await ctx.send((f"{message}{user} won {reward} {coin_emoji}!"))
        else:
            await ctx.send(f"Unfortunately, {user} won nothing.")

        users[user_string]["Balance"] += reward

        with open("la_economia.json", "w") as f:
            json.dump(users, f)

@bot.hybrid_command()
async def claim(ctx: commands.Context):
    user = ctx.author
    open_account(user)
    users = get_profile_data()
    user_string = str(user.id)
    

    if users[user_string]["Balance"] >= -100:
        users[user_string]["Balance"] += 100
        users[user_string]["Prismatic Shards"] += 1300
        await ctx.send(f"Here's today's share, {user}. 100 {coin_emoji} and 1300 {diamond_emoji}. Don't spend it all at once, okay?")
    else:
        users[user_string]["Balance"] = 100
        await ctx.send(f"*sigh* {user}, have this to get back on your feet. Be more responsible, okay?")

    with open("la_economia.json", "w") as f:
        json.dump(users, f)

 
@bot.hybrid_command()
async def donate(ctx: commands.Context, receiver: discord.Member, donation=0):
    user = ctx.author
    open_account(user)
    open_account(receiver)
    users = get_profile_data()
    user_string = str(user.id)
    receiver_string = str (receiver.id)

    userbalance = users[user_string]["Balance"]


 
    if donation<0:
        await ctx.send("Stealing's bad! Don't try that again.")
    elif donation==0:
        await ctx.send("Why are you holding out an empty hand? I'm not holding that.")
    else:
        if userbalance <= 0:
            await ctx.send("You can't donate on an empty wallet.")
        elif userbalance < donation:
            await ctx.send("You can't give what you don't have. Try again.")  
        elif user==receiver:
            await ctx.send("You can't just give yourself money, try again.")
        elif receiver.id==1245076712841154580:
            users[user_string]["Balance"] -= donation
            await ctx.send(f"For me? Thanks for the {donation} {coin_emoji}, {user}. ")         
        else:
            users[user_string]["Balance"] -= donation
            users[receiver_string]["Balance"] += donation
            await ctx.send(f"{user} donated {donation} to {receiver}. Quite generous.")

    with open("la_economia.json", "w") as f:
        json.dump(users, f)


#equip
@bot.hybrid_command()
async def equip(ctx: commands.Context, item):
    item = format(item)
    user = ctx.author
    users = get_profile_data()
    create_inventory(user)
    user_string = str(user.id)

    inventory = users[user_string]["Inventory"]["Item Inventory"]

    if item not in inventory:
        await ctx.send(f"{user}, you don't have {item}")
    else:
        users[user_string]["Inventory"]["Item Inventory"]["Default Rod"] = {"Count": 1}
        users[user_string]["Equipped"] = item
        await ctx.send(f"{user} has equipped {item}")

    with open("la_economia.json", "w") as f:
        json.dump(users, f)   




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



        