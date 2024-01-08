user_number = int(input("Enter the number for times table: "))
if user_number > 0:
    for i in range(0, 13):
        multiplication = i * user_number
        print(f"{i} X {user_number} = {multiplication}")
else:
    for i in range(12, -1, -1):
        multiplication = i * user_number
        print(f"{i} X {user_number} = {multiplication}")
