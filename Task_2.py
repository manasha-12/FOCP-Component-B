import sys
from datetime import timedelta


def read_shelter_record_file():
    # record_file = input('Enter the file path : ')
    lines = []
    try:
        with open("D:\The British College\Level 4\Semester 1\FOCP (Fundamentals of Computer Programming)\Component B (60%)\shelter_2023-08-26.log", 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Cannot open")
    except Exception as e:
        print(f'An error occurred: {e}')
    return lines


def separate_time(read_lines):
    separated_values = []
    for in_line in read_lines:
        if in_line.strip() == 'END':
            break

        separated_values.append(in_line.strip().split(','))
    return separated_values


def calculate_visited_time(in_entry_time, in_exit_time, in_cat_type):
    in_total_time_in_house = 0
    in_cat_visit_durations = []
    visit_duration = in_exit_time - in_entry_time
    in_total_time_in_house += timedelta(minutes=visit_duration)
    if in_cat_type == 'OURS':
        in_cat_visit_durations.append(visit_duration)
    return in_total_time_in_house, in_cat_visit_durations


def count_cat_entry(in_cat_type):
    in_cat_visits = 0
    in_intruder_cat_visits = 0
    if in_cat_type == 'OURS':
        in_cat_visits += 1
    elif in_cat_type == 'THEIRS':
        in_intruder_cat_visits += 1
    return in_cat_visits, in_intruder_cat_visits


def statistical_overview(in_cat_visits, in_cat_visit_durations):
    if in_cat_visits == 0:
        in_average_visit_length = in_longest_visit = in_shortest_visit = 0
    else:
        in_average_visit_length = sum(in_cat_visit_durations) / in_cat_visits
        in_longest_visit = max(in_cat_visit_durations)
        in_shortest_visit = min(in_cat_visit_durations)
    return in_average_visit_length, in_longest_visit, in_shortest_visit


def output_for_cat_shelter(in_cat_visits, in_intruder_cat_visits, in_total_time_in_house, in_average_visit_length,
                           in_longest_visit,
                           in_shortest_visit):
    print(f"""Log File Analysis"
    ========================
    Cat Visits: {in_cat_visits}")
    Other Cats: {in_intruder_cat_visits}\n")
    Total Time in House: {str(in_total_time_in_house)}\n")
    Average Visit Length: {int(in_average_visit_length)} Minutes")
    Longest Visit: {in_longest_visit} Minutes")
    Shortest Visit: {in_shortest_visit} Minutes\n""")


# calling the functions
read_line = read_shelter_record_file()
record_list = separate_time(read_line)

for lines in read_line:
    # total_time_in_house, cat_visit_durations = calculate_visited_time(line[1], line[2],
    #                                                                       record_list[i][0])
    if len(lines) >= 3:
        line = lines.strip().split(',')
        if lines == 'END':
            break
        else:
            total_time_in_house, cat_visit_durations = calculate_visited_time(line[1], line[2], line[0])

cat_visits = []
for lines in read_line:
    i = 0
    if lines == 'END':
        break
    cat_visits, intruder_cat_visits = count_cat_entry(record_list[i][0])
    i += 1

average_visit_length, longest_visit, shortest_visit = statistical_overview(cat_visits, cat_visit_durations)

# final output function
output_for_cat_shelter(cat_visits, intruder_cat_visits, total_time_in_house, average_visit_length, longest_visit,
                       shortest_visit)
