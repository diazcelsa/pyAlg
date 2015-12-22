#!/bin/python3

import numpy as np
from timeit import default_timer as timer
from collections import defaultdict

numcon = 8
arraysize = 20
points = np.arange(arraysize)

# Function to generate a number of connections for a given size random array
def genconnections(ncon,points):
    conne = np.zeros((2,ncon), dtype=np.int)

    # Generate randomly non-repeated connections
    i = 0
    while (i < ncon):
        index = i
        a = np.random.choice(points, size=2)
        if a[0] != a[1]:
            if i == 0:
                conne[0][i] = a[0]
                conne[1][i] = a[1]
                i = i+1
            elif i > 0:
	        val = 0
                for j in range(index):
                    if conne[0][j] == a[0] and conne[1][j] == a[1]:
                         val = 0
		         break
		    elif conne[1][j] == a[0] and conne[0][j] == a[1]:
		         val = 0
		         break
                    else:
		         val = 1
	        if val == 1:
                    conne[0][i] = a[0]
                    conne[1][i] = a[1]
                    i = i+1
    return conne


# Function to get the different nets out of the nodes and edges
def clusternets(connectsize,connects):
	# Find query, define blocks of connections
	blocks = defaultdict(list)
	keys = np.zeros((connectsize,), dtype=np.int)
	# counts the index of the matrix
	i = 0
	# counts the keys or blocks
	u = 0
	while (i < connectsize):
      		if keys[i] == 1:
       		    	i = i+1
           		continue
      		blocks[u].append(connects[0][i])
      		blocks[u].append(connects[1][i])
      		keys[i] = 1
      		# check all the connections
      		# while connected node not found, keep on checking out
      		use = connectsize-np.count_nonzero(keys)
      		z = 0
      		while (z < use):
           		for j in range(i+1,connectsize):
                		if any(item == connects[0][j] for item in blocks[u]):
                     			# check if the node already in my net
                     			if any(item == connects[1][j] for item in blocks[u]):
                          			# remove column of my list and keep on looking for nonrepeated nodes
                          			keys[j] = 1
                     			else:
                          			# add the node to the net
                          			blocks[u].append(connects[1][j])
                          			# remove column from matrix
                          			keys[j] = 1
                		elif any(item == connects[1][j] for item in blocks[u]):
                     			# check if the node already in my net
                     			if any(item == connects[0][j] for item in blocks[u]):
                          			# remove column of my list and keep on looking for nonrepeated nodes
                          			keys[j] = 1
                     			else:
                          			# add the node to the net
                          			blocks[u].append(connects[0][j])
                          			# remove column from matrix
                          			keys[j] = 1
           		z = z+1
      		# end of the check for that block, no more connections in the net, start a new block
      		i = i+1
      		u = u+1

	return blocks




# Start calculating time
t = timer()

# Generate the connections
connections = genconnections(numcon,points)

elapsed_time = timer() - t

print "these are my connections: \n",connections
print "This is the time performance (s) of connections generation: \n",elapsed_time



# start calculating time
t = timer()

# Find the nets
nets = clusternets(numcon,connections)

elapsed_time = timer() - t

print "these are my nets: \n",nets
print "This is the time performance (s) of connections generation: \n",elapsed_time




