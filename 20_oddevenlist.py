x = []   
s = int(input("Enter the number of elements for a list: "))
for i in range(s):
    a = int(input(f"Enter Number {i+1}: "))
    x.append(a)
for num in sorted(set(x)):
    freq = x.count(num)
    print(f"{num} appeared ({freq}) times and that is {'even' if freq %2 == 0 else 'odd'} number of times")


# x = [33,44,22,44,22]; [print (f"{i} appeared {'even' if x.count(i)%2==0 else 'odd'} number of times")for i in sorted(set(x))]


# x=[];s=int(input("Enter the number of elements for a list: "));[x.append(int(input(f"Enter Number {i+1}: "))) for i in range(s)];[print(f"{n} appeared ({x.count(n)}) times and that is {'even' if x.count(n)%2==0 else 'odd'} number of times") for n in sorted(set(x))]