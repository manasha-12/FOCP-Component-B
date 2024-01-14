import sys

arguments = sys.argv[1:]

if not arguments:
    print("No arguments provided.")
else:
    shortest_argument = sorted(arguments, key=len)[0]

    print(f"The shortest argument is: {shortest_argument}")
