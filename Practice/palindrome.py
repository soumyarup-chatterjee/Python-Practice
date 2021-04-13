def main():
	s = input('Enter string : '); l = len(s)
	res = True
	for i in range(-1, -l - 1, -1):
		if(s[i] != s[abs(i) - 1]): 
			res = False
			break
	print(res)

main()