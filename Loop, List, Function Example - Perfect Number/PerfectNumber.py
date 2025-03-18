# take an integer from user
# print all its proper divisors
# tell if the number is perfect, abundant, or deficient

def proper_divisors(m):
    divisors = []
    for i in range(1, m):
        if m % i == 0:
            divisors.append(i)
    return divisors


def classify(n, divisors):
    #     return either perfect, abundant, or deficient

    # manually:
    # sum_divisors = 0
    # for i in range(len(divisors)):
    #     sum_divisors = sum_divisors + divisors[i]

    # easier way:
    sum_divisors = sum(divisors)

    if sum_divisors == n:
        return "perfect", sum_divisors
    elif sum_divisors < n:
        return "abundant", sum_divisors
    else:
        return "deficient", sum_divisors



if __name__ == "__main__":
    n = int(input("enter a positive integer (n): "))

    proper_divisors_of_n = proper_divisors(n)

    print(f"proper divisors of {n}:", proper_divisors_of_n)

    n_type, sum_of_divisors = classify(n, proper_divisors_of_n)

    print(f"sum of the proper divisors of {n}: {sum_of_divisors}")
    print(f"{n} is {n_type}!")
