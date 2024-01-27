import getpass


def rot13(text):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift = 13 if char.islower() else -13
            encrypted += chr(
                (ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
        else:
            encrypted += char
    return encrypted


filepath = "D:\\The British College\\Level 4\\Semester 1\\FOCP (Fundamentals of Computer Programming)\\Task_3\\passwd.txt"


def login(username, password):
    encrypted_password = rot13(password)
    with open(filepath, "r") as file:
        for line in file:
            parts = line.split(":")
            if parts[0] == username and parts[2].strip() == encrypted_password:
                return True

    return False


if __name__ == "__main__":
    username = input("User: ")
    password = getpass.getpass("Password: ")

    # Call the login function
    if login(username, password):
        print("Access granted.")
    else:
        print("Access denied.")
