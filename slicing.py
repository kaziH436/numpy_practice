import numpy as np

# ROW SELECTION
array=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]]
               )

#array[start:end:step] end is exclusive, step and start is inclusive
print(array[0:3])

# reversed
print(array[::-1])



# COLUMN SELECTION 
#array[row,start:end:step]

# prints all cols in 0 to 2 index
print(array[:,0:3])
print(array[:, ::-1])

# first two rows and first two cols 
print(array[0:2, 0:2])

# results in 3 4 7 8
print(array[0:2, 2:])