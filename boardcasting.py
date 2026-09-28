import numpy as np

# this lets numpy perform operations on matrixes of different sizes 
# by expanding the smaller matrix in dimensions 

# this is possible when the dimensions have the same size
# or one of the dimensions has a size of 1 

array1 = np.array([[1,2,3,4,]])
array2=np.array([1],[2],[3],[4])
print(array1.shape) # 1,4
print(array2.shape) # 4,1 
# possible to boardcast since one of the dimensions is 1

print(array1*array2)



