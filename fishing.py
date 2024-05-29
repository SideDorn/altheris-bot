import random

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
    number = random.randint(1,100 + modifier)
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


def fish_helper(modifier, region):
    region = region.lower()
    if region == "horrimmia":
        return horrimmia_fish(modifier)
    elif region == "triptych_lux":
        return tiferet_fish(modifier)
    else: return ""

test = fish_helper(0, "horrimmia")
