import os

os.rename("'timex'.txt", 'timex.txt')  
os.rename("'temp1'.txt", 'temp1.txt')  
os.rename("'temp2'.txt", 'temp2.txt')  

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

# Modify three files
modify_file("timex.txt")
modify_file("temp1.txt")
modify_file("temp2.txt")

print("Three files have been modified successfully.")
