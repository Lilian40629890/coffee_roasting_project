import os
import re
from datetime import datetime, timedelta
import sys

# Parse the time in the file name
def parse_time_from_filename(filename):
    # Use regular expressions to match date and time formats
    match = re.match(r"(\d{2})-(\d{2})-(\d{2})_(\d{4})", filename)
    if match:
        year = "20" + match.group(1)  # data collect started at 2020
        month = match.group(2)
        day = match.group(3)
        hour = match.group(4)[:2]
        minute = match.group(4)[2:]
        time_str = f"{year}-{month}-{day} {hour}:{minute}"
        return datetime.strptime(time_str, "%Y-%m-%d %H:%M")
    return None

# Set the folder path where the file is located
folder_path = "/Users/lilianlee/coffee_database/timex.txt"

# Assuming there is only one file in the folder, get the name of the file
filename = os.listdir(folder_path)[0]  # Get the first file name

# Parse the time in the file name
if filename:
    print(f"Parsing time from filename: {filename}")
    file_time = parse_time_from_filename(filename)
    if file_time:
        print(f"Extracted time: {file_time}")
    else:
        print(f"Failed to extract time from {filename}")


# Read the list of values ​​in timex.txt
def read_timex_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        values = [float(val.strip()) for val in content.split(",")]
    return values

# Convert the numeric value to a timestamp that conforms to the SQL TIMESTAMP format
def convert_to_timestamp(start_time, time_values):
    timestamp = [
        (start_time + timedelta(seconds=val)).strftime("%Y-%m-%d %H:%M:%S")
        for val in time_values
    ]
    return timestamp

# Write results to a new file as a comma separated list
def write_timestamp_file(output_path, timestamp):
    with open(output_path, "w") as file:
        file.write(", ".join(timestamp))  #Convert list to comma separated string

# 主邏輯
def process_file(filename, timex_file, output_file):
    # 1. From file name resolution start time
    start_time = parse_time_from_filename(filename)
    if not start_time:
        raise ValueError("Unable to parse start time from archive name")
    # 2. Read the value in timex.txt
    time_values = read_timex_file(timex_file)
    # 3. Convert a numeric value to a format that conforms to SQL TIMESTAMP
    timestamp = convert_to_timestamp(start_time, time_values)
    # 4. Write timestamps to new file
    write_timestamp_file(output_file, timestamp)
    print(f"Successfully written timestamp to {output_file}")


if __name__ == "__main__":
    # Get file name from command line arguments
    if len(sys.argv) < 2:
        print("Please provide the file name as a command line parameter")
        sys.exit(1)
    input_filename = sys.argv[1]  # Get the file name passed by the command line
    timex_file = "/Users/lilianlee/coffee_database/timex.txt"  # Input file name
    output_file = "/Users/lilianlee/coffee_database/timestamp.txt"  # Output file name
    process_file(input_filename, timex_file, output_file)


