# Write a program to compare the execution speed of the functions IsPrime(p) and IsPrimeFast(p)
from math import sqrt
from datetime import datetime


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def is_prime_faster(n):
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False

    return True


for p in [1000, 10000, 50000, 100000, 1000000]:
    start = datetime.now()

    for i in range(p+1):
        is_prime(i)

    end = datetime.now()
    print('IsPrime for {p} numbers is {time}'.format(p=p, time=end - start))

    start = datetime.now()

    for i in range(p+1):
        is_prime_faster(i)

    end = datetime.now()
    print('IsPrimeFaster for {p} numbers is {time}'.format(p=p, time=end - start))
