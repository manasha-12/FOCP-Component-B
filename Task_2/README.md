# Cat Shelter Log Analyzer
This Python program analyzes the daily log file from a cat shelter. The program provides insights into the shelter's usage, tracking the activities of the correct cat and potential intruders.

# Usage
To run the program, provide the name of the data file as a command-line argument. The program will process the file and display relevant statistics about the cat shelter usage.

# Log File Format
The log file records cat activities, including entry and departure times. Each line represents a cat's visit or the end of the data stream.

  * OURS: Correct cat's entry.
  * THEIRS: Intruder cat's entry.
  * END: End of the data stream.
  
Times are represented in minutes since midnight.

# Output
The program outputs the following statistics:

  * Total number of times the correct cat entered the shelter.
  * Number of times intruding cats were doused with water.
  * Total time spent in the shelter by the correct cat.
  * Average duration of each visit by the correct cat.
  * Duration of the longest visit by the correct cat.
  * Duration of the shortest visit by the correct cat.
