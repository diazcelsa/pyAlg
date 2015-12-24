#!/bin/python

import numpy as np
from timeit import default_timer as timer
from collections import defaultdict
import sys

numcon = 9
arraysize = 10

#numcom = sys.argv[1]
#arraysize = sys.argv[2]

# create np.array of size "size"
items = np.arange(arraysize)
# create a length array of zeros with size "size"
length = np.zeros((arraysize,), dtype=np.int)

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

def quick_union(connections, items):
    # while length of connections define the union tree
    numconec = len(connections[0])

    # generate union array by checking all connections generated
    z = 0
    while (z < numconec):
	# get first connection
	if items[connections[0][z]] != items[connections[1][z]]:
	    # if not connected create the connection
	    items[connections[0][z]] = items[connections[1][z]]
        z = z+1
    return items

def weighted_quickunion(connections, items, length):
    # while length of connections define the union tree
    numconec = len(connections[0])

    # generate union array by checking all connections generated
    z = 0
    while (z < numconec):
        # when they are not already connected
        if items[connections[0][z]] != items[connections[1][z]]:
	    # give the root of the larger tree
	    if length[connections[1][z]] >= length[connections[0][z]]:
        	items[connections[0][z]] = items[connections[1][z]]
		# add level of length[connections[0][z]] to length of tree of items[connections[1][z]]
		if length[connections[0][z]] == 0:
		    length[connections[1][z]] += 1
		else:
		    length[connections[1][z]] += length[connections[0][z]] 
            elif length[connections[0][z]] > length[connections[1][z]]:
		items[connections[1][z]] = items[connections[0][z]]
		# add levels of length[connections[1][z]] to length of tree of items[connections[0][z]]
		if length[connections[1][z]] == 0:
		    length[connections[0][z]] += 1 
		else:
		    length[connections[0][z]] += length[connections[1][z]]

        z = z+1
    # end of check connections generated        
    return items,length


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


# start calculating time
t = timer()

# call quick_union
tree = quick_union(connections, items)

elapsed_time = timer() - t

print "This is the tree for quick union algorithm: \n",tree
print "This is the time performance (s) of quick union: \n",elapsed_time



# start calculating time
t = timer()

# call weighted quick_union
tree = weighted_quickunion(connections, items, length)

print "This is the tree for weighted quickunion algorithm: \n",tree[0]
print "This are the weights for each node: \n",tree[1]
print "This is the time performance (s) of weighted quick union: \n",elapsed_time

