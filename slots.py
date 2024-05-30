import random

def slotreward(bet, slot1, slot2, slot3):
    if slot1 == slot2 == slot3 == 7:
        return bet * 200
    
    elif slot1 == slot2 == slot3:
        return bet * 20
    
    elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
        return bet * 2
    
    else:
        return bet * 0
    
def slotmachine(bet, slot1, slot2, slot3):
    bet = 100 # placeholder value for now

    slot1 = random.randint(1, 12)
    slot2 = random.randint(1, 12)
    slot3 = random.randint(1, 12)

    print (f"{slot1} / {slot2} / {slot3}")
    reward = slotreward(bet, slot1, slot2, slot3)
    print (f"You earned {reward}.")

slotmachine('bet', 'slot1', 'slot2', 'slot3')