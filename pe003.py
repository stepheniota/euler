""" project euler 0003 - largest prime factor

What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt

def prime_factors(n):
    """ Constructs a list of the prime factorization of n.

    Note that each prime factor appears in the output list
    as many times as it divides the number.

    ref ~ Laaksonen, CP Handbook (2019), pg 199.
    """
    f = []
    for i in range(2, int(sqrt(n) + 1)):
        while n % i == 0:
            f.append(i)
            n /= i
            
    if n > 1: f.append(n)

    return f

if __name__ == '__main__':
    subject = 600_851_475_143

    largest_prime_factor = prime_factors(subject)[-1]
    print(largest_prime_factor)
