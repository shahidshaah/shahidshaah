import statistics as stats
marks = []
print("Enter the list of marks followed by -1: ")
while True:
    value = int(input())
    if value<0:
        break
    # marks = marks.append(value)
    marks.append(value)
    # marks = marks + [value]
    print(marks)
avgmarks = stats.mean(marks)
print(f"The average marks is {avgmarks}")
belowAvrg = 0
aboveAvrg = 0
avgSt =  0
for value in marks:
    if value == avgmarks:
        avgSt+=1
    elif value < avgmarks:
        belowAvrg+=1
    else:
        aboveAvrg+=1
print(f"The number of below average and average and above average is {belowAvrg}, {avgSt}, {aboveAvrg}")