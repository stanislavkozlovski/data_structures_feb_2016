"""
You are given a matrix N x M and a start position. Your task is to traverse the matrix using the movements of the horse from the chess game and marking where you have gone.
1. Visit the start position and assign 1 in it.
2. If a position holds the value V, assign V+1 in all not-visited cells which can be reached by movement of the horse from this position.
3. Repeat the previous step until all positions are visited.

Input:
The first line holds the number N – the number of rows in the matrix.
The second line holds the number M – the number of the columns in the matrix.
The third line holds the number R – the row of the start position of the horse.
The fourth line holds the number C – the column of the start position of the horse.
The cell at the top left corner is (0, 0) and the cell in the bottom right corner is (N-1, M-1).
Output:
Print at the console the cells from column M / 2 (integer division) in the matrix. Each cell should stay on separate line. If the horse has not visited some cell, it should hold 0.
"""
from collections import deque
DIRECTIONS = [
    (1, -2), (-1, -2),
    (1, 2), (-1, 2),
    (2, 1), (2, -1),
    (-2, 1), (-2, -1)
]


def main():
    row_count = int(input())
    col_count = int(input())
    start_row, start_col = int(input()), int(input())
    board = build_board(row_count, col_count)
    ride_horse(board, start_row, start_col)
    col_to_print = col_count // 2
    print("\n".join([str(board[x][y]) for x in range(len(board)) for y in range(len(board[x])) if y == col_to_print]))


def ride_horse(board, start_row, start_col):
    """ Use BFS to go to all possible horse positions,
        keeping track of the steps we're at and adding it to the board """
    visited = set()
    positions_stack = deque([(start_row, start_col), "LEVEL UP"])
    steps = 0
    while positions_stack != deque(["LEVEL UP"]):  # if we only have the level up token in our stack, we've traversed everything
        position_tuple = positions_stack.pop()
        if position_tuple == "LEVEL UP":
            steps += 1
            positions_stack.appendleft("LEVEL UP")
            continue
        x, y = position_tuple
        visited.add(position_tuple)
        board[x][y] = steps
        # add the horse positions
        for add_x, add_y in DIRECTIONS:
            new_x = x + add_x
            new_y = y + add_y
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[new_x]) and (new_x, new_y) not in visited:
                positions_stack.appendleft((new_x, new_y))


def build_board(n, m):
    return [[0] * m for _ in range(n)]

if __name__ == '__main__':
    main()
