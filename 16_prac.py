import random as rand

person1=[]
person2=[]

store= int(input("Enter the number of times you want to play: "))

for i in range(store):
    
    num1=rand.randint(1,10)
    num2=rand.randint(1,10)

    person1.append(num1)
    person2.append(num2)

print(person1)
print(person2)

if sum(person1)>sum(person2):
    print(f"person1 won with {sum(person1)} points")
else:
    print(f"person2 won with {sum(person2)} points")