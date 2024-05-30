import random

# 2 of a kind = x2 reward of bet
# 3 of a kind = x20 reward of bet
# 3 sevens = x200 reward of bet

# iirc 10 per day limit?

def slotreward(bet, slot1, slot2, slot3):
    if slot1 == slot2 == slot3 == 7:
        return bet * 200
    
    elif slot1 == slot2 == slot3:
        return bet * 20
    
    elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
        return bet * 2
    
    else:
        return bet * 0

bet = 100 # empty by default 

slot1 = random.randint(1, 12)
slot2 = random.randint(1, 12)
slot3 = random.randint(1, 12)

print (f"{slot1} / {slot2} / {slot3}")
reward = slotreward(bet, slot1, slot2, slot3)
print (f"You earned {reward}.")

