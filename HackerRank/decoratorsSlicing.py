def wrapper(f):
    def fun(l):
        phnoList = list()
        for i in l:
            err = len(i) - 10
            left = i[err : 5+err]
            right = i[5+err : ]
            phnoList.append('+91' + str(left) + str(right))
        return phnoList
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
