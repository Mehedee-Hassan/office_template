


test = np.array([[ [ 1,2],[3,4]],[[5,6],[7,8]] ])
test.reshape(1,8)
"""
array([[1, 2, 3, 4, 5, 6, 7, 8]])
"""

test.reshape(-1,1)
""" 
    12 elements with reshape(-1,1) corresponds to an array with 
    x =12/1=12 rows and 1 column. 
    12 elements with reshape(1,-1) 
    corresponds to an array with 1 row and x =12/1=12 columns

"""

"""
array([[1],
       [2],
       [3],
       [4],
       [5],
       [6],
       [7],
       [8]])

"""
