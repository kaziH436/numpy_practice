import numpy as np

array = np.array([1,2,3,4,5], 
                 [6,7,8,9,10])
print(np.argmin(array)) # returns index of min in array

print(np.sum(array,axis=0)) # sums the cols
print(np.sum(array,axis=1)) # sums the rows