def karatsuba_mult(n1, n2):
    """
    :param n1: The first positive number
    :param n2: The second positive number
    :return: The multiplication of n1 and n2

    """
    # The base case of recursive function
    if n1 < 10 or n2 < 10:
        return n1 * n2

    # We first split the numbers almost from the middle (of the smallest number)
    min_digits = min(num_digits(n1), num_digits(n2))
    d = int(min_digits / 2)
    left1, right1 = split_digits(n1, d)
    left2, right2 = split_digits(n2, d)

    # Now we can recursively compute the multiplication
    x1 = karatsuba_mult(left1, left2)
    x2 = karatsuba_mult(left1 + right1, left2 + right2)
    x3 = karatsuba_mult(right1, right2)
    return x1 * 10 ** (d * 2) + (x2 - x1 - x3) * 10 ** d + x3


def num_digits(n):
    """
    Returns the number of digits of the argument
    """
    if n >= 0:
        return len(str(n))
    else:
        return len(str(-n))


def split_digits(n, d):
    """
    :param n: The positive number to be split
    :param d: The number of digits in the right part
    :return: The left and right parts of the original number
    Splits the number n into two smaller numbers such that "right" is the first d digits of n from right and
    "left" is the remaining digits
    """
    left = int(n / 10 ** d)
    right = n % 10 ** d
    return left, right


n1 = 190412
n2 = 5678
# Testing Karatsuba multiplication
print(karatsuba_mult(n1, n2))
print(n1*n2)
