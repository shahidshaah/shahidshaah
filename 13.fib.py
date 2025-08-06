num = int(input("Enter the number to which you want generate fibonacci series: "))
FIB = []
def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return fib(x-1)+fib(x-2)
for i in range(num):
    FIB.append(fib(i))
print(FIB)