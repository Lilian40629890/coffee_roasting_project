import os

# Define a function to handle file modifications
def modify_file(file_name):
    # Read file content
    with open(file_name, "r") as file:
        content = file.read()
    # Delete the first ten characters and the last three characters
    modified_content = content[10:-3]
    # Save the modified content back to the original file
    with open(file_name, "w") as file:
        file.write(modified_content)

# Modify files without single quotes in their names
file_names = [
    "/Users/lilianlee/temporary_files/timex.txt", 
    "/Users/lilianlee/temporary_files/temp1.txt", 
    "/Users/lilianlee/temporary_files/temp2.txt"
]

for file_name in file_names:
    modify_file(file_name)

# Confirm the content of each file after modification
for file_name in file_names:
    with open(file_name, "r") as file:
        modified_content = file.read()
    print(f"Content of '{file_name}' after modification:\n{modified_content}\n")

print("Three files have been modified successfully.")
