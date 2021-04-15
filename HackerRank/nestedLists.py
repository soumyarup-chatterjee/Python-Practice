def take_input():
	n = int(input())
	finalList = list()
	for i in range(n):
		name = str.strip(input()); score = float(input())
		finalList.append([name, score])
	return (finalList, n)

def main():
	details, n = take_input()
	liMax = min(details, key= lambda details: details[1])
	liRest = [x for x in details if(x[1] > liMax[1])]
	liRest_min = min(liRest, key = lambda liRest: liRest[1])
	runnerUps = [x[0] for x in liRest if(x[1] == liRest_min[1])]
	runnerUps.sort(key = lambda runnerUps: runnerUps[0])
	for name in runnerUps:
		print(name)

main()