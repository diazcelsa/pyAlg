import numpy as np
from timeit import default_timer as timer
from collections import defaultdict
from unionfind import *

side = 5
totsize = side*side

# generate intial blocked zeros matrix
grid = np.zeros((side,side), dtype=np.int)

# create np.array of size "size"
items = np.arange(totsize+2)

# create a length array of zeros with size "size"
length = np.zeros((totsize+2,), dtype=np.int)

# generate unions of imaginary "a"(totsize +1) and "b" (totsize +2)
row = np.arange(side)
conne = np.zeros((2,side*2), dtype=np.int)

# connect a (totsize+1) to upper side of matrix 0->side-1
c = 0
while (c < side):
    conne[1][c] = items[totsize]
    conne[0][c] = items[c]
    c += 1

# connect b (totsize+2) to botton side of matrix totsize-1->totsize-side-1
d = totsize-side
while (d < totsize):
    conne[1][c] = items[totsize+1]
    conne[0][c] = items[d]
    d += 1
    c += 1

# generate unions of those connections with weighted quick union
tree = weighted_quickunion(conne, items, length)

print conne
print tree[0]
print tree[1]

# start the loop until percolates
count = 0
while (count < totsize):
    # generate a vacancy randomly in size "totsize"
    vac = np.random.choice(totsize, size=1)
    
    
    # generate unions after open vacancy

    # check if a connected to b




