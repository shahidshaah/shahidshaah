"""
➤ Q1: Create an array from 1 to 10 and print all even numbers.
➤ Q2: Create a 3x3 matrix filled with 0s, then change the center to 9.
➤ Q3: Multiply two 2D arrays of the same shape element-wise.


NumPy is faster, but only when it matters (large data).
For small data, Python's sum() can sometimes be slightly quicker due to lower overhead.
"""

import numpy as np

def num1():
    print("1---------------")
    # boolean masking or filtering
    arry = np.arange(1, 11) 

    even_arr = arry[arry % 2 == 0]  # 0 1 0 1 1 0 0 1 0 0 1 --> 1 1 1 1 1  
    print("Even numbers:", even_arr) 

    print("2---------------")
    #2
    matric=np.zeros((3,3), dtype=int)
    matric[1,1]=9
    print(matric)

    
    # matric=np.zeros(10).astype(int)
    # print(matric)

    #3
    print("3---------------")
    TwodArr1=np.array([
        [1,2,3,4],
        [5,4,3,2]
    ])
    TwodArr2=np.array([
        [6,7,5,4],
        [5,4,3,7]
    ])
    print(TwodArr1*TwodArr2)

# num1()/


def num2():
    arr1=np.array([2,3,4,5,6,7,4])
    print("sum: ",np.sum(arr1))
    print("mean: ",np.mean(arr1))
    # print(np.mode(arr1))
    print("median: ",np.median(arr1))
    print("max: ",np.max(arr1))
    print("min: ",np.min(arr1))
    print(np.linspace(20, 1, 20))

# num2()

def num3():
    """
    this function is used to check shape, log, sqrt, exp
    """
    arr=np.array([[2,3,4,5,6,7]])
    print(arr.shape)
    b=arr.reshape((2,3))
    print(b)
    print(b.shape)
    print("-------------")

    a = np.array([8, 2, 3])
    sqrt_a = np.sqrt(a) 
    print("sqrt= ",sqrt_a)
    print("-------------")

    log_a = np.log(99)  #WHAT POWER DO WE NEED TO USE ON E TO GET 99 [e=2.718]
    print("log= ",log_a)
    print("-------------")
    c=np.exp(arr)
    print("exponention= ",c)

    
num3()
