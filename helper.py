""" helper functions. """
from math import sqrt

def is_prime(n):
    """ return true in n is prime else false. """
    assert n > 0
    if n == 2: 
        return True
    elif n == 1 or n % 2 == 0: 
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0: 
            return False
    return True
