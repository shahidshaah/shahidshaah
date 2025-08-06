x = str(input("Enter the sequence: "))
count = 0
lg = len(x)
lg = lg-1
for i in range(lg):    
    if x[i] == x[lg] :
        count = count + 1
        lg = lg - 1
lg = len(x)
if count == lg-1:
    print("Palandrome")
else:
    print("Not a palandrom") 


# x = str(input("Enter the sequence: "))
# y = x[::-1]
# if x == y:
#     print("This is a palandrome")
# else:
#     print("This not a palandrome")

