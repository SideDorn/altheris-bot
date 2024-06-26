from random import randint
from random import choice

rare = ["Wood Golem",
            "Scrap Golem",
            "Magma Golem",
            "Divine Golem",
            "Stone Golem",
            "Fire Golem",
            "Water Golem",
            "Ice Golem",
            "Earth Golem",
            "Wind Golem"]
superrare = ["Suzaku Hinomiya",
                "Rina",
                "Sir Tarcus Flammenwohl",
                "Lind Akeldama",
                "Jahlagtas",
                "Alan Voidwalker",
                "Oomfie Ellier",
                "Arghena",
                "Astaroth",
                "Tia Hellsflame"]
ssr = ["Aranlyre Diceroll",
        "Rita Dorchadas",
        "Ezekiel Guangming",
        "Daiyousei",
        "Zhiraion Gaffot",
        "Finana Ryugu",
        "Kane Cannequis"]



def character_gacha(pulls = 1):
    pulled_characters = []
    # Gacha Rates
    # SSR = 1%
    # SR = 15%
    
    remoji = '\U0001F539'
    sremoji = '\U0001F537'
    ssremoji = '\U0001F536'
    for i in range(1, pulls + 1):

        gacha_rng_result = randint(1, 100)
        if i == 10:
            catch = pity()
        elif gacha_rng_result>=1 and gacha_rng_result<=84:
            catch = f"{remoji} " + choice(rare)
        elif gacha_rng_result>=85 and gacha_rng_result<=99:
            catch = f"{sremoji} " + choice(superrare)
        elif gacha_rng_result==100:
            catch = f"{ssremoji} " + choice(ssr)


        pulled_characters.append(catch)

    return pulled_characters


def pity():
    gacha_rng_number = randint(1, 100)
    remoji = '\U0001F539'
    sremoji = '\U0001F537'
    ssremoji = '\U0001F536'
    if gacha_rng_number == 100:
        return f"{ssremoji} " + choice(ssr)
    else: 
        return f"{sremoji} " + choice(superrare)

#print(character_gacha(10))
