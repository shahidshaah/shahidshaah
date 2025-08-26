x = int(input("Enter the number of elements for a list: "))

factorial = 1
v=1

FACT = []
BREAKDOWN = []
for i in range(x):
    factorial = factorial*(x-i)
    FACT.append(factorial)
print(factorial)

list = []

for i in range(x):
    y = int(input(f"Enter Number {i+1}: "))
    list.append(y)
print(f"Orginal List: {x}")

