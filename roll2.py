import random
import re

diceroll_regex = "^([0-9])*d([0-9]+)$"

def is_dice_roll(string):
	
	if re.match(diceroll_regex, string):
		return True
	else: return False
	
	
def base_roll(string):
	
	if is_dice_roll(string):

		numbers = string.split("d")
		rolls = []
		result = 0
		
		if numbers[0] == "":
			sides = int(numbers[1])
			roll = random.randint(1, sides)
			result += roll
			rolls.append(roll)
		else:
			dice_count = int(numbers[0])
			sides = int(numbers[1])
			i = 1
			
			while i <= dice_count and i <= 10000:
				roll = random.randint(1, sides)
				result += roll
				rolls.append(roll)
				i+=1
		
		return rolls, result


def diceroll(string):
	final_roll = 0
	results = []
	splitter_regex = '[+-]'
	
	rolls = re.split(splitter_regex, string)
	operations = re.findall(splitter_regex, string)
	
	i = 0
	while i < len(rolls):
		# just a number
		if i == 0:
			if is_dice_roll(rolls[i]):
				dicerolls, result = base_roll(rolls[i])
				results.append(dicerolls)
			else:
				result = int(rolls[i])
				results.append([result])
		else:
				if is_dice_roll(rolls[i]):
					dicerolls, result = base_roll(rolls[i])
					
					if operations[i - 1] == '-':
						j = 0
						print(len(dicerolls))
						while j < len(dicerolls):
							dicerolls[j] = dicerolls[j] * -1
							
							j += 1
					results.append(dicerolls) 
					
				else:
					result = int(rolls[i])
					if operations[i - 1] == '-':
						result *= -1
				
		final_roll += result
				
				
					
				
		
		i += 1
	

	return final_roll, results
	

print(diceroll("2147483648d2147483648"))
