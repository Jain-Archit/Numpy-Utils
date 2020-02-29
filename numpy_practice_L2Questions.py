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

Q4 = """ Create the following pattern without hardcoding. Use only numpy functions and the below input array a.
         a = np.array([1,2,3])
         output = array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
     """
def A4():
    a = np.arange(1,4,1)
    print(a)
    b = np.repeat(a,3)
    c = np.tile(a,3)
    print(b)
    print(c)
    d = np.r_[b,c]
    print(d)
    """ np.r_ does what? Used for row-wise merging of two arrays"""    
    
Q5 = """ Get the common items between a and b
         a = np.array([1,2,3,2,3,4,3,4,5,6])
         b = np.array([7,2,10,2,7,4,9,4,9,8])
     """
def A5():
    a = np.array([1,2,3,2,3,4,3,4,5,6])
    b = np.array([7,2,10,2,7,4,9,4,9,8])
    c = np.intersect1d(a,b)
    print(c)
    
Q6 = """ From array a remove all items present in array b
     a = np.array([1,2,3,4,5])
     b = np.array([5,6,7,8,9])
     """
def A6():
    a = np.array([1,2,3,4,5])
    b = np.array([3,5,6,7,8,9])
    c = np.setdiff1d(a,b)
    print(c)
    
Q7 = """ Get the positions where elements of a and b match
     a = np.array([1,2,3,2,3,4,3,4,5,6])
     b = np.array([7,2,10,2,7,4,9,4,9,8])
     """
def A7():
    a = np.array([1,2,3,2,3,4,3,4,5,6])
    b = np.array([7,2,10,2,7,4,9,4,9,8])
    idx = np.where(a == b)
    print(idx)

Q8 = """ Get all items between 5 and 10 from a.
     a = np.array([2, 6, 1, 9, 10, 3, 27])
     """
def A8():
    a = np.array([2, 6, 1, 9, 10, 3, 27])
    idx1 = a[a>=5]
    idx2 = a[a<=10]
    res = np.intersect1d(idx1,idx2)
    print(res)
    """ Alternative Solution
        index = np.where(np.logical_and(a>=5, a<=10))
        a[index]
    """

Q9 = """ Convert the function maxx that works on two scalars, to work on two arrays.
         def maxx(x, y):
            if x >= y:
                return x
            else:
                return y
        
            maxx(1, 5)
            #> 5
            
         a = np.array([5, 7, 9, 8, 6, 4, 5])
         b = np.array([6, 3, 4, 8, 9, 7, 1])
         pair_max(a, b)
         #> array([ 6.,  7.,  9.,  8.,  9.,  7.,  5.])
      """
def A9():
    def maxx(x,y):
        if x >= y:
            return x
        else:
            return y
        
    pair_max = np.vectorize(maxx, otypes=[float])
    a = np.array([5, 7, 9, 8, 6, 4, 5])
    b = np.array([6, 3, 4, 8, 9, 7, 1])
    c = pair_max(a, b)
    print(c)
    """
        np.vectorize : 
    """

Q10 = 

