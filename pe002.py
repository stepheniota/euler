""" project euler 0002 - even fibonacci numbers

By considering the terms in the Fibonacci sequence whose 
values do not exceed four million, 
find the sum of the even-valued terms.
"""

fib, prev, curr = [], 1, 2
while curr <= 4_000_000:
    if curr % 2 == 0: 
        fib.append(curr)
    curr, prev = prev + curr, curr

ans = sum(fib)
print(ans)
