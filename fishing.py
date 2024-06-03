import random
import json
import os
from economy_helper import get_profile_data
from economy_helper import open_account
from item_name_formatter import format

common_fish = ["Tuna","Salmon","Carp","Guppy"]

def horrimmia_fish(modifier):
    number = random.randint(1, 100) + modifier
    catch = ""

    if number > 55:
        catch = "Tilapieaux"
    elif number > 20:
        catch = "Smoky Carp"
    else:
        catch = random.choice(common_fish)
    return [number, catch]

def tiferet_fish(modifier):
    number = random.randint(1, 100) + modifier
    catch = ""

    if number > 90:
        catch = "Genesis Ichthys"
    elif number > 60:
        catch = "Chromafish"
    elif number > 30:
        catch = "Pixel Salmon"
    else:
        catch = random.choice(common_fish)
    
    return [number, catch]

def sharnoth_fish(modifier):
    number = random.randint(1, 100) + modifier
    catch = ""

    if number > 60:
        catch = "Ciseaux Noir"
    elif number > 25:
        catch = "Dorchadic Guppy"
    else:
        catch = random.choice(common_fish)

    return [number, catch]

def iskald_fish(modifier):
    number = random.randint(1, 100) + modifier
    catch = "" 

    if number > 80:
        catch = "Necrosalmon"
    elif number > 30:
        catch = "Smiling Face"
    else:
        catch = random.choice(common_fish)

    return [number, catch]

def lhodikess_fish(modifier):
    number = random.randint(1, 100) + modifier
    catch = ""

    if number > 90:
        catch = "King of Winter"
    elif number > 30:
        catch = "Icefish"
    else:
        catch = random.choice(common_fish)
    return [number, catch]

def phronesis_fish(modifier):
    number = random.randint(1, 100) + modifier
    catch = ""

    if number > 60:
        catch = "Fishcartes"
    else:
        catch = random.choice(common_fish)

    return [number, catch]

def cloudfish(modifier):
    number = random.randint(1, 100) + modifier
    catch = ""

    if number > 70:
        catch = "Archangel Salmon"
    elif number > 40:
        catch = "Cloud Chaser"
    else:
        catch = "nothing"

    return [number, catch]

def alqafar_fish(modifier):
    number = random.randint(1, 100) + modifier
    catch = ""

    if number > 60:
        catch = "Sandstrider"
    elif number > 30:
        catch = "Dune Guppy"
    else:
        catch = "nothing"

    return [number, catch]

def fish_helper(modifier, region):
    region = region.lower()
    if region == "horimmia":
        return horrimmia_fish(modifier)
    elif region == "triptych_lux":
        return tiferet_fish(modifier)
    elif region == "sharnoth":
        return sharnoth_fish(modifier)
    elif region == "iskald":
        return iskald_fish(modifier)
    elif region == "lhodikess":
        return lhodikess_fish(modifier)
    elif region == "phronesis":
        return phronesis_fish(modifier)
    elif region == "cloudfish":
        return cloudfish(modifier)
    elif region == "alqafar":
        return alqafar_fish(modifier)
    else: return ""

def create_inventory(user):
    open_account(user)
    user_string = str(user.id)
    users = get_profile_data()

    
    if "Inventory" not in users[user_string]:
        users[user_string]["Inventory"] = {"Fish Inventory": {}, "Item Inventory": {}}
        with open("la_economia.json", "w") as f:
            json.dump(users, f)
    else: return


    
def add_fish(user, fish):

    user_string = str(user.id)
    create_inventory(user)
    users = get_profile_data()
    fish_inventory = users[user_string]["Inventory"]["Fish Inventory"]

    if fish not in fish_inventory:
        fish_inventory[fish] = {}
        fish_inventory[fish]["Count"] = 0

    if fish == "nothing":
        return
    
    fish_inventory[fish]["Count"] += 1
    with open("la_economia.json", "w") as f:
        json.dump(users, f)

# def sell_fish(ctx, user, fish, count = 1):
#     fish = format(fish)
#     user_string = str(user.id)
#     create_inventory(user)
#     users = get_profile_data()
#     fish_inventory = users[user_string]["Inventory"]["Fish Inventory"]

#     if fish not in fish_inventory or fish_inventory[fish]:
#         ctx.send(f"Sorry{}")

    
#     fish_inventory[fish]["Count"] -= 1
#     users[user_string]["Balance"] += 
#     with open("la_economia.json", "w") as f:
#         json.dump(users, f)

