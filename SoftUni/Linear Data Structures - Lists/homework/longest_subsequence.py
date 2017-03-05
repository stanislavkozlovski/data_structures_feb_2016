"""
Write a method that finds the longest subsequence of equal numbers in given List<int> and returns the result as new List<int>.
If several sequences has the same longest length, return the leftmost of them. Write a program to test whether the method works correctly.
"""
last_num = None
max_num = None
max_count = 0
current_count = 0
for dig in [int(dig) for dig in input().split()]:
    #  current_count = 1 if dig != last_num else current_count + 1
    if dig == last_num:
        current_count += 1
    else:
        current_count = 1
    if current_count > max_count:
        max_count = current_count
        max_num = dig

    last_num = dig

print(' '.join([str(max_num)] * max_count))

"""
12 2 7 4 3 3 8
3 3

2 2 2 3 3 3
2 2 2

4 4 5 5 5
5 5 5

1 2 3
1

0
0

"""