def main():
	n = int(input())
	scores = list(map(int, str.split(input())))
	liMax = max(scores)
	liRest = [x for x in scores if x < liMax]
	print(max(liRest))

main()