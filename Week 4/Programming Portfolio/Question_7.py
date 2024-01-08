from statistics import mean


def check_valid_temperature(in_temperature_list):
    new_temperature_list = []
    for temperature in in_temperature_list:
        if "c" in temperature:
            new_temperature = temperature.split('c')
            new_temperature_list.append(new_temperature)
        else:
            print('Enter temperature in valid format.')
    temperature_statistics(new_temperature_list)


def temperature_statistics(in_temperature_list):
    max_value = max(in_temperature_list)
    min_value = min(in_temperature_list)
    mean_value = mean(in_temperature_list)
    print(f"The Maximum Value is {max_value: .2f}")
    print(f"The Minimum Value is {min_value: .2f}")
    print(f"The Mean Value is {mean_value: .2f}")
    return None


temperature_list = []
for i in range(1, 7):
    number = input(f'Enter a number for position {i}: ').lower()
    temperature_list.append(number)

check_valid_temperature(temperature_list)
