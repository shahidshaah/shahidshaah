x = int(input("Enter the number of elements for a tuple: "))
t = []
count = 0
for i in range(x):
    s = int(input(f"Enter number {i+1}: "))
    t.append(s)
for i in t:
    if i%2 == 0:
        count+=1
my_tuple = tuple(t)
if count==x:
    print(f"All elements in tuple: {my_tuple} are even")
else:
    print(f"All elements in tuple: {my_tuple} are not even")