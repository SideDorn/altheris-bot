import random

def slotreward(bet, slot1, slot2, slot3):
    if slot1 == slot2 == slot3 == 7:
        message = "JACKPOT!!! You got three 7s! "
        return bet * 200, message
    
    elif slot1 == slot2 == slot3:
        message = "Huge win!! All numbers matched! "
        return bet * 20, message
    
    elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
        message = "Congratulations! Two numbers matched! "
        return bet * 2, message
    
    else:
        message = "Unfortunately you didn't win. "
        return bet * 0, message
    
def slotmachine(bet):

    slot1 = random.randint(1, 12)
    slot2 = random.randint(1, 12)
    slot3 = random.randint(1, 12)

    results = f"{slot1} / {slot2} / {slot3}"
    reward, message = slotreward(bet, slot1, slot2, slot3)
    return results, reward, message

 # Testing with a bet value of 100