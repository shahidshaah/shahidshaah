a = int(input("Enter the number to find its factorail: "))
def fact(x):
    if x<=1:
        return 1
    return fact(x-1)*(x)
print(f"The factorial of {a} is {fact(a)}")