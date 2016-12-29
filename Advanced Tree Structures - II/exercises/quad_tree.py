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
