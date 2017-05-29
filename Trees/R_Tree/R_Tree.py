"""
A really incomplete and inefficient implementation of an R-Tree
    Supports:
    - addition ( i hope )
Easy optimizations:
Add some sort of heuristic or basic logic for splitting a node. Currently it splits without any logic
    Will significantly decrease search time
Todos:
Add search
"""


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def contains(self, r_obj: 'Rectangle'):
        """
        returns a boolean indicating if the rectangle is entirely in this rectangle's bounds
        """
        return self.x1 <= r_obj.x1 and self.x2 >= r_obj.x2 and self.y1 >= r_obj.y1 and self.y2 <= r_obj.y2


class RObject(Rectangle):
    """
    Describes a leaf object in the R-Tree, e.g a Restaurant
    """
    def __init__(self, x1, y1, x2, y2, object_type):
        super().__init__(x1, y1, x2, y2)
        self.object_type = object_type

    def __eq__(self, other):
        return self.x1 == other.y1 and self.y2 == other.y2 and self.x1 == other.x1 and self.x2 == other.x2 and self.object_type == other.object_type


class RNode(Rectangle):
    """
    Describes a boundable rectangle
    """
    def __init__(self, x1, y1, x2, y2, max_order):
        super().__init__(x1, y1, x2, y2)
        self.children = []
        self.max_order = max_order

    def add(self, r_obj: RObject):
        if len(self.children) > 0 and isinstance(self.children[0], self.__class__):
            # We have other RNode children, so find this node a better place
            for ch in self.children:
                if ch.contains(r_obj):
                    return ch.add(r_obj)
            raise Exception('Could not find a RNode to add it in :O')
        else:
            # Add the RObject here
            self.children.append(r_obj)
            if len(self.children) == self.max_order:
                # split, by generating two new RNodes
                first_half = self.create_minimum_bounding_rnode(self.children[0:self.max_order//2], self.max_order)
                second_half = self.create_minimum_bounding_rnode(self.children[self.max_order//2:], self.max_order)
                self.children = [first_half, second_half]

    def create_minimum_bounding_rnode(self, children, mx_order):
        """ Given a couple of Rectangle children, create a Minimum Bounding RNode which
            can contain all of the rectangles """
        # find the min x1, max y1, min y2 and max x2
        min_x1, max_y1, min_y2, max_x2 = float('inf'), float('-inf'), float('inf'), float('-inf')
        for child in children:
            if child.x1 < min_x1:
                min_x1 = child.x1
            if child.y1 > max_y1:
                max_y1 = child.y1
            if child.y2 < min_y2:
                min_y2 = child.y2
            if child.x2 > max_x2:
                max_x2 = child.x2

        r_node = RNode(min_x1, max_y1, max_x2, min_y2, max_order=mx_order)
        r_node.children = children
        return r_node


class RTree:
    def __init__(self, x1, y1, x2, y2, max_order):
        self.root = RNode(x1, y1, x2, y2, max_order=max_order)

    def add(self, r_object: RObject):
        self.root.add(r_object)