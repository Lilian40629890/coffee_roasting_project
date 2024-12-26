import os

# Ensure the working directory is correct
output_dir = "/home/runner/work/coffee_roasting_project/coffee_roasting_project/test/old_data/temporary_files"  # Same directory as in extract_lists_1.1.py

# Update the modify_file function to include the full path
def modify_file(file_name):
    file_path = os.path.join(output_dir, file_name)
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return

    # Read file content
    with open(file_path, "r") as file:
        content = file.read()
    # Delete the first ten characters and the last three characters
    modified_content = content[10:-3]
    # Save the modified content back to the original file
    with open(file_path, "w") as file:
        file.write(modified_content)

# Modify files without single quotes in their names
file_names = ["timex.txt", "temp1.txt", "temp2.txt"]

for file_name in file_names:
    modify_file(file_name)

print("Three files have been modified successfully.")
