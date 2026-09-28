import numpy as np

array1=np.array([1,2,3])
array2=np.array([2,3,3])

print(array1+array2)
print(array1-array2)
print(array1*array2)
print(array1/array2)
print(array1**array2)


# comparison 
scores = np.array([91,99,92,29,0])
print(scores==91)
print(scores>20)

#filtering
scores[scores<60]=0
print(scores)