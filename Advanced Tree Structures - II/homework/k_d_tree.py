class Node:
    def __init__(self, coords, parent, left=None, right=None):
        self.coords = coords
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Node at coords {}'.format(':'.join(str(part) for part in self.coords))


class KdTree:
    def __init__(self, dimensions=2):
        self.dimensions = list(range(1, dimensions+1))
        self.root = None
        self.count = 0

    def add(self, coords):
        if not isinstance(coords, tuple):
            raise Exception('The {k}-D Tree only accepts tuples!'.format(k=len(self.dimensions)))
        if len(coords) != len(self.dimensions):
            raise Exception('The {k}-D Tree only accepts tuples of size {size}!'.format(k=len(self.dimensions),
                                                                                        size=len(self.dimensions)))
        if self.root is None:
            self.root = Node(coords=coords, parent=None)
            self.count = 0
            return

        parent, direction = self._find_parent(coords)
        new_node = Node(coords=coords, parent=parent)
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
