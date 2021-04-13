def getCount(term, arr, len):
	count = 0
	for i in range(len):
		if(arr[i] == term): count += 1
	return count

def isPresent(id, arr):
	for element in arr:
		if(element[0] == id): return True
	return False

def countSort(arr, len):
	result = list()
	for i in range(len):
		if(isPresent(arr[i], result)): continue
		result.append([arr[i], getCount(arr[i], arr, len)])
	return result

def main():
	arr = list(map(int, str.split(input())))
	l = len(arr); res_id = -1
	result = countSort(arr, l)
	for x in result:
		if(x[1] == 1):
			res_id = x[0]
			break
	print(res_id)

main()