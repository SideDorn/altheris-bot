import random

# 1d20 default
dice = 1
sides = 20

# Roll first checks for advantage/disadvantage
advantage = False
disadvantage = False

if advantage:
  roll1 = random.randint(1, sides)
  roll2 = random.randint(1, sides)
  roll = max(roll1, roll2)
  
elif disadvantage:
  roll1 = random.randint(1, sides)
  roll2 = random.randint(1, sides)
  roll = min(roll1, roll2)
  
else:
  roll = random.randint(1, sides)

print(f"You rolled {dice}d{sides} and got {roll}.") 

# Natural 1 & 20 Message Prompt

if sides == 20 and roll == 20:
  print ("Critical Success! It's a Natural 20!")

elif roll == 1:
  print ("Oh no! It's a Natural 1!")