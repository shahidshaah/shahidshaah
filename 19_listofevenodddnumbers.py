count = 0
x = [10]
while True:
    y = int(input("Enter Number from 0-9: "))
    x.append(y)
    count+=1
    if count == 10:
        break

zero = x.count(0)
print(zero)
one = x.count(1)
print(one)
two = x.count(2)
print(two)
three = x.count(3)
print(three)
four = x.count(4)
five = x.count(5)
six = x.count(6)
seven = x.count(7)
eight = x.count(8)
nine = x.count(9)

if zero%2 == 0 and zero != 0:
    print("Zero Occured even Times")
if zero%2 != 0: print("Zero Occured even Times")

if one%2 == 0 and one == 0:
    print("One Occured even Times")
if one%2 != 0: print("One Occured even Times")

if two%2 == 0 and two != 0:
    print("Two Occured even Times")
if two%2 != 0: print("Two Occured even Times")

if three%2 == 0 and three != 0:
    print("Three Occured even Times")
if three%2 != 0: print("Three Occured even Times")

if four%2 == 0 and three != 0:
    print("Four Occured even Times")
if four%2 != 0: print("Four Occured even Times")

if five%2 == 0 and four != 0:
    print("Five Occured even Times")
if five%2 != 0:
    print("Five Occured odd Times")

if six%2 == 0 and five != 0:
    print("six Occured even Times")
if six%2 != 0: print("six Occured even Times")

if seven%2 == 0 and six != 0:
    print("seven Occured even Times")
if seven%2 != 0: print("seven Occured even Times")

if eight%2 == 0 and seven != 0:
    print("eight Occured even Times")
if eight%2 != 0: print("eight Occured even Times")

if nine%2 == 0 and eight != 0:
    print("nine Occured even Times")
if nine%2 != 0 and nine !=0:
    print("nine Occured even Times")
