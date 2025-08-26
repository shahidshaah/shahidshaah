PRINCIPAL_AMOUNT = []    
TIME_PERIOD = []
RATE_OF_INTERST = []
from decimal import Decimal as cal
x = int(input("Enter the number of customers: "))
i = 0
n = 1     #we have set the number of rate of interest fixed to compund aually
j = 0
while i<x:
    i+=1
    y = cal(input(f"Enter the principal amount of user {i}: "))
    PRINCIPAL_AMOUNT.append(y)
    z = cal(input(f"Enter the time period of user {i}: "))
    TIME_PERIOD.append(z)
    s = cal(input(f"Enter the rate of interest of user {i}: "))
    RATE_OF_INTERST.append(s)
    print(" ")
for p in range(x):
    j+=1
    FINAL_AMOUNT = PRINCIPAL_AMOUNT[p]*pow(1+RATE_OF_INTERST[p]/(100*n),(n*TIME_PERIOD[p]))
    C_I = FINAL_AMOUNT - PRINCIPAL_AMOUNT[p]
    print(f"Details of user {j}:-\nP.A: {PRINCIPAL_AMOUNT[p]}\tTime Period: {TIME_PERIOD[p]}\tRate of Interst (anually): {RATE_OF_INTERST[p]}\tFinal Amount: {FINAL_AMOUNT}\tC.I: {C_I}\n")