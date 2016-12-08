"""
We are given numbers n and m, and the following operations:

n  n + 1
n  n + 2
n  n * 2

3 10
3 -> 5 -> 10

5 -5
(no solution)

10 30
10 -> 12 -> 14 -> 28 -> 30

Write a program that finds the shortest sequence of operations from the list above that starts from n and finishes in m. If several shortest sequences exist, find one of them. Examples:
"""
import sys
from collections import deque

n, m = [int(num) for num in input().split()]
queue = deque()
solution = []
if m < n:
    print("(no solution)")
    sys.exit()

queue.append(m)
while queue:
    number = queue.popleft()
    solution.append(number)
    if number == n:
        break

    if number % 2 == 0:
        divided_num = number / 2
        if divided_num >= n:
            queue.append(divided_num)
            continue
    else:
        # number is odd
        # check if there is a point to divide the number below ours and if so, decrement by 1 so as to
        # divide on the next iteration
        if (number - 1 / 2) >= n and number-2 != n:
            queue.append(number-1)
            continue

    minus_two_num = number - 2
    if minus_two_num >= n:
        queue.append(minus_two_num)
    else:
        queue.append(number-1)

solution = list(reversed(solution))
print(solution)
