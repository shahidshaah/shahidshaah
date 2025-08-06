x = [2,3,4,5,5,6,5,4,4,2,1,3]
t = len(x)
list = []
wednesday = 0                                                                           
s = int(input("Enter the number you want to search: "))
for i in set(x):
    if s == i:
        wednesday+=1
        print(f"{i} is present more than once")
print("It is present at index(s): ")
for i in range(t):
    if s == x[i]:
        list.append(i)
print(*list)
if wednesday == 0:
    print("No duplicate number is found")