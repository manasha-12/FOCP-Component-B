def take_user_name():
    name = input("Enter your name: ")
    convert_to_uppercase(name)


def convert_to_uppercase(in_user_name):
    if in_user_name:
        user_name = in_user_name[0].upper() + in_user_name[1:].lower()
        print(f"Hello {user_name}. Good to meet you!")
    else:
        print("Hello Stranger!")


take_user_name()