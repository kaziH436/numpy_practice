import numpy as np

array=np.array([[['A', 'c','D'], ['D', 'E', 'F'], ['G', 'H', 'I']], 
                [['A', 'c','D'], ['D', 'E', 'F'], ['G', 'H', 'I']], 
                [['A', 'c','D'], ['D', 'E', 'F'], ['Y', ' ', ' ']]]
               )

# chain indexing 
print(array[0][0][0]) # prints 'A'

# multidomentional indexing, faster 
print(array[0,0,0]) # print 'A'


# excersize
word = array[0,0,0]+array[2,0,0] + array[2,0,0]
print(word)