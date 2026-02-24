"""Finds the (unique) Pythagorean triplet a^2 + b^2 = c^2
    for which a + b + c = 1000"""

for a in range(500):
    for b in range(1, 500):
        c_squared = a**2 + b**2
        c = int(c_squared**(1/2))
        if c == c_squared**(1/2):
            if a + b + c == 1000:
                prod = a * b * c
                print("a = ", a)
                print("b = ", b)
                print("c = ", c)
                print("abc = ", prod)
            else:
                continue
        else:
            continue
