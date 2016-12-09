"""
You have a connected directed graph with N nodes and M edges. You are given the directed edges from one node to another.
The nodes are numbered from 0 to N-1 inclusive. Check whether the graph is a tree and find its root.

Input:
Read the input data from the console.
The first line holds the number of nodes N.
The first line holds the number of edges M.
Each of the following M lines hold the edges: two numbers separated by a space.
The first number is the parent node; the second number is the child node.

Output:
Print at the console the number of the root node in case the graph is a tree.
If there is no root, print “No root!” at the console.
If multiple root nodes exist, print "Multiple root nodes!" at the console.
"""
node_count = int(input())
edge_count = int(input())
node_has_parent = {node: False for node in range(node_count)}

# read edges and save which node has a parent
for _ in range(edge_count):
    parent, child = [int(node) for node in input().split()]
    node_has_parent[child] = True
# get the nodes without parents
roots = [node for node, has_parent in node_has_parent.items() if not has_parent]

if not roots:
    print("No root!")
elif len(roots) == 1:
    print(roots[0])
else:
    print("Multiple root nodes!")