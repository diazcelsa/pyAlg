import numpy as np
from time import perf_counter


t = perf_counter()

a = np.arange(10)
b = np.arange(10)

for i in a:
    for j in b:
        z = i*j

elapsed_time = perf_counter() - t

print(elapsed_time)
