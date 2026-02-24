"""Finds the largest palindrome made from the product of two 3-digit numbers."""
palindromes = []
factors = []
for i in range(999,0,-1):
    for j in range(999,0,-1):
        product = i * j
        product_string = str(product)
        reversed_product = "".join([product_string[i] for i in range(len(product_string)-1, -1, -1)])
        if product_string == reversed_product:
            palindromes.append(int(product_string))
            factors.append((i,j))

max_palindrome = max(palindromes)
max_index = palindromes.index(max_palindrome)
max_factors = factors[max_index]

print("index: ", max_index)
print("factors: ", max_factors)
print("palindrome: ", max_palindrome)    