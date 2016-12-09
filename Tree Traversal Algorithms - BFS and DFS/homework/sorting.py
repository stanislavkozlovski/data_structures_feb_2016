"""
You are given a list with numbers, holding a random permutation of the integers from 1 to N, inclusive.
At each step, it is allowed to make only one operation of the following type: take K consecutive elements from the list
 and reverse their order (e.g. if we have the numbers 1, 8, 3, 6, after their reversal they became in order 6, 3, 8, 1).
The list should be sorted in increasing order (1, 2, 3, …, N).
By given N, K and a list of numbers, find the smallest number of steps (operations) needed to sort the numbers in ascending order.
If this is impossible, print -1.

Input:-
The first line holds the number N – count of the numbers.
The second line holds the shuffled numbers (separated one from another by a space).
The third line holds the number K – number of consecutive elements.

Output
Print at the console the smallest number of operations, needed to sort the numbers in increasing order.
"""
number_count = int(input())
numbers = [int(num) for num in input().split()]
reverse_count = int(input())
operations = 0
has_reversed = True

""" Algorithm is the following:
    Go through each number and try to see if the number {REVERSE_COUNT} indexes away from him is smaller.
    If it's smaller then we obviously need to sort that part and we reverse that part exactly.
    Continue to do this until we go through a whole iteration of the list without reversing anything.
    This means that either the list cannot be sorted in this way or that it's already sorted."""
while has_reversed:
    has_reversed = False
    for idx, num in enumerate(numbers):
        idx_to_reverse = (idx + reverse_count) - 1
        if idx_to_reverse >= len(numbers):
            break
        else:
            if num > numbers[idx_to_reverse]:  # Reverse!
                numbers = numbers[:idx] + list(reversed(numbers[idx:idx_to_reverse+1])) + numbers[idx_to_reverse+1:]
                operations += 1
                has_reversed = True

# check if it's sorted
if list(sorted(numbers)) == numbers:
    print(operations)
else:
    print(-1)
