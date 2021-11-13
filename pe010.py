""" pe 10 - summation of primes

Find the sum of all the primes below two million.
"""

import numpy as np

from helper import is_prime

candidates = range(3, 2_000_000, 2)
answer = 2 + sum(filter(is_prime, candidates))

print(answer)



