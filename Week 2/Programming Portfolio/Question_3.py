number_of_students = int(input("How many students? "))
group_size = int(input("Required group size? "))

number_of_groups = number_of_students // group_size
left_over_students = number_of_students % group_size

if number_of_groups == 1 and left_over_students == 0:
    print(f"There is 1 group with 0 students left over.")
elif number_of_groups == 1:
    print(f"There is 1 group with {left_over_students} student{'s' if left_over_students > 1 else ''} left over.")
elif left_over_students == 0:
    print(f"There are {number_of_groups} groups with 0 students left over.")
else:
    print(f"There are {number_of_groups} groups with {left_over_students} student{'s' if left_over_students > 1 else ''} left over.")