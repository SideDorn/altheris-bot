import random

def nilgiri_fish(modifier):
    number = random.randint(1, 100)
    number += modifier
    catch = ""
    common_fish = ["Tuna","Salmon","Carp","Guppy"]

    
    if number > 56:
        catch = "Tilapieaux"
    elif number > 21:
        catch = "Smoky Carp"
    else:
        catch = random.choice(common_fish)
    return [number, catch]

def fish_helper(modifier, region):
    if region == "Nilgiri":
        return nilgiri_fish(modifier)
    else: return ""

test = fish_helper(0, "Nilgiri")
