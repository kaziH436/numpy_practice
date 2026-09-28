import numpy as np
rng=np.random.default_rng()

print(rng.integers(low=1, high=7, size=3))

print(rng.integers(low=1, high=7, size=(3,2)))

# seed: reproduce the same results 


print(np.random.uniform(
    low=-1, high=1, size=3
))

print(np.random.uniform(
    low=-1, high=1, size=(3,2)
))

# np.random.seed() vs rng=np.random.default_rng()?

rng=np.random.default_rng
array=np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)



# Random choice 
fruits = np.array(["apple", "orange", "coconut"])
fruit=rng.choice(fruits)
fruits=rng.choice(fruits,size=3)
fruits=rng.choice(fruits,size=(3,2))
