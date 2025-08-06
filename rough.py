import numpy as np
arr= np.array([[2,3,4],[3,4,6]])

# print(arr.flatten())
# print(np.ndim(arr))  #shows dimentions of array
# print(arr.itemsize)


a=np.random.randint(1,100,20).tolist()
a1= set(a)
countDict={}
for i in a1:
    countDict[i] = a.count(i)
print(countDict)
# # countNum={i:a.count(i) for i in a1}
# print(countNum)