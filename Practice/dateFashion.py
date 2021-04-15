def table_chance(you, date):
	if(you >= 8 or date >= 8): return 2
	elif(you <= 2 or date <= 2): return 0
	else: return 1

def main():
	you = int(input('Enter self fashion : ')); date = int(input('Enter date\'s fashion : '))
	print(table_chance(you, date))

main()