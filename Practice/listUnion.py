def present(term, arr):
	for itr in arr:
		if(itr == term): return True
	return False

def main():
	arr1 = list(map(int, str.split(input('1st List : '))))
	arr2 = list(map(int, str.split(input('2nd List : '))))
	union = list()
	for i in arr1:
		if(not(present(i, union)) and present(i, arr2)): union.append(i)
	print(union)

main()
