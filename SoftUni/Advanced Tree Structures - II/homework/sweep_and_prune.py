OBJECT_WIDTH, OBJECT_HEIGHT = 10, 10


class BoundableObject:
    def __init__(self, name, x1, y1):
        self.name = name
        self.x1 = x1
        self.x2 = x1 + OBJECT_WIDTH
        self.y1 = y1
        self.y2 = y1 + OBJECT_HEIGHT

    def __repr__(self):
        return '{x1} {x2}'.format(x1=self.x1, x2=self.x2,)

    def __str__(self):
        return self.name

    def __gt__(self, other):
        return self.x1 > other.x1

    def __lt__(self, other):
        return self.x1 < other.x1

    def intersects(self, other):
        return (
            self.x1 <= other.x2 and other.x1 <= self.x2
            and self.y1 <= other.y2 and other.y1 <= self.y2)

    def change_coords(self, new_x, new_y):
        self.x1 = new_x
        self.x2 = self.x1 + OBJECT_WIDTH
        self.y1 = new_y
        self.y2 = self.y1 + OBJECT_HEIGHT


def insertion_sort(arr):
    for idx in range(1, len(arr)):
        pos = idx
        curr_value = arr[idx]

        while pos > 0 and curr_value < arr[pos-1]:
            arr[pos] = arr[pos-1]
            pos -= 1

        arr[pos] = curr_value

    return arr


class Game:
    def __init__(self):
        self.has_started = False
        self.objects = []
        self.tick_count = 1

    def game_tick(self):
        self.objects = insertion_sort(self.objects)
        self.check_for_collisions()
        self.tick_count += 1

    def check_for_collisions(self):
        for idx, obj in enumerate(self.objects):
            for sec_idx in range(idx + 1, len(self.objects)):
                if obj.intersects(self.objects[sec_idx]):
                    print('({tick}) - {obj1} collides with {obj2}'.format(tick=self.tick_count, obj1=obj,
                                                                          obj2=self.objects[sec_idx]))
                else:  # no need to continue since this is a sorted array
                    break

    def handle_commands(self):
        command = input()
        if not self.has_started:
            if command == 'start':
                self.has_started = True
                return
            if command.startswith('add'):
                name, x1, y1 = command.split()[1:]
                x1, y1 = int(x1), int(y1)
            self.objects.append(BoundableObject(name, x1, y1))
        else:  # game has started
            if command.startswith('move'):
                name, x1, y1 = command.split()[1:]
                x1, y1 = int(x1), int(y1)
                obj = self.find_object_with_name(name)
                if obj is None:
                    raise Exception('No such object in the array!')
                obj.change_coords(x1, y1)

            self.game_tick()

    def find_object_with_name(self, name):
        for obj in self.objects:
            if obj.name == name:
                return obj


def main():
    game = Game()
    while True:
        game.handle_commands()


if __name__ == '__main__':
    main()