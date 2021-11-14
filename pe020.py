""" pe 20 - factorial digit sum

Find the sum of the digits in the number 100!
"""
from math import factorial

digits = str(factorial(100))
ans = sum([int(i) for i in digits])

print(ans)