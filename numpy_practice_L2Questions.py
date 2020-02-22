"""
    Level L2 Starts Now
"""
import numpy as np

Q1 = "Replace all odd numbers in arr with -1 without changing arr"
def A1():
    in_ = np.arange(10)
    out_ = np.copy(in_)
    out_[in_ %2 == 1] = -1
    print(in_)
    print(out_)
    """
        Alternative Solution
    """
    output_1 = np.where(in_ %2 == 1,-1,in_)
    print(in_)
    print(output_1)
    
Q2 = "Stack arrays a and b vertically"
def A2():
    a = np.arange(3)
    b = np.arange(3,6,1)
    print(a)
    print(b)
    res = np.vstack((a,b))
    print(res)
    
Q3 = "Stack the arrays a and b horizontally."
def A3():
    a = np.arange(6).reshape(2,-1)
    b = np.arange(6,12,1).reshape(2,-1)
    print(a)
    print(b)
    res = np.hstack((a,b))
    print(res)

Q4 = " Create the following pattern without hardcoding. Use only numpy functions and the below input array a.
         a = np.array([1,2,3])
         output = array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
     "
def A4():
    a = np.arange(1,4,1)
    print(a)
    b = np.repeat(a,3)
    c = np.tile(a,3)
    print(b)
    print(c)
    d = np.r_[b,c]
    print(d)
    """ np.r_ does what?"""    
    
Q5 = 
def A5():
    