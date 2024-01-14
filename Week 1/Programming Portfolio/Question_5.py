number_of_students_per_group = 24
number_of_total_students = [113, 175, 12]
for students in number_of_total_students:
    no_of_group = students // number_of_students_per_group
    no_of_left_out = students - (no_of_group * 24)
    print("Number of Groups with 24 Students each: ", no_of_group)
    print("Number of Left Out Students: ", no_of_left_out)

