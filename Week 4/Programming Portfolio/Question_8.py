from statistics import mean


def calculation():
    number_list = []
    while True:
        user_input = str(input("Enter numbers or press enter to end: "))
        number_list.append(user_input)
        if user_input == "":
            break
        else:
            continue
    number_list[-1:] = []
    new_list = [int(i) for i in number_list]

    max_value = max(new_list)
    min_value = min(new_list)
    mean_value = mean(new_list)
    print(f"The maximum value is {max_value: .1f}")
    print(f"The minimum value is {min_value: .1f}")
    print(f"The mean value is {mean_value: .1f}")
    return None


calculation()
