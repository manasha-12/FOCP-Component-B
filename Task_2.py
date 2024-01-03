import sys


def read_shelter_record_file(file_path):
    try:
        with open(file_path, 'r') as file:
            in_lines = file.readlines()

        in_entry_list = []
        in_exit_list = []
        in_cat_list = []

        for record_lines in in_lines:
            if record_lines.strip() == 'END':
                break

            reading_lines = record_lines.strip().split(',')
            cat_type, entry_time, exit_time = reading_lines

            entry_time = int(entry_time)
            exit_time = int(exit_time)

            in_entry_list.append(entry_time)
            in_exit_list.append(exit_time)
            in_cat_list.append(cat_type)

        return in_cat_list, in_entry_list, in_exit_list

    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')
    except Exception as e:
        print(f'An error occurred: {e}')
        # Return default values if an error occurs
        return [], [], []


def calculate_visited_time(in_cat_visit_durations, in_entry_time, in_exit_time, in_cat_type):
    # in_total_time_in_house = timedelta()
    visit_duration = in_exit_time - in_entry_time
    if in_cat_type == 'OURS':
        in_cat_visit_durations.append(visit_duration)
    in_total_time_in_house = sum(in_cat_visit_durations)
    return in_total_time_in_house, in_cat_visit_durations


def count_cat_entry(in_cat_visits, in_intruder_cat_visits, in_cat_type):
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
    total_hours, remaining_minutes = divmod(in_total_time_in_house, 60)
    total_minutes = int(remaining_minutes)
    print(f"""            Log File Analysis
    ==================================
    Cat Visits: {in_cat_visits}
    Other Cats: {in_intruder_cat_visits}
    Total Time in House: {int(total_hours)} Hours, {total_minutes} Minutes
    Average Visit Length: {int(in_average_visit_length)} Minutes
    Longest Visit: {in_longest_visit} Minutes
    Shortest Visit: {in_shortest_visit} Minutes""")


# calling the functions
if len(sys.argv) != 2:
    print("Missing command line argument!")
else:
    data_file_path = sys.argv[1]
    cat_list, entry_list, exit_list = read_shelter_record_file(data_file_path)

    cat_visit_list = []
    for i in range(0, len(cat_list)):
        total_time_in_house, cat_visit_durations = calculate_visited_time(
            cat_visit_list, entry_list[i], exit_list[i], cat_list[i]
        )

    cat_visits = 0
    intruder_cat_visits = 0
    for i in range(0, len(cat_list)):
        cat_visits, intruder_cat_visits = count_cat_entry(
            cat_visits, intruder_cat_visits, cat_list[i]
        )

    average_visit_length, longest_visit, shortest_visit = statistical_overview(
        cat_visits, cat_visit_durations
    )

    # final output
    output_for_cat_shelter(
        cat_visits, intruder_cat_visits, total_time_in_house, average_visit_length,
        longest_visit, shortest_visit
    )
