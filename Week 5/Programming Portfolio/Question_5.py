import sys


def process_temperatures(temperatures):
    if not temperatures:
        print("No temperatures provided.")
        return

    temperatures = [float(temp) for temp in temperatures]

    max_temperature = max(temperatures)
    min_temperature = min(temperatures)
    mean_temperature = sum(temperatures) / len(temperatures)

    print(f"Maximum temperature: {max_temperature:.2f}C")
    print(f"Minimum temperature: {min_temperature:.2f}C")
    print(f"Mean temperature: {mean_temperature:.2f}C")


temperature_arguments = sys.argv[1:]

process_temperatures(temperature_arguments)
