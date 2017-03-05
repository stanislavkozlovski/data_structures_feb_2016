"""
Write a program that reads N integers from the console and reverses them using a stack. Use the Stack<int> class from .NET Framework.
Just put the input numbers in the stack and pop them. Examples:



1 2 3 4 5
5 4 3 2 1

1
1

(empty)
(empty)

1 -2
-2 1
"""
from collections import deque


stack = deque()
reversed_numbers = []
# fill the stack
for number in input().split():
    stack.append(number)
# get the elements from the stack
while stack:
    reversed_numbers.append(stack.pop())
print(' '.join(reversed_numbers))