def main():
	x = int(input('Enter dividend : '))
	y = int(input('Enter divisor : '))
	if (x % 2 == 0): print(str(x) + ' is even')
	else: print(str(x) + ' is odd')

	if(x % y == 0): print(str(x) + ' is perfectly divisible by ' + str(y))
	else: print(str(x) + ' is not divisible by ' + str(y))

main()