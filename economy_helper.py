import json
import os
from random import randint

def open_account(user):
    user_string = str(user.id)
    users = get_profile_data()
    
    if user_string in users:
        return
    else:
        users[user_string] = {}
        users[user_string]["Balance"] = 100
        users[user_string]["Prismatic Shards"] = 1300       

    with open("la_economia.json", "w") as f:
        json.dump(users, f)

def get_profile_data():
    with open("la_economia.json", 'r') as f:
        users = json.load(f)

    return users

def open_keyitems(user):
    user_string = str(user.id)
    keyitems =  get_keyitem_data()
    if user_string in keyitems:
        return
    else:
        keyitems[user_string] = {}
        keyitems[user_string]["Inventory"] = {}
    with open("keyitems.json", "w") as f:
        json.dump(keyitems, f)

def get_keyitem_data():
    with open("keyitems.json", 'r') as f:
        keyitems = json.load(f)

    return keyitems

def update_economy(updated_json):
    with open("la_economia.json", 'r') as f:
        json.dump(updated_json, f)

def change_balance(user_string: str, added_money):
    users = get_profile_data()
    balance = users[user_string]["Balance"]
    balance += added_money

    users[user_string]["Balance"] = balance

    with open("la_economia.json", 'r') as f:
        json.dump(users, f)
