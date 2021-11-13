""" pe 7 - 10001st prime

What is the 10,001st prime number?
"""
from math import sqrt
from helper import is_prime


n_primes, answer = 0, 1
while n_primes < 10_001:
    answer += 1
    if is_prime(answer):
        n_primes += 1

print(answer)
