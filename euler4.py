"""
Project Euler - Problem #4
https://projecteuler.net/problem=4
"""
def find_largest_palindrome(num):
    """
    Finds the largest palindrome obtained from multiplying 2 numbers with 'num' digits
    """
    maximum = 1
    upper = int(num * str(9))
    lower = int("1" + (num - 1) * "0")
    for i in range(upper, lower, -1):
        for j in range(i, lower, -1):
            mult = i * j
            if is_palindrome(mult) and mult > maximum:
                maximum = mult
    print(str(maximum))

def is_palindrome(num):
    """
    Determines if a given number is a palindrome (e.g. 9009) or not
    """
    numstr = str(num)
    for i in range(len(numstr) // 2):
        if numstr[i] != numstr[len(numstr) - 1 - i]:
            return False
    return True

find_largest_palindrome(3)
