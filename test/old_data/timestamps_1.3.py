import os
import re
from datetime import datetime, timedelta
import sys

# Parse the time in the file name
def parse_time_from_filename(filename):
    try:
        filename = os.path.basename(filename)
        # Use regular expressions to match date and time formats
        print(f"Attempting to parse filename: {filename}")  # Debugging output
        match = re.match(r"(\d{2})-(\d{2})-(\d{2})_(\d{4})", filename)
        
        # Print if match is found
        if match:
            year = "20" + match.group(1)  # data collect started at 20XX
            month = match.group(2)
            day = match.group(3)
            hour = match.group(4)[:2]
            minute = match.group(4)[2:]
            time_str = f"{year}-{month}-{day} {hour}:{minute}"
            print(f"Extracted time string: {time_str}")  # Debugging output
            return datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        else:
            print(f"Filename does not match expected pattern: {filename}")  # Debugging output
        return None
    except Exception as e:
        print(f"Error parsing time from filename {filename}: {e}")
        return None

# Set the folder path where the file is located
folder_path = "test/old_data/temporary_files"  # Ensure this folder path is correct

# Assuming there is only one file in the folder, get the name of the file
files = os.listdir(folder_path)

# Filter files that match the expected pattern
valid_files = [f for f in files if parse_time_from_filename(f)]

# If no valid files are found
if not valid_files:
    print("No files found with the expected pattern.")
    sys.exit(1)

# Get the first valid file
filename = valid_files[0]

# Parse the time in the file name
if filename:
    print(f"Parsing time from filename: {filename}")
    file_time = parse_time_from_filename(filename)
    if file_time:
        print(f"Extracted time: {file_time}")
    else:
        print(f"Failed to extract time from {filename}")

# Read the list of values in timex.txt
def read_timex_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.readlines()  # Read all lines
            values = []
            for line in content:
                stripped_line = line.strip()  # Remove whitespace characters at the beginning and end of the line
                if stripped_line:  # Ignore empty lines
                    # Use commas to separate numbers and remove whitespace around each number
                    for value in stripped_line.split(","):  # Split by comma
                        cleaned_value = value.strip()  # Remove spaces
                        if cleaned_value:  # Avoid empty values after stripping
                            try:
                                values.append(float(cleaned_value))  # Convert to float and add to list
                            except ValueError:
                                print(f"Invalid value in {file_path}: {cleaned_value}")  # if not a valid number
        if not values:
            raise ValueError(f"No valid numeric values found in {file_path}.")
        return values
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []


# Convert the numeric value to a timestamp that conforms to the SQL TIMESTAMP format
def convert_to_timestamp(start_time, time_values):
    try:
        timestamp = [
            (start_time + timedelta(seconds=val)).strftime("%Y-%m-%d %H:%M:%S")
            for val in time_values
        ]
        return timestamp
    except Exception as e:
        print(f"Error converting time values to timestamp: {e}")
        return []

# Write results to a new file as a comma separated list
def write_timestamp_file(output_path, timestamp):
    try:
        with open(output_path, "w") as file:
            file.write(", ".join(timestamp))  # Convert list to comma separated string
        print(f"Successfully written timestamp to {output_path}")
    except Exception as e:
        print(f"Error writing timestamp to file {output_path}: {e}")

# Main logic
def process_file(filename, timex_file, output_file):
    try:
        # 1. From file name resolution start time
        start_time = parse_time_from_filename(filename)
        if not start_time:
            raise ValueError("Unable to parse start time from archive name")
        
        # 2. Read the value in timex.txt
        time_values = read_timex_file(timex_file)
        print(f"Parsed time values: {time_values}")  # Debugging output
        if not time_values:
            raise ValueError(f"Failed to read or parse time values from {timex_file}")
        
        # 3. Convert a numeric value to a format that conforms to SQL TIMESTAMP
        timestamp = convert_to_timestamp(start_time, time_values)
        if not timestamp:
            raise ValueError("Failed to convert time values to timestamp")
        
        # 4. Write timestamps to new file
        write_timestamp_file(output_file, timestamp)
    except Exception as e:
        print(f"Error processing file {filename}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    input_filename = sys.argv[1]  # Get the file name passed by the command line
    
    # Use os.path.join to ensure correct relative paths
    timex_file = os.path.join("test", "old_data", "temporary_files", "timex.txt")  # Input file name
    output_file = os.path.join("test", "old_data", "temporary_files", "timestamp.txt")  # Output file name
    
    # Process the file
    process_file(input_filename, timex_file, output_file)
