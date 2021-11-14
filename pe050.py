""" pe 50 - consecutive prime sum

Which prime, below one-million, can be written as 
the sum of the most consecutive primes?
"""
import numpy as np

from helper import is_prime

def prime(n): 
    return n if is_prime(n) else 2

is_prime_vec = np.vectorize(prime)

limit = 1_000_000
primes = set(is_prime_vec(np.arange(2, limit + 1)))
primes_list = sorted(list(primes))

max_len, ans = 0, None
for i in range(len(primes_list)):
    for j in range(i, -1, -1):
        cur_sum = sum(primes_list[j:i + 1])
        if cur_sum > limit:
            break
        cur_len = i - j + 1
        if cur_sum in primes and cur_len > max_len:
            max_len, ans = cur_len, cur_sum

print(f'{max_len=}, {ans=}')


