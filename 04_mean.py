x = []
while True:
   y = int (input("Enter Number: "))
   if y < 0:
      break
   x.append (y)
print("The grades are :", x) 
t = sum(x)
z = len(x)
print(f"The average of {x} is  {t/z:.2f}")
# x = []
# for _ in iter(int, 1):
#    y = int (input("Enter Number: "))
#    if y < 0:
#       break
#    x.append (y)
# print("The grades are :", x) 
# t = sum(x)
# z = len(x)
# print(f"The average of {x} is  {t/z:.2f}")
