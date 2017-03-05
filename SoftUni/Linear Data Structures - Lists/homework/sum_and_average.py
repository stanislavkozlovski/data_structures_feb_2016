"""
Write a program that reads from the console a sequence of integer numbers (on a single line, separated by a space).
Calculate and print the sum and average of the elements of the sequence. Keep the sequence in List<int>.
"""
sequence = [int(num) for num in input().split()]
seq_sum = sum(sequence)
print("Sum={sum}; Average={avg}".format(
    sum=seq_sum, avg=seq_sum/len(sequence)
))
"""
Input
Output
4 5 6
Sum=15; Average=5

1 1
Sum=1; Average=1

0
Sum=0; Average=0

10
Sum=10; Average=10

2 2 1
Sum=5; Average=1.66666666666667
"""