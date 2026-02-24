def sumSquareDifference(n):
    """Finds the difference between the sum of squares and the square of
    the sum of the first n natural numbers"""
    integers = [i for i in range(1, n+1)]
    squares = [i**2 for i in integers]

    sum_of_squares = sum(squares)
    square_of_sum = sum(integers) ** 2

    difference = square_of_sum - sum_of_squares

    return difference


if __name__ == "__main__":
    print(sumSquareDifference(100))