import statistics as easy
marks = []
print("Enter the list of marks: ")
below_average = 0
above_average = 0
average_std = 0
a = 1
while True:
    value = int(input(f"Marks of Student {a}: "))
    if value < 0:
        break
    marks.append(value)
    average = easy.mean(marks)
    a+=1
for value in marks:
    if value>average:
        above_average+=1
    elif value < average:
        below_average+=1
    else:
        average_std+=1
print(f"The average of marks list is {average}")
print(f"Number of below average students is {below_average}")
print(f"Number of above average students is {above_average}")
print(f"Number of average students is {average_std}")
