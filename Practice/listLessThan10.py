def main():
	arr = list(map(int, str.split(input('Enter list : '))))
	res = list()
	for elem in arr:
		if(elem < 10): res.append(elem)
	print(res)

main()