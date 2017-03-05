class BoundableObject:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.width = x2 - x1
        self.height = y2 - y1
        self.mid_x = x1 + (self.width//2)
        self.mid_y = y1 + (self.height//2)

    def __repr__(self):
        return '{x1} {y1} {x2} {y2}'.format(x1=self.x1, y1=self.y1, x2=self.x2, y2=self.y2)

    def intersects(self, other):
        return (self.x1 <= other.x2
                and other.x1 <= self.x2
                and self.y1 <= other.y2
                and other.y1 <= self.y2)

    def overlaps(self, other):
        return (self.x2 <= other.x2
                and self.x1 >= other.x1
                and self.y2 <= other.y2
                and self.y1 >= other.y1)


class Cell(BoundableObject):
    max_objects = 4
    max_depth = 5

    def __init__(self, x1, y1, x2, y2, depth=0):
        super().__init__(x1, y1, x2, y2)
        self.depth = depth
        self.objects = []
        self.children = []

    def foreach_dfs(self, func, quadrant=0):
        if self.objects:
            func(self.objects, quadrant, self.depth)
        if self.children:
            for idx, child in enumerate(self.children):
                child.foreach_dfs(func, idx)

    def add_object(self, obj):
        if len(self.children) > 0:
            for cell in self.children:
                if obj.overlaps(cell):
                    cell.add_object(obj)
                    return
            self.objects.append(obj)
        else:
            self.objects.append(obj)
            if len(self.objects) >= self.max_objects:
                self._create_children()
                objs_to_remove = []
                for obj in self.objects:
                    for cell in self.children:
                        if obj.overlaps(cell):
                            cell.add_object(obj)
                            objs_to_remove.append(obj)
                # remove the objects we've moved
                for obj_to_remove in objs_to_remove:
                    self.objects.remove(obj_to_remove)

    def get_objects(self):
        """ Returns all objects from this cell"""
        if self.children:
            return [obj for child in self.children for obj in child.get_objects()] + self.objects
        else:
            return self.objects

    def _create_children(self):
        """        midX, Y2
   X1,Y2------------------------------X2, Y2
        | Cell 1      |   Cell 0     |
        |             |              |
 X1,midY|---------midX-midY---------|X2, midY
        | Cell 2      |   Cell 3     |
        |             |              |
 X1, Y1 ------------------------------X2, Y1
                    midX, Y1

        """
        if not self.children and self.depth < self.max_depth:
            cell_0 = Cell(x1=self.mid_x, y1=self.mid_y, x2=self.x2, y2=self.y2, depth=self.depth+1)
            cell_1 = Cell(x1=self.x1, y1=self.mid_y, x2=self.mid_x, y2=self.y2, depth=self.depth+1)
            cell_2 = Cell(x1=self.x1, y1=self.y1, x2=self.mid_x, y2=self.mid_y, depth=self.depth+1)
            cell_3 = Cell(x1=self.mid_x, y1=self.y1, x2=self.x2, y2=self.mid_y, depth=self.depth+1)
            self.children = [cell_0, cell_1, cell_2, cell_3]

    def report(self, subquandrant=None):
        """
        return objects that intersect with the given obj
        :param subquandrant:
        :return:
        """
        objects_in_subquandrant = []
        for obj in self.objects:
            if obj.intersects(subquandrant):
                objects_in_subquandrant.append(obj)
        for child in self.children:
            if child.intersects(subquandrant):
                objects_in_subquandrant.extend(child.report(subquandrant))

        return objects_in_subquandrant


class QuadTree(Cell):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.count = 0

    def __len__(self):
        return self.count

    def add_object(self, obj):
        super().add_object(obj)
        self.count += 1

    def get_subquandrant(self, idx):
        if idx <= 0 or idx > 4:
            raise Exception('Subquandrants are 4 only!')
        if not self.children:
            raise Exception('There are no subquandrants made yet!')
        return self.children[idx-1]
