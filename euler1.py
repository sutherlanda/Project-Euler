"""
Project Euler - Problem #1
https://projecteuler.net/problem=1
"""
def mul_sum():
    """
    Sums multiples of 3 and 5 between 1 and 1000
    """
    total = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    print(str(total))

mul_sum()
