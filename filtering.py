import numpy as np
ages = np.array([12,12,34,18,49],[29,98,20,91,2])
teenages = ages[ages<18] # doesn't return a 1d, its flattens the 2d
print(teenages)

# to perserve the shape

adults=np.where(ages>=18, ages, 0) # condition, array name, what to put in the empty place so fill value
