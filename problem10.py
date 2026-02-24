def findPrimes(limit):
    """Creates a list of all primes below limit"""
    primes = [2]
    i = 2
    while i < limit:
        for p in primes:
            if i % p == 0:
                break
            elif p == primes[-1]:
                primes.append(i)
        i += 1
    return primes

if __name__ == "__main__":
    print(sum(findPrimes(2000000)))