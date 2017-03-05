"""
The second part of this lab aims to implement the Breadth-First-Search (BFS) algorithm to find the nearest possible exit from a labyrinth.
We are given a labyrinth. We start from a cell denoted by 's'. We can move left, right, up and down, through empty cells '-'.
 We cannot pass through walls '*'. An exit is found when a cell on a labyrinth side is reached.
For example, consider the labyrinth below. It has size 9 x 7. We start from cell {1, 4}, denoted by 's'.
Тhe nearest exit is at the right side, the cell {8, 1}.
The path to the nearest exit consists of 12 moves: URUURRDRRRUR (where 'U' means up, 'R' means right, 'D' means down and 'L' means left).
There are two exits and several other paths to these exits, but the path URUURRDRRRUR is the shortest.
"""
from collections import deque

DIRECTIONS = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}


class Point:
    def __init__(self, x, y, direction, prev_point=None):
        self.x = x
        self.y = y
        self.direction = direction
        self.prev_point = prev_point

    def __hash__(self):
        return hash(str(self.x) + str(self.y))

    def __repr__(self):
        return "Point at {x} {y}".format(x=self.x, y=self.y)


def main():
    labyrinth, start_row, start_col = build_labyrinth()
    start_point = Point(start_row, start_col, "")
    if has_exited_lab(start_point, labyrinth):
        print("Start is at the exit.")
        return
    last_cell = exit_labyrinth(labyrinth, start_point)
    if last_cell == "No exit!":
        print(last_cell)
        return
    print("Shortest exit: {}".format(''.join(build_exit_route(last_cell))))


def exit_labyrinth(lab: list, point):
    # use bfs to traverse the graph
    visited = set()
    nodes_to_visit = deque([point])

    while nodes_to_visit:
        node = nodes_to_visit.popleft()
        if node in visited:
            continue
        visited.add(node)
        # try to traverse neighbours
        for dir, row_col in DIRECTIONS.items():
            row_to_add, col_to_add = row_col
            new_row = node.x + row_to_add
            new_col = node.y + col_to_add
            new_node = Point(x=new_row, y=new_col, direction=dir, prev_point=node)
            valid_move = (0 <= new_row < len(lab) and 0 <= new_col < len(lab[new_row])  # not out of bounds
                          and lab[new_row][new_col] != '*'   # not a wall
                          and new_node not in visited)  # not visited
            if not valid_move:
                continue  # invald move!
            if has_exited_lab(new_node, lab=lab):
                return new_node
            nodes_to_visit.append(new_node)

    return "No exit!"


def build_labyrinth():
    _ = input()
    row_count = int(input())
    labyrinth = []
    start_row, start_col = -1, -1
    for row_idx in range(row_count):
        input_row = list(input())
        if 's' in input_row:
            start_row = row_idx
            start_col = input_row.index('s')
        labyrinth.append(input_row)

    return labyrinth, start_row, start_col


def build_exit_route(end_cell):
    """ Using the last cell, build the exit route using the previous cells """
    exit_route = []
    cell = end_cell
    while cell:
        exit_route.append(cell.direction)
        cell = cell.prev_point
    return list(reversed(exit_route))


def has_exited_lab(point: Point, lab: list):
    """ Return a boolean indicating if we have exited the labyrinth """
    return (point.x == len(lab)-1 or point.x == 0) or (point.y == len(lab[0]) - 1 or point.y == 0)



if __name__ == '__main__':
    main()
