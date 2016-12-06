"""
Write a program that removes from given sequence all numbers that occur odd number of times.
"""
from collections import Counter


orig_list = input().split()
for item, count in Counter(orig_list).items():
    if count % 2 != 0:
        orig_list = [number for number in orig_list if number != item]

print(' '.join(orig_list))

"""
1 2 3 4 1
1 1
2, 3 and 4 occur odd number of times (once). 1 occurs 2 times

1 2 3 4 5 3 6 7 6 7 6
3 3 7 7
1, 2, 4, 5 and 6 occurs odd number of times  removed

1 2 1 2 1 2

All numbers occur odd number of times  removed

3 7 3 3 4 3 4 3 7
7 4 4 7
3 occurs odd number of times (5)  removed

1 1
1 1
All numbers occur even number of times  sequence stays unchanged
"""