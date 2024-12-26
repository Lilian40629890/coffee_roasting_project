import sys
import os

# Define three specific words to search for
keywords = ["'timex'", "'temp1'", "'temp2'"]

# Get the file path from the command line arguments
input_file = sys.argv[1]  # The first command line parameter is the file path

# Open the original file and read it
with open(input_file, "r", encoding="utf-8") as file:
    content = file.read()

# Processing content: Line break based on specified keywords
for keyword in keywords:
    content = content.replace(keyword, "\n" + keyword)

# Set the directory where files are stored
output_dir = "test/old_data/temporary_files"
os.makedirs(output_dir, exist_ok=True)  #Create the folder if it does not exist

# Save updated content to temporary file
output_file = "linebreak.txt"

with open(output_file, "w", encoding="utf-8") as temp_file:
    temp_file.write(content)
    
print(f"File processing completed and saved to {output_file}")

# Read and print the content of the output file for verification
with open(output_file, "r", encoding="utf-8") as temp_file:
    output_content = temp_file.read()

# Print a portion of the output content to check the result
print("\n--- Output File Content Preview ---")
print(output_content[:500])  # Print the first 500 characters as a preview
