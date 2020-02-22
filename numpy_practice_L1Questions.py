"""
    This python code provides solution written by me for L1 problems given in the URL.
    A good practice to get to know the syntax for commonly used numpy problems.
    Note: There may be multiple solutions for a single problem.
"""

url = "https://www.machinelearningplus.com/python/101-numpy-exercises-python/"

import numpy as np

Q1 =  "Import numpy as np and print the version number."
def A1():
    # import numpy as np
    print (np.__version__)
  
Q2 = "Create a 1D array of numbers from 0 to 9"
def A2():
    a = np.arange(10)
    print(a)

Q3 = "Create a 3×3 numpy array of all True’s"
def A3():
    b = np.ones((3,3),dtype = bool)
    print(b)
    # Alternate Solution
    # np.full((3, 3), True, dtype=bool)
    
Q4 = "Extract all odd numbers from arr"
def A4():
    input_ = np.arange(10)
    output_ = input_[input_ % 2 == 1]
    print(input_)
    print(output_)

Q5 = "Replace all odd numbers in arr with -1"
def A5():
    input_ = np.arange(10)
    print(input_)
    output_ = input_
    output_[output_ % 2 == 1] = -1
    print(output_)
    """ Alternative Solution
        Use np.where()
    """
    indexes = np.where( input_ %2 == 1)
    output_1 = input_
    output_1[indexes] = -1
    print(indexes)
    print(output_1)
    
Q6 = "Convert a 1D array to a 2D array with 2 rows"
def A6():
    input_ = np.arange(10)
    print(input_)
    output_ = np.reshape(input_,(2,-1))
    print(output_)
    
Q7 = ""
def A7():
    
Q7 = ""
def A7():
    
Q7 = ""
def A7():
    
Q7 = ""
def A7():
    
Q7 = ""
def A7():
    
Q7 = ""
def A7():
    
Q7 = ""
def A7():
    