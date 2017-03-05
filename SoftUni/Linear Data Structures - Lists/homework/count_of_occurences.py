"""
Write a program that finds in given array of integers how many times each of them occurs.
The input sequence holds numbers in range [0…1000].
The output should hold all numbers that occur at least once along with their number of occurrences.
"""
# sure I could not use this and use a dictionary, or even worse iterate for each number, counting it, but why
from collections import Counter


for number, count in Counter(input().split()).items():
    print("{num} -> {times} times".format(num=number, times=count))

"""
3 4 4 2 3 3 4 3 2
2 -> 2 times
3 -> 4 times
4 -> 3 times

1000
1000 -> 1 times

0 0 0
0 -> 3 times


7 6 5 5 6
5 -> 2 times
6 -> 2 times
7 -> 1 times
"""