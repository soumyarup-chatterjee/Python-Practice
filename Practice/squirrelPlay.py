# The squirrels in Palo Alto spend most of the day playing.
# In particular, they play if the temperature is between 60 and 90 (inclusive).
# Unless it is summer, then the upper limit is 100 instead of 90.
# Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.

def squirrel_play(temp, is_summer):
	if(is_summer and temp >= 60 and temp <= 100): return True
	if(not(is_summer) and temp >= 60 and temp <= 90): return True
	return False

def main():
	temp = int(input('Enter temperature : '))
	is_summer = input('Is summer? (Y|n) : ')
	if(is_summer == 'Y'): is_summer = True
	else: is_summer = False
	print(squirrel_play(temp, is_summer))