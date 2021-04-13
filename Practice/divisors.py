def main():
	num = int(input('Enter number : '))
	res = [1]
	for i in range(2, (num // 2 + 1)):
		if(num % i == 0): res.append(i)
	print(res)

main()