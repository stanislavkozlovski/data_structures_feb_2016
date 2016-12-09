"""
The first part of this lab aims to implement the DFS algorithm (Depth-First-Search) to traverse a graph and find its
 connected components (nodes connected to each other either directly,
or through other nodes). The graph nodes are numbered from 0 to n-1. The graph comes from the console in the following format:
First line: number of lines n
Next n lines: list of child nodes for the nodes 0 … n-1 (separated by a space)
Print the connected components in the same format as in the examples below:
"""


def main():
    visited = set()  # holding the nodes we've visited
    graph = build_graph()

    # get the components
    components = []
    for node in sorted(graph.keys()):
        if node not in visited:
            components.append(get_component(graph, node, visited))

    # print the components
    for component in components:
        if component:
            print("Connected components: {component}".format(
                component=' '.join(
                    [str(part) for part in component]  # convert to string for string join to work
                )))


def build_graph():
    graph = {
        # key: Parent
        # value: List of the children
    }
    # build the graph
    for index in range(int(input())):
        user_input = input()
        children = []
        if user_input:
            children = [int(child) for child in user_input.split()]

        graph[index] = children

    return graph


def get_component(graph, start_node, visited):
    nodes = []  # the nodes in the component

    def __dfs(node):
        nonlocal nodes
        nonlocal visited
        if node not in visited:
            visited.add(node)
            for child in graph[node]:
                __dfs(child)
            nodes.append(node)


    __dfs(start_node)
    return nodes


if __name__ == '__main__':
    main()
