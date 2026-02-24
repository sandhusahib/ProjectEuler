"""Find the last 10 digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000"""

sum_of_powers = 0
for i in range(1, 1001):
    sum_of_powers += i**i

print(str(sum_of_powers)[-10:])