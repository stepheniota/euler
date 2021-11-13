""" pe 6 - sum square difference

Find the difference between 
the sum of the squares of the first one hundred natural numbers and 
the square of the sum.
"""
import numpy as np

nums = np.arange(1, 101)
answer = np.square(np.sum(nums)) - np.sum(np.square(nums))

print(f'{answer=}')
