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


def is_username_unique(in_username, filename="passwd.txt"):
    with open(filename, "r") as file:
        for line in file:
            parts = line.split(":")
            if parts[0] == in_username:
                return False
    return True


def add_user(in_username, in_real_name, in_password, filename="passwd.txt"):
    while not is_username_unique(in_username):
        print("Username already exists. Please enter a new username.")
        in_username = input("Enter new username: ")

    encrypted_password = rot13(in_password)
    with open(filename, "a") as file:
        file.write(f"{in_username}:{in_real_name}:{encrypted_password}\n")
    print("User Created.")


def delete_user(in_username, filename="passwd.txt"):
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        user_deleted = False
        for line in lines:
            if not line.startswith(in_username + ":"):
                file.write(line)
            else:
                user_deleted = True

        if user_deleted:
            print("User Deleted.")
        else:
            print("User not found.")


def change_password(in_username, in_current_password, in_new_password, filename="passwd.txt"):
    encrypted_current_password = rot13(in_current_password)
    encrypted_new_password = rot13(in_new_password)

    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        password_changed = False
        for line in lines:
            parts = line.split(":")
            stored_username = parts[0].strip()
            stored_password = parts[2].strip()
            if stored_username == in_username and stored_password == encrypted_current_password:
                file.write(f"{parts[0]}:{parts[1]}:{encrypted_new_password}\n")
                password_changed = True
            else:
                file.write(line)

        if password_changed:
            print("Password changed.")
        else:
            print("Invalid username or password.")


def login(in_username, in_password, filename="passwd.txt"):
    encrypted_password = rot13(in_password)
    with open(filename, "r") as file:
        for line in file:
            parts = line.split(":")
            if parts[0] == in_username and parts[2].strip() == encrypted_password:
                return True

    return False


if __name__ == "__main__":
    command = input("Enter command (adduser, deluser, passwd, login): ")

    if command == "adduser":
        username = input("Enter new username: ")
        while not is_username_unique(username):
            print("Username already exists. Please enter a new username.")
            username = input("Enter new username: ")

        real_name = input("Enter real name: ")
        password = input("Enter password: ")
        add_user(username, real_name, password)

    elif command == "deluser":
        username = input("Enter username: ")
        delete_user(username)

    elif command == "passwd":
        username = input("User: ")
        current_password = input("Current Password: ")
        new_password = input("New Password: ")
        confirm_password = input("Confirm: ")

        if new_password == confirm_password:
            change_password(username, current_password, new_password)
        else:
            print("Passwords do not match.")

    elif command == "login":
        username = input("User: ")
        password = input("Password: ")

        if login(username, password):
            print("Access granted.")
        else:
            print("Access denied.")

    else:
        print("Invalid command.")
