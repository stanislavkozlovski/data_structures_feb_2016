"""
You are given a tree of N nodes represented as a set of N-1 pairs of nodes (parent node, child node).
Write a program to read the tree from the console and find:
The root node
All leaf nodes (in increasing order)
All middle nodes (in increasing order)
* The longest path in the tree (the leftmost if several paths have the same longest length)
* All paths in the tree with given sum P of their nodes (from the leftmost to the rightmost)
** All subtrees with given sum S of their nodes (from the leftmost to the rightmost)

Sample input:
9
7 19
7 21
7 14
19 1
19 12
19 31
14 43
14 6
27
63

Output:
Root node: 7
Leaf nodes: [1, 6, 12, 21, 31, 43]
Middle nodes: [14, 19]
Longest path: 7->19->1(length = 3)
Paths of sum 27:
7 -> 19 -> 1
7 -> 14 -> 6
Subtrees of sum 63:
19 + 1 + 12 + 31
14 + 43 + 6

"""


def main():
    tree = {}
    for _ in range(int(input()) - 1):
        parent, child = [int(num) for num in input().split()]
        if parent not in tree.keys():
            tree[parent] = []
        tree[parent].append(child)
    desired_sum = int(input())
    desired_subtree_sum = int(input())
    # FIND ROOT :)
    root = find_root(tree)
    leafs = find_leafs(tree, root)
    middle_nodes = find_middle_nodes(tree, root)
    longest_path, length = find_longest_path(tree, root)
    paths_with_sum = find_paths_with_sum(tree, root, desired_sum)
    subtrees_with_sum = find_subtrees_with_sum(tree, root, desired_subtree_sum)

    print("Root node: {}".format(root))
    print("Leaf nodes: {}".format(leafs))
    print("Middle nodes: {}".format(middle_nodes))
    print("Longest path: {}(length = {})".format("->".join([str(part) for part in longest_path]), length))
    print("Paths of sum {}:\n{}".format(desired_sum, '\n'.join(  # then join every such string
        [' -> '.join([str(part) for part in path])  # convert every node in each path to str and join the path as a str
         for path in paths_with_sum])))  # for each path
    print("Subtrees of sum {}:\n{}".format(desired_subtree_sum, '\n'.join(  # then join every such string
        [' + '.join([str(part) for part in path])  # convert every node in each path to str and join the path as a str
         for path in subtrees_with_sum])))  # for each path))


def find_root(tree: dict):
    # Our root will not be a child of any node
    for key in tree.keys():
        if key not in [child for children in list(tree.values()) for child in children]:
            return key


def find_leafs(tree: dict, root: int):
    # leafs do not have children therefore are not in tree.keys()
    all_children = [child for children in list(tree.values()) for child in children]
    return list(sorted([leaf for leaf in all_children if leaf not in tree.keys() and leaf != root]))


def find_middle_nodes(tree: dict, root: int):
    return list(sorted([middle_node for middle_node in tree.keys() if middle_node != root]))


def find_longest_path(tree: dict, root: int):
    # DFS
    max_depth = 0
    nodes_to_max_depth = []

    def dfs(node: int, depth: int, prev_nodes: list):
        nonlocal max_depth, nodes_to_max_depth
        prev_nodes.append(node)

        if depth > max_depth:
            max_depth = depth
            nodes_to_max_depth = [node for node in prev_nodes]  # DEEP COPY
        if node in tree.keys():

            for child in tree[node]:
                dfs(child, depth + 1, prev_nodes)

        prev_nodes.pop()
    dfs(root, 1, [])
    return nodes_to_max_depth, max_depth


def find_paths_with_sum(tree: dict, root: int, sum: int):
    nodes_to_sum = []

    def dfs(node: int, current_sum: int, prev_nodes: list):
        nonlocal nodes_to_sum, sum
        prev_nodes.append(node)

        if current_sum >= sum:
            if current_sum == sum:
                deep_copied_nodes = [node for node in prev_nodes]
                nodes_to_sum.append(deep_copied_nodes)
            prev_nodes.pop()
            return
        if node in tree.keys():
            for child in tree[node]:
                dfs(child, current_sum+child, prev_nodes)

        prev_nodes.pop()
    dfs(root, root, [])
    return nodes_to_sum


def find_subtrees_with_sum(tree: dict, root: int, desired_sum: int):
    # create a dict, each key holding the Root of a subtree and as value: the sum of that subtree
    nodes_sum = {parent:0 for parent in tree.keys()}

    def dfs(node: int):
        nonlocal nodes_sum
        current_sum = node
        if node in tree.keys():
            for child in tree[node]:
                current_sum += child
                dfs(child)
                # current_sum += nodes_sum[child]
        nodes_sum[node] = current_sum
    dfs(root)  # fills our nodes_sum dictionary with the sum of each subtree
    desired_subtree_parents = [parent for parent, subtree_sum in nodes_sum.items() if subtree_sum == desired_sum]
    return [subtree for subtree in get_subtree_nodes(tree, desired_subtree_parents)]


def get_subtree_nodes(tree: dict, roots: list):
    """ Given roots of subtrees, return all the nodes for each subtree"""
    subtree_nodes = []
    current_subtree = []

    def dfs(node: int):  # traverse the subtree and add it's nodes to our current subtree
        nonlocal current_subtree
        current_subtree.append(node)
        if node in tree.keys():
            for child in tree[node]:
                dfs(child)
    for root in roots:
        dfs(root)
        subtree_nodes.append([node for node in current_subtree])
        current_subtree = []  #  reset it
    return subtree_nodes

if __name__ == '__main__':
    main()