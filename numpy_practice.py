import numpy as np

# way too slow
my_list = [1, 2, 3, 4]
my_list*=2
print(my_list)

# using numpy makes it faster 
array = np.array([1,2,3,4])
print(type(array))


array=array*2
print(array)
