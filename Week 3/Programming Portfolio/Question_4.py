BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
password = input("Enter password: ")
if password in BAD_PASSWORDS:
    print("You cannot have this password!")
else:
    if (len(password) >= 8) and (len(password) <= 12):
        password_check = input("Confirm Password: ")
        if password == password_check:
            print("Password Set!")
        else:
            print("Sorry! Wrong password. Please try again")
    else:
        print("Invalid password length. You entered less than 8 characters or more than 12 characters")
