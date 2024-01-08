BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while True:
    password = input("Enter password: ")
    if password in BAD_PASSWORDS:
        print("You cannot have this password!")
        continue
    else:
        if (len(password) >= 8) and (len(password) <= 12):
            password_check = input("Confirm Password: ")
            if password == password_check:
                print("Password Set!")
                break
            else:
                print("Sorry! Wrong password. Please try again")
                continue
        else:
            print("Invalid password length. You entered less than 8 characters or more than 12 characters")
            continue
