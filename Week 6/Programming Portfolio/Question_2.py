def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


integer_to_find_factors = 12
factors_list = find_factors(integer_to_find_factors)

print(f"The factors of {integer_to_find_factors} are: {factors_list}")
