input_string = input("Enter a string: ")


def remove_last_character(string):
    print('Input String:', string)
    if len(string) > 1:
        string = string.strip()
        string = string[:-1]
    else:
        string = string
    print('Output String:', string)
    return string


remove_last_character(input_string)
