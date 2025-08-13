import numpy as np
def num3():
    x=np.array([4,5,6,7,8]) 
    y=x*2
    print(y)
# num3()
def num4():
    x=np.array([4,5,6,7,8]) 
    y=x*[2,1,7,4,3]
    print(y)
# num4()
def num5():
    x=np.array([4,5,6,7,8]) 
    y=x*np.array([5,5,2,9,1])
    print(y)
# num5()
def num6():
    x=np.array([4,5,6,7,8]) 
    y=x*np.array([5,5,2,9,1]).T
    print(y)
# num6()
def num7():
    x=np.array([4,5,6,7,8]) 
    y=x>np.array([5,5,2,9,1]).T
    print(y)
# num7

def num8():
    x=np.array([4,5,6,7,8]) 
    print(x.cumsum())
# num8()

def num9():
    x = [[4,5,6,7,7],[2,3,6,4,7],[3,4,5,7,8]]
    print(max(x))
# num9()

def num10():
    x = [[4,5,6,7,7],[5,3,6,4,7],[3,4,5,7,8]]
    print(max(x))
# num10()

def num11():
    x = np.array([[4,5,6,7,7],[2,3,6,4,7],[3,4,5,7,8]])
    print(x.max(axis = 0))   #checks the max across the row 
    print(x.max(axis = 1))   #checks the max down the columns 
# num11()

def num12():
    arr1 = np.array([4, 5, 6, 4])
    print(arr1)
    print(np.shape(arr1))     #the shpe tells you the dimentios and the size of an array
# num12()

def num13():
    arr1 = np.array([4, 5, 6, 4])
    arr2 = arr1.reshape([2,2]) 
    #reshape changes the shape (arrangement) of the array without changing its data
    print(arr1)
    print(arr2)
    print(np.shape(arr1))    
    print(np.shape(arr2))     
# num13()

def num14():
    x = np.array([[4,5,6,7,8,6],[5,6,7,2,5,4],[3,4,6,4,3,2]])
    print(x.std(axis = 0))    #standard error.....cal'd using mean, var, underroot var value happens columns wise 
    print(np.add([2,3,5,2],4))
# num14()

def num15():
    x = np.array([[4,5,6,7,8,6],[5,6,7,2,5,4],[3,4,6,4,3,2]])
    print(x[0:2])
# num15()  

def num16():
    x = np.array([[4,5,6,7,8,6],[5,6,7,2,5,4],[3,4,6,4,3,2]])
    print(x[0:1,0:5:2])
# num16()  
                    #(OR)
def num17():
    x = np.array([[4,5,6,7,8,6],[5,6,7,2,5,4],[3,4,6,4,3,2]])
    y = x[0:1,0:5:2]
    print(y)
# num17()  

def num18():
    x = np.array([[4,5,6,7,8,6],[5,6,7,2,5,4],[3,4,6,4,3,2]])
    y = x[0:1,0:5:2]
    x[0,0] = 10
    print(y)
# num18()  

def num19():
    x = np.array([[4,5,6,7,8,6],[5,6,7,2,5,4],[3,4,6,4,3,2]])
    y = x[0:1,0:5:2]
    x[0,0] = 10
    x.reshape(9,2)
    print(y)
# num19() 

def num20():
    x = np.array([[4,5,6,7,8,6],[5,6,7,2,5,4],[3,4,6,4,3,2]])
    x[0,0] = 10
    # z = x.reshape(9,2)
    # z = x.ravel()
    y = x[0:1,0:5:2]
    # y = np.array([[1,2,3]])
    z = np.hstack((x,y.T))
    print(z)
# num20()  

def num21():
    x = np.array([[4,3,2,3], [4,1,4,5], [3,5,7,2], [8,2,5,2]])
    # print(x[0:3,0:2])
    # print(x[3:0:-1, 2:0:-1])   #start, stop, and step
    print(x[[3,1,3], [0,1,3]])
# num21()






    



