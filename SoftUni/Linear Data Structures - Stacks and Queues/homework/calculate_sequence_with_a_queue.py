"""
We are given the following sequence of numbers:
S1 = N
S2 = S1 + 1
S3 = 2*S1 + 1
S4 = S1 + 2
S5 = S2 + 1
S6 = 2*S2 + 1
S7 = S2 + 2
…
Using the Queue<T> class, write a program to print its first 50 members for given N. Examples:

2
2, 3, 5, 4, 4, 7, 5, 6, 11, 7, 5, 9, 6, …

-1
-1, 0, -1, 1, 1, 1, 2, …

1000
1000, 1001, 2001, 1002, 1002, 2003, 1003, …
"""
from collections import deque


REQUIRED_COUNT = 50  # first 50 members
current_count = 1
queue = deque()
queue.append(int(input()))
members = []

# calculates enough members to reach REQUIRED_COUNT
for _ in range((REQUIRED_COUNT//3) + 1):
    element = queue.popleft()
    members.append(element)
    queue.append(element + 1)
    queue.append(element * 2 + 1)
    queue.append(element + 2)
# adds what's left of the member from our queue
while len(members) < 50:
    members.append(queue.popleft())

print(len(members))
