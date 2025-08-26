x = int(input("Enter the number of elements for a list: "))
list = []
flag = 0
for i in range(x):
    y = int(input(f"Enter number {i+1}: "))
    list.append(y)
s = int(input("Enter the number you want to search in a list: "))
for index,j in enumerate(list):
    if(s==j):
        flag+=1
        print(f"{j} exists at index {index}")
if flag == 0:
    print("Number not found") 