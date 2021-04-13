def main():
	x = input(); l = len(x); xor = ord(x[0])
	if len > 1:
		for i in range(1, l):
			xor = xor ^ ord(x[i])
	print(xor)

main()