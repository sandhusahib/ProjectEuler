def findPrime(n):
    """Finds the n-th prime number"""
    primes = [2]
    i = 2
    while len(primes) < n:
        for p in primes:
            if i % p == 0:
                break
            elif p == primes[-1]:
                primes.append(i)
        i += 1

    return primes[-1]

if __name__ == "__main__":
    print(findPrime(10001))