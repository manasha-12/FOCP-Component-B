from datetime import timedelta


def read_shelter_record_file():
    # record_file = input('Enter the file path : ')
    lines = []
    try:
        with open(
                "D:\The British College\Level 4\Semester 1\FOCP (Fundamentals of Computer Programming)\Component B (60%)\shelter_2023-08-26.log",
                'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Cannot open")
    except Exception as e:
        print(f'An error occurred: {e}')
    return lines


def separate_time(read_lines):
    separated_values = []
    for line in read_lines:
        if line.strip() == 'END':
            break

        separated_values.append(line.strip().split(','))
    return separated_values


def calculate_visited_time(in_entry_time, in_exit_time, in_cat_type):
    in_total_time_in_house = 0
    in_cat_visit_durations = []
    visit_duration = in_exit_time - in_entry_time
    in_total_time_in_house += timedelta(minutes=visit_duration)
    if in_cat_type == 'OURS':
        in_cat_visit_durations.append(visit_duration)
    return in_total_time_in_house, in_cat_visit_durations


output = read_shelter_record_file()
value = separate_time(output)
print(value)

# for lines in output:
#     total_time_in_house, cat_visit_durations = calculate_visited_time(value[1], value[2], value[0])
for lines in output:
    line = lines.strip().split(',')
    if lines == 'END':
        break
    else:
        print(line[2])


