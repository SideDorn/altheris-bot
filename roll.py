import random

# 1d20 default
dice = 1
sides = 20

roll = random.randint(1, sides)

print(f"You rolled {dice}d{sides} and got {roll}.") 

if sides == 20 & roll == 20:
    print ("Critical Success! It's a Natural 20!")
    
elif roll == 1:
    print ("Oh no! It's a Natural 1!")