"""sum of digits of number 2^1000"""

digit_string_list = list(str(2**1000))
digits = [int(i) for i in digit_string_list]

sum_of_digits = sum(digits)
print(sum_of_digits)