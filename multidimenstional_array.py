import numpy as np

array=np.array(['A', 'c','D'])
print(array.ndim)

array=np.array([['A', 'c','D'], ['D', 'E', 'F'], ['G', 'H', 'I']])
print(array.ndim)


array=np.array([[['A', 'c','D'], ['D', 'E', 'F'], ['G', 'H', 'I']], 
                [['A', 'c','D'], ['D', 'E', 'F'], ['G', 'H', 'I']], 
                [['A', 'c','D'], ['D', 'E', 'F'], ['Y', ' ', ' ']]]
               )

print(array.ndim) # results in a value error as the dimensions need to be consistent, the ['Y'] isn't
# add an " "

print(array.shape) # returns row, col but since its 3d its depth, row, col (3,3,3)




