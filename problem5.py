def evenlyDivisible(limit):
    """Finds the smallest number that can be divided by each integer from 1 
    to the limit, without leaving a remainder in any case (evenly divisible
    in all cases)"""
    dividend = limit
    while dividend >= limit:
        for i in range(1, limit+1):
            if dividend % i != 0:
                dividend += 1
                break
            elif i == limit:
                return dividend
            


if __name__ == "__main__":
    
    print(evenlyDivisible(20))