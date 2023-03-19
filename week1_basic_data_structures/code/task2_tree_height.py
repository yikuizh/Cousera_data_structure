# python3

import sys
import threading

def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0

    queue = []

    node_value = list(range(n))

    root_index = parents.index(-1)

    root_node = node_value[root_index]

    queue.append(root_node) # add the root value
    # print (queue)

    # first is to create the tree

    while queue:
        #print ('queue:',queue)
        size = len(queue) # number of current level nodes
        #print ('size:',size)

        while size > 0: 

            parent_node = queue[0] # one time one node print
            #print ('parents_node:',parent_node)
            queue.pop(0)
            # child_nodes = parents.index(parent_node) # where parent index = 1 -- 3, and 4
            child_nodes = [i for i,x in enumerate(parents) if x == parent_node] # too slow

            #print ('child_nodes:',child_nodes)

            if child_nodes:
                for nodes in child_nodes:
                    queue.append(nodes)

            size = size - 1
        
        max_height +=1

    return max_height

# def main():
#n = 5
#n = int(input()) # number of nodes; also num = range(n)
#parents = [4,-1,4,1,1]
#parents = list(map(int, input().split())) # list: n integer numbers define the parents nodes of the i-th node
#print(compute_height(n, parents))

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#threading.Thread(target=compute_height).start()
