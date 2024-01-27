import getpass

filepath = "D:\\The British College\\Level 4\\Semester 1\\FOCP (Fundamentals of Computer Programming)\\Task_3\\passwd.txt"


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


def is_username_unique(in_username, in_filepath):
    with open(in_filepath, "r") as file:
        for line in file:
            parts = line.split(":")
            if parts[0] == in_username:
                return False
    return True


def add_user(in_username, in_real_name, in_password, in_filepath):
    while not is_username_unique(in_username, filepath):
        print("Username already exists. Please enter a new username.")
        in_username = input("Enter new username: ")

    encrypted_password = rot13(in_password)
    with open(in_filepath, "a") as file:
        file.write(f"{in_username}:{in_real_name}:{encrypted_password}\n")
    print("User Created.")


if __name__ == "__main__":
    username = input("Enter new username: ")
    real_name = input("Enter real name: ")
    password = getpass.getpass("Enter password: ")

    # Call the add_user function
    add_user(username, real_name, password, filepath)
