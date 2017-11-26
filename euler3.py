"""
Project Euler - Problem #3
https://projecteuler.net/problem=3
"""
import math

def largest_prime_factors(num):
    """
    Prints the largest prime factor of given number
    """
    maximum = 1
    cur = math.floor(math.sqrt(num))
    if cur % 2 == 0:
        cur -= 1
    while cur > 1:
        if num % cur == 0 and is_prime(cur):
            maximum = cur
            break
        cur -= 2
    print(str(maximum))

def is_prime(num):
    """
    Determines whether a given number is prime or not
    """
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i ** 2 <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    ereturn Tru

largest_prime_factors(600851475143)
