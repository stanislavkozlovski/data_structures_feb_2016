class Node:
    def __init__(self, name:str, coords, parent, left=None, right=None):
        self.name = name
        self.coords = coords
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return '{name} at coords {coords}'.format(name=self.name, coords=':'.join(str(part) for part in self.coords))


class KdTree:
    def __init__(self, dimensions=2):
        self.dimensions = list(range(1, dimensions+1))
        self.root = None
        self.count = 0

    def add(self, coords, name):
        if not isinstance(coords, tuple):
            raise Exception('The {k}-D Tree only accepts tuples!'.format(k=len(self.dimensions)))
        if len(coords) != len(self.dimensions):
            raise Exception('The {k}-D Tree only accepts tuples of size {size}!'.format(k=len(self.dimensions),
                                                                                        size=len(self.dimensions)))
        if self.root is None:
            self.root = Node(name=name, coords=coords, parent=None)
            self.count = 0
            return

        parent, direction = self._find_parent(coords)
        new_node = Node(name=name, coords=coords, parent=parent)
        if direction == 'L':
            parent.left = new_node
        else:
            parent.right = new_node

        self.count += 1

    def _find_parent(self, coords):
        """
        Find the parent for given coordinates
        return the parent and the direction of the new child
        """
        depth = 0

        def __find_parent(node):
            nonlocal depth
            compare_idx = depth % len(self.dimensions)  # get the dimension by which we want to compare

            if coords[compare_idx] > node.coords[compare_idx]:
                # go right
                if node.right is not None:
                    depth += 1
                    return __find_parent(node.right)
                else:
                    return node, 'R'
            else:
                if node.left is not None:
                    depth += 1
                    return __find_parent(node.left)
                else:
                    return node, 'L'

        return __find_parent(self.root)

    def report(self, x, y, radius):
        min_x, max_x = x - radius, x + radius
        min_y, max_y = y - radius, y + radius
        valid_nodes = []

        def _find_nodes(node, depth):
            compare_x = (depth % 2) == 0
            node_x, node_y = node.coords
            if min_x <= node_x <= max_x and min_y <= node_y <= max_y:
                valid_nodes.append(node)
            if node.left is not None:
                if compare_x:
                    if min_x < node.coords[0]:
                        _find_nodes(node.left, depth + 1)
                else:
                    if min_y < node.coords[1]:
                        _find_nodes(node.left, depth + 1)
            if node.right is not None:
                if compare_x:
                    if max_x > node.coords[0]:
                        _find_nodes(node.right, depth + 1)
                else:
                    if max_y > node.coords[1]:
                        _find_nodes(node.right, depth + 1)

        _find_nodes(self.root, 0)
        return valid_nodes


def build_tree():
    tree = KdTree(2)
    addition_lines = int(input())

    for _ in range(addition_lines):
        name, x, y = input().split()
        x, y = float(x), float(y)  # convert to numbers
        tree.add((x, y), name)

    return tree


def report_range(tree):
    _, x, y, radius = input().split()
    x, y, radius = float(x), float(y), float(radius)
    return tree.report(x, y, radius)


def main():
    tree = build_tree()
    print('\n'.join(node.name for node in report_range(tree)))

if __name__ == '__main__':
    main()
