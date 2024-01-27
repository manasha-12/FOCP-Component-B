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


def change_password(in_username, in_current_password, in_new_password, in_filepath):
    encrypted_current_password = rot13(in_current_password)
    encrypted_new_password = rot13(in_new_password)

    with open(in_filepath, "r") as file:
        lines = file.readlines()

    with open(in_filepath, "w") as file:
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


if __name__ == "__main__":
    username = input("Enter username: ")
    current_password = getpass.getpass("Current Password: ")
    new_password = input("New Password: ")

    # Call the change_password function
    change_password(username, current_password, new_password, filepath)
