""" helper functions. """
from math import sqrt


def is_prime(n: int) -> bool:
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


def sieve_of_Eratosthenes(n: int) -> list[int]:
    """ Return all primes not greater than input n.

    ref ~ https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    assert n > 1

    A = [True] * (n + 1)  # index i represents int i in [0, n]
    A[0] = A[1] = False   # boundary conditions

    for i in range(2, int(sqrt(n) + 1)):
        if A[i]:
            for j in range(i**2, n, i):
                A[j] = False
    return [i for i in range(n - 2) if A[i]]


def prime_factors(n: int) -> list[int]:
    """ Constructs a list of the prime factorization of n.

    Note that each prime factor appears in the output list
    as many times as it divides the number.

    ref ~ Laaksonen, CP Handbook (2019), pg 199.
    """
    factors = []
    for i in range(2, int(sqrt(n) + 1)):
        while n % i == 0:
            factors.append(i)
            n /= i
            
    # occurs if input n is prime
    if n > 1:  
        factors.append(n)

    return factors
