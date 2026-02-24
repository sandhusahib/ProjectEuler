"""Finds sum of all numbers less than 1 million, which are
    palindromic in both base 10 and base 2.
    e.g. 585 (decimal) == 1001001001 (binary)"""

sum_of_palindromes = 0
count = 0
for i in range(10**6):
    string = str(i)
    rev_string = string[::-1]
    if string == rev_string:
        binary_string = bin(i)[2:]
        rev_binary_string = binary_string[::-1]
        if binary_string == rev_binary_string:
            sum_of_palindromes += i
            count += 1
        else:
            continue
    else:
        continue

print("Sum of Palindromes: ", sum_of_palindromes)
print("Number of Palindromes: ", count)