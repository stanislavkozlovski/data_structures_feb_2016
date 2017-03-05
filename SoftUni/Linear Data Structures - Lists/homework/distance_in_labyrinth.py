"""
We are given a labyrinth of size N x N. Some of its cells are empty (0) and some are full (x).
We can move from an empty cell to another empty cell if they share common wall.
Given a starting position (*) calculate and fill in the array the minimal distance from this position to any other cell in the array.
Use "u" for all unreachable cells. Example:
"""
from pprint import pprint
from collections import deque

NEIGHBOUR_DIRECTIONS = [(1, 0), (-1, 0),
                        (0, 1), (0, -1)]
LEVEL_UP_KEY = 'LEVEL UP'


def main():
    labyrinth = [
        [0, 0, 0, 'x', 0, 'x'],
        [0, 'x', 0, 'x', 0, 'x'],
        [0, '*', 'x', 0, 'x', 0],
        [0, 'x', 0, 0, 0, 0],
        [0, 0, 0, 'x', 'x', 0],
        [0, 0, 0, 'x', 0, 'x']
    ]
    second_labyrinth = [
        [0, 0, 0, 0, 0, 0],
        ['x', 'x', 'x', 'x', 'x', 'x'],
        [0, 'x', 0, 0, 0, 'x'],
        ['x', 0, 0, 0, 0, 'x'],
        [0, 0, '*', 0, 0, 0]
    ]

    for lab in [labyrinth, second_labyrinth]:
        row, col = get_start_index(lab)
        traverse_labyrinth(lab, row, col)
        mark_unvisited(lab)
        pprint(lab)


def traverse_labyrinth(lab: list, row: int, col: int):
    visited = {(row, col)}
    stack = deque([(row, col), LEVEL_UP_KEY])
    level = 1
    while True:
        item = stack.popleft()
        if item == LEVEL_UP_KEY:
            level += 1
            if not stack:  # stack is empty
                break
            stack.append(LEVEL_UP_KEY)
            continue
        start_row, start_col = item
        for add_row, add_col in NEIGHBOUR_DIRECTIONS:  # go to all the neighbours
            new_row, new_col = start_row + add_row, start_col + add_col
            if (0 <= new_row < len(lab) and 0 <= new_col < len(lab[new_row]) # in bounds
                    and lab[new_row][new_col] is not 'x'  # it's not a x
                    and (new_row, new_col) not in visited):  # we haven't visited it
                visited.add((new_row, new_col))
                stack.append((new_row, new_col))
                lab[new_row][new_col] = level


def mark_unvisited(lab: list):
    """ Marks all the unvisited cells in our labyrinth"""
    for row in lab:
        for idx, col in enumerate(row):
            if col == 0:
                row[idx] = 'u'


def get_start_index(labyrinth):
    for row_idx, row in enumerate(labyrinth):
        for col_idx, col in enumerate(row):
            if col == '*':
                return row_idx, col_idx


if __name__ == '__main__':
    main()
