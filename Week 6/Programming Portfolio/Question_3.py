def is_prime(number_to_check):
    if number_to_check <= 1:
        return False
    elif number_to_check == 2:
        return True
    elif number_to_check % 2 == 0:
        return False
    else:
        for i in range(3, int(number_to_check ** 0.5) + 1, 2):
            if number_to_check % i == 0:
                return False
        return True


test_case_number = 17
result = is_prime(test_case_number)

if result:
    print(f"{test_case_number} is a prime number.")
else:
    print(f"{test_case_number} is not a prime number.")
