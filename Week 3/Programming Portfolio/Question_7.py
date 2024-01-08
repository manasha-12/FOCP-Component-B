user_number = int(input("Enter the number for times table: "))
for i in range(0, 13):
    multiplication = i * user_number
    print(f"{i} X {user_number} = {multiplication}")
