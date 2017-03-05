"""
You are given a tree holding N nodes. Each node holds a unique number. Each node can have child nodes.
Find the longest path by sum of the nodes from leaf to leaf.

Input:
Read the input from the console.
The first line holds the number N – the count of the nodes of the tree.
The second line holds the number M – the count of the edges between nodes in the tree.
Each of the next M lines holds an edge is in format “p1 p2”.

Output:
Print at the console the sum of the nodes of the largest path from leaf to leaf.
"""


def main():
    _ = int(input())
    edge_count = int(input())
    graph = build_graph(edge_count)

    max_sum = 0
    for node in graph.keys():
        current_sum = find_longest_dance(graph, node)
        if current_sum > max_sum:
            max_sum = current_sum
    print(max_sum)


def find_longest_dance(graph, start_node):
    max_sum = 0
    visited = set()

    def dfs(node, current_sum):
        nonlocal max_sum, visited
        if node in visited:
            return
        visited.add(node)
        current_sum += node
        if current_sum > max_sum:
            max_sum = current_sum

        for child in graph[node]:
            dfs(child, current_sum)
        current_sum -= node

    dfs(start_node, 0)  # start the traversal

    return max_sum


def build_graph(count):
    graph = {
        # key: node (the parent)
        # value: list of nodes (the children)
    }
    for _ in range(count):
        parent, child = [int(node) for node in input().split()]
        if parent not in graph.keys():
            graph[parent] = []
        if child not in graph.keys():
            graph[child] = []

        graph[parent].append(child)
        graph[child].append(parent)

    return graph


if __name__ == '__main__':
    main()
