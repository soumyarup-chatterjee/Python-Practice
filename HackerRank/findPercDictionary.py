def takeInput():
	n = int(input())
	details = dict()
	for i in range(n):
		tmp = str.split(input())
		details[str.strip(tmp[0])] = [float(tmp[x]) for x in range(1, len(tmp))]
	query = str.strip(input())
	return (details, query)

def calcSum(arr):
	sum = 0
	for num in arr:
		sum += num
	return sum

def main():
	details, query = takeInput()
	if(query in details): 
		result = "{:.2f}".format(calcSum(details[query]) / len(details[query]))
		print(result)

main()