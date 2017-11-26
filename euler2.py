"""
Project Euler - Problem #2
https://projecteuler.net/problem=2
"""
def even_fib_sum():
    """
    Sums all even Fibonacci terms less than 4,000,000
    """
    total = 2
    first_fib = 1
    second_fib = 2
    next_fib = first_fib + second_fib
    while next_fib < 4000000:
        first_fib = second_fib
        second_fib = next_fib
        next_fib = first_fib + second_fib
        if next_fib % 2 == 0:
            total += next_fib
    print(str(total))

even_fib_sum()
