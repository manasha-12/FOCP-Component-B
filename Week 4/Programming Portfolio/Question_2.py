def count_upper_lower(user_string):
    lowercase_letter_counter = 0
    uppercase_letter_counter = 0

    for letter in user_string:
        if letter.isupper():
            uppercase_letter_counter += 1
        elif letter.islower():
            lowercase_letter_counter += 1

    print('Upper Case Letters :',uppercase_letter_counter, 'Lower Case Letters :', lowercase_letter_counter)


count_upper_lower("HelloWorld")
