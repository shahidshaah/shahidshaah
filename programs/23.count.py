x = (44,33,33,4,44,33,3)
for i in sorted(set(x)):
    y = x.count(i)
    print(f"{i} occured ({y}) times in tuple")