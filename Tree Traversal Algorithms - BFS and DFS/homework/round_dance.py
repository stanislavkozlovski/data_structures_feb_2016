"""
Build a round dance, where everybody is holding a friend. You are given the number the person who should lead the dance.
Every person has a unique number. Every friendship is two-way. If Stamat is a friend of Minka, Minka is a friend of Stamat.
There are no circular friendships (e.g. A is friend to B, C is friend to B and A is friend to C).
Your task is to find the longest round dance, such that it starts with K-person and every person in it is holding his/her friend.
Input:
At the first line the number F is given – the number of friendships.
At the second line the number K is given – the man, who leads the dance.
Each of the next F lines holds a friendship between two people, separated by a space.
Output:
Print at the console the number of people in the longest dance.
"""


def main():
    friendship_count = int(input())
    dance_leader = int(input())
    graph = build_graph(friendship_count)
    print(find_longest_dance(graph, dance_leader))


def find_longest_dance(graph, start_node):
    max_depth = 0
    visited = set()

    def dfs(node, depth):
        nonlocal max_depth, visited
        if node in visited:
            return
        visited.add(node)

        if depth > max_depth:
            max_depth = depth

        for child in graph[node]:
            dfs(child, depth + 1)

    dfs(start_node, 1)  # start the traversal

    return max_depth


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
