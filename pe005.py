""" pe 5 - smallest multiple

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?

Idea: find the prime factors of ints 1 to 20.
      Choose the smallest subset of those factors needed to
      reconstruct ints 1 to 20.
"""
from collections import Counter
from math import sqrt, prod, floor

from pe003 import prime_factors


divisors = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
#divisors = list(range(1, 11))

meta = {}
for n in divisors:
    factors = Counter(prime_factors(n))
    for f, cnt in factors.items():
        if f not in meta or meta[f] < cnt:
            meta[f] = cnt

answer = 1
for val, cnt in meta.items():
    answer *= val**cnt

answer = int(answer)
print(f'{answer=}')
