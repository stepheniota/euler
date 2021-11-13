""" project euler 4  - largest palindrome product

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n):
    """ Test whether some integer n reads the same both ways. """
    n = str(n)
    return n == n[::-1]

if __name__ == '__main__':
    largest_palindrome, min_val, max_val = 0, 100, 999
    for n1 in range(max_val, min_val - 1, -1):
        for n2 in range(max_val, min_val - 1, -1):
            candidate = n1 * n2
            if candidate < largest_palindrome:
                break
            elif is_palindrome(candidate):
                largest_palindrome = candidate

    print(largest_palindrome)