x = int(input("Enter the number to generate its table: "))
count = 1
def condition():
    global count
    if count > 10:
        return 'STOP'
    flag = count
    count += 1
    return flag
for i in iter(condition,'STOP'):
    print(f"{x} x {i} = {x*i}")
