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
