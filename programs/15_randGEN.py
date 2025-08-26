import random
count = 0
for i in range(0,5):
    a = random.randint(1, 10)
    s = int(input("Guess the random number between 1 and 10: "))
    if s == a:
        print("Correct guess!")
        count+=1
        print(f"Your current score is {count}")
    else:
        print("Wronge guess try again!")
        print(f"The random numbr was {a}")
print(f"Game over, you scored {count}")