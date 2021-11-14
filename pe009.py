""" pe 9 - special pythagorean triplet

There exists exactly one Pythagorean triplet for which 
        a + b + c = 1000  and  a**2 + b**2 = c**2.
Find the product a*b*c.
"""

def is_pythagorean(a, b, c):
    one = a**2 + b**2 == c**2
    two = a**2 + c**2 == b**2
    three = b**2 + c**2 == a**2
    return one or two or three

a, b = 1, 1

ans = -1
for a in range(1, 1000):
    for b in range(1, 1000 - a - 1):
        c = 1000 - a - b
        assert a + b + c == 1000
        if c > 0 and is_pythagorean(a, b, c):
            ans = a * b * c
            break

print(ans)

