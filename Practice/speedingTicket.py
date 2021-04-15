# You are driving a little too fast, and a police officer stops you.
# Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
# If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. 
# If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

def speeding_ticket(speed, is_birthday):
	limit = [60, 80]
	if(is_birthday):
		limit[0] += 5
		limit[1] += 5
	
	if(speed <= limit[0]): return 0
	elif(speed > limit[0] and speed <= limit[1]): return 1
	else: return 2


def main():
	speed = int(input('Enter speed : ')); is_birthday = input('Birthday? (Y|n) : ')
	if(is_birthday == 'Y') : is_birthday = True
	else: is_birthday = False
	print(speeding_ticket(speed, is_birthday))

main()