import random

# 12 / 12 / 12

# 2 of a kind = x2 reward of bet
# 3 of a kind = x20 reward of bet
# 3 sevens = x200 reward of bet

# iirc 10 per day limit?

slot1 = random.randint(1, 12)
slot2 = random.randint(1, 12)
slot3 = random.randint(1, 12)

print (f"{slot1} / {slot2} / {slot3}")
