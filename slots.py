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
    
def slotmachine(bet, slot1, slot2, slot3):
    bet = 100 # placeholder value for now

    slot1 = random.randint(1, 12)
    slot2 = random.randint(1, 12)
    slot3 = random.randint(1, 12)

    print (f"{slot1} / {slot2} / {slot3}")
    reward, message = slotreward(bet, slot1, slot2, slot3)
    print (f"{message}You won {reward} gold!")

slotmachine('bet', 'slot1', 'slot2', 'slot3')