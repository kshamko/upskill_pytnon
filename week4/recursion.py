l = [11,22,43,64]

for i in l:
    print(i)


def printRecursive(l):
    if len(l) == 0:
        return
    else:
        print(l[0])
        printRecursive(l[1:])        

print("--------")
printRecursive(l)

fib(10)
