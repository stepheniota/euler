""" pe 25 - 1000-digit fibonacci number

What is the index of the first term 
in the Fibonacci sequence to contain 1000 digits?
"""

def num_digits(n):
    return len(str(n))

def solve(n_digits=1000):
    old, prev = 1, 1  # boundary conditions
    ans = 3  # pe wants 1 indexed solution
    while True:
        fib = old + prev
        old, prev = prev, fib
        if num_digits(fib) == n_digits:
            return ans
        ans += 1

ans = solve(1000)

print(ans)
