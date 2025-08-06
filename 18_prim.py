og = []
pr = []
comp = []
nprncpm = []
yes = 0
no = 0
nes = 0
z = 2
count = 0
print("Enter 5 integer numbers: ")
for i in range(5):
    x = int(input("Enter Number:  "))

    for i in range(int(x**0.5)):   

        if x % z== 0 and x!=2:
            count+=1
            break
        z+=1
    
    og.append(x)
    if count:
        comp.append(x)
        no = 1
        count = 0
    elif x ==0  or x== 1:
        nes = 1
        nprncpm.append(x)
    else:
        yes = 1
        pr.append(x)
    z = 2
    
print(f"Original list: {og}\n")
if nes == 1:
    print(f"Neither prime nor composite: {nprncpm}\n")
if yes == 1:
    print(f"Prime Number(s): {pr}\n")
if no == 1:
    print(f"Composite Number(s)): {comp}\n")
 