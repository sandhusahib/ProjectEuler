def sumMultiples_3_or_5(limit):
    """Finds the sum of all multiples of 3 or 5 below limit (int)
        e.g. if limit = 10; 3 + 5 + 6 + 9 = 23"""
    
    sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum

if __name__ == "__main__":
    
    print(sumMultiples_3_or_5(1000))