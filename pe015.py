""" pe 15 - power digit sum

What is the sum of the digits of the number 2^{1000}?
"""

ans = sum(int(n) for n in str(2**1000))

print(ans)