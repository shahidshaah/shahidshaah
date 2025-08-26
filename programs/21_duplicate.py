x = int(input("Enter the number of elements for a list: "))
list = []
flag = 0
for i in range(x):
    y = int(input(f"Enter Number {i+1}: "))
    list.append(y)
for dup in set(list):
    if list.count(dup)>=2:
        print(f"{dup} occuered {list.count(dup)} times")
        flag+=1
if flag == 0:
    print("There are no duplicate elements in a list")