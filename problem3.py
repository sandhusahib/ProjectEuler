def largestPrimeFactor(number):
    """Finds largest prime factor of a number (int >= 2)"""
    max_prime = 2
    for i in range(2, int((number+1)/2)):
        if number % i == 0 and i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % max_prime != 0:
            for j in range(2, i + 1):
                if j == i:
                    max_prime = i
                elif i % j == 0:
                    break
                else:
                    continue
                print(max_prime)
    return max_prime


def largestPrimeFactor2(number):
    """Finds largest prime factor of a number (int >= 2)"""
    primes = []
    for i in range(2, int((number+1)/2)):
        if number % i == 0:
            for j in range(2, i + 1):
                if j == i:
                    max_prime = i
                elif i % j == 0:
                    break
                else:
                    continue
                print(max_prime)
    return max_prime

if __name__ == "__main__":
    
    print(largestPrimeFactor(600851475143))