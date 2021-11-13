""" pe 14 - longest collatz sequence

The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)


Which starting number, under one million, produces the longest chain?
"""

def collatz(n):
    assert n > 0
    if n % 2 == 0:
        return n/2
    return 3*n + 1

def solve():
    max_len, longest = 0, None
    # cache results to break out of collatz when seen seq repeats
    seen = {1: 1} 

    for num in range(2, 1_000_000):
        n, cur_len = num, 0
        while n not in seen:
            n = collatz(n)
            cur_len += 1
        seen[num] = cur_len + seen[n]
        if seen[num] > max_len:
            max_len, longest = seen[num], num
    return longest

if __name__ == '__main__':
    answer = solve()
    print(answer)
