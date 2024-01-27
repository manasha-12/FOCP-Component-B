def integer_to_binary(number_in_decimal):
    if number_in_decimal < 0:
        raise ValueError("Input must be a positive integer.")
    return bin(number_in_decimal)[2:]


positive_integer = 42
binary_representation = integer_to_binary(positive_integer)

print(f"The binary representation of {positive_integer} is: {binary_representation}")
