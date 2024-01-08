number_of_sweets = int(input("Enter number of sweets: "))
number_of_pupils = int(input("Enter number of pupils attending: "))
number_of_sweet_per_person = number_of_sweets // number_of_pupils
number_of_left_over = number_of_sweets % number_of_pupils
print(f"Sweet per person to be distributed : {number_of_sweet_per_person}, left over sweets : {number_of_left_over}" )
