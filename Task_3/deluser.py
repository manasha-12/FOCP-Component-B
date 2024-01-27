filepath = "D:\\The British College\\Level 4\\Semester 1\\FOCP (Fundamentals of Computer Programming)\\Task_3\\passwd.txt"


def delete_user(in_username, in_filepath):
    with open(in_filepath, "r") as file:
        lines = file.readlines()

    with open(in_filepath, "w") as file:
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


if __name__ == "__main__":
    username = input("Enter username: ")

    # Call the delete_user function
    delete_user(username, filepath)
