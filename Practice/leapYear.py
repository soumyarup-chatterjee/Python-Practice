# In the Gregorian calendar, three conditions are used to identify leap years:
# 
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

def is_leap(year):
	if(year % 4 == 0):
		if(year % 100 == 0):
			if(year % 400 == 0): return True
			else: return False
		return True
	return False

def main():
	year = int(input())
	print(is_leap(year))

main()