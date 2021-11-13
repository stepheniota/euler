""" pe 7 - 10001st prime

What is the 10,001st prime number?
"""
from math import sqrt

from pe003 import prime_factors


def is_prime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n_primes, answer = 0, 1
    while n_primes < 10_001:
        answer += 1
        if is_prime(answer):
            n_primes += 1

    print(answer)
