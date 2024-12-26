import re
import sys
import os

def find_multiple_lists_in_log(file_path, list_names):
    """
    Find multiple list names and their values ​​specified in the log file
    :param file_path: 
    :param list_names: 
    :return: 
    """
    results = {list_name: [] for list_name in list_names}  #Initialize the result dictionary
    # Construct a regular expression to match any list name
    pattern = rf"({'|'.join(map(re.escape, list_names))}):\s*\[([^\]]+)\]"
    try:
        with open(file_path, 'r') as file:
            for line in file:
                matches = re.findall(pattern, line)  # Find all matching lists
                for match in matches:
                    # Extract list names and values ​​and store them in the result dictionary
                    for list_name in list_names:
                        if line.startswith(f"{list_name}:"):
                            results[list_name].append(line.strip())
    except FileNotFoundError:
        print(f"File not found：{file_path}")
        return {}
    return results
    

# Receive archive path from command line argument
log_file = sys.argv[1]  # The first command line parameter is the file path

lists_to_find = ["'timex'", "'temp1'", "'temp2'"]  # Multiple list names to find

found_lists = find_multiple_lists_in_log(log_file, lists_to_find)
if found_lists:
    print("Find the following list:")

    # Set the directory where files are stored, relative to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current script directory
    output_dir = os.path.join(script_dir, "temporary_files")  # Define the output directory
    os.makedirs(output_dir, exist_ok=True)  # Create the folder if it does not exist

    for list_name, entries in found_lists.items():
        print(f"\n{list_name}:")
        for entry in entries:
            print(entry)

        # Clean the list name to remove single quotes
        cleaned_name = list_name.strip("'")  

        # Set the output file path using cleaned_name
        file_name = os.path.join(output_dir, f"{cleaned_name}.txt")  # Use cleaned name as file name
        with open(file_name, "w") as file:
            for entry in entries:
                file.write(entry + "\n")
        print(f"Data saved to file: {file_name}")
        
        # Confirm the content of the file by reading it back
        print(f"\nConfirming contents of {file_name}:")
        with open(file_name, "r") as file:
            file_contents = file.read()
            print(file_contents)  # Print the file content
else:
    print("No matching listings found.")



