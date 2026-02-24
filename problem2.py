def sumEvenFibonacci(limit):
    """Finds the sum of all even Fibonacci numbers below the limit"""
    f1, f2 = 1, 2
    sum = 0
    
    while f1 < limit:
        f3 = f1
        f1 = f2
        f2 = f2 + f3
        if f1 % 2 == 0:
            sum += f1
    
    return sum

if __name__ == "__main__":
    print(sumEvenFibonacci(4 * 10**6))