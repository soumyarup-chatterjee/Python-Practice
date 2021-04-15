def main():
	x = int(input())
	y = int(input())
	z = int(input())
	n = int(input())
	print([[cx, cy, cz] for cx in range(x + 1) for cy in range(y + 1) for cz in range(z + 1) if(cx + cy + cz != n)])

main()