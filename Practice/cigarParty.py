def cigar_party(weekend, num):
	if(weekend and num >= 40): return True
	if(not(weekend) and num >= 40 and num <= 60): return True
	return False

def main():
	num = int(input('Enter numebr of cigars : ')); weekend = input('Is this a weekend? (Y/n) : ')
	if(weekend == 'Y'): weekend = True
	else: weekend = False
	if(cigar_party(weekend, num)): print('Party is successful')
	else: print('Party is not successful')

main()