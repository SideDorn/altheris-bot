from economy_helper import get_profile_data

async def bet_checker(ctx, bet, user_string):
    user = ctx.author
    users = get_profile_data()
    user_string = str(user.id)
    if bet < 5:
        await ctx.send(f"{user}, please take note that the minimum bet is 5 gold. Thank you.")
        return False
    elif bet > users[user_string]["Balance"]:
        await ctx.send(f"{user}, please don't bet more than what you have.")
        return False
    else: return True
