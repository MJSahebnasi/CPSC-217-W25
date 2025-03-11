# implementation 1:
# 983 // 10 = 98
# 983 // 100 = 9
# 983 // 1000 = 0

# implementation 2:
# 983 // 10 = 98
# 98 // 10 = 9
# 9 // 10 = 0

def print_digits_count(n):
    """
    Prints the number of digits of the input number
    :param n: input, integer
    :return: nothing
    """
    copy_of_n = n
    digits_count = 0
    while n != 0:
        n = n // 10
        digits_count += 1  # same as: digits_count = digits_count + 1
    print(f"{copy_of_n} has {digits_count} digits.")
    # 10 has 2 digits


def digits_count(n):
    """
    Returns the number of digits of the input number
    :param n: input, integer
    :return: number of digits, integer
    """
    digits_count = 0
    while n != 0:
        n = n // 10
        digits_count += 1  # same as: digits_count = digits_count + 1
    return digits_count


def print_digits_count_debugged(n):
    """
    Prints the number of digits of the input number
    :param n: input, integer
    :return: nothing
    """
    copy_of_n = n
    n = abs(n)
    digits_count = 0
    while n > 0:
        n = n // 10
        digits_count += 1  # same as: digits_count = digits_count + 1
    print(f"{copy_of_n} has {digits_count} digits.")
    # 10 has 2 digits


def max_of_3(a, b, c):
    """
    returns the max of 3 input
    :param a: int
    :param b: int
    :param c: int
    :return: int, max of 3 input
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# print_digits_count(4)
# print_digits_count(14)
# print_digits_count(901)
# print_digits_count(1001)

# digits_count_of_12 = digits_count(12)
# print(f"12 has {digits_count_of_12} digits.")
#
# m = digits_count(1200)
# print(f"1200 has {m} digits.")

# print_digits_count_debugged(-10)
# print_digits_count_debugged(-1)

print(max_of_3(10, 1, 10))
