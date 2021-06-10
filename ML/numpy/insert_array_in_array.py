
a= np.array(seq[0])
a = np.reshape(a,(a.shape[0],1))
a[:10]
"""
array([[3],
       [7],
       [2],
       [7],
       [1],
       [1],
       [3],
       [5],
       [5],
       [6]])
"""

a= np.insert(a, [1], np.array([1,0]), axis=1)

"""
array([[3, 1, 0],
       [7, 1, 0],
       [2, 1, 0],
       [7, 1, 0]])"""
# a = np.insert(a, 1, np.array((1, 1)), 1)
