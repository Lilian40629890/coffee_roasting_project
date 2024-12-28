import csv
import sys

# Read the file and assign the contents to variables
with open("/Users/lilianlee/temporary_files/timex.txt", "r") as file:
    first_data = [line.strip() for line in file.readlines()]

with open("/Users/lilianlee/temporary_files/temp1.txt", "r") as file:
    second_data = [line.strip() for line in file.readlines()]

with open("/Users/lilianlee/temporary_files/temp2.txt", "r") as file:
    third_data = [line.strip() for line in file.readlines()]

with open("/Users/lilianlee/temporary_files/timestamp.txt", "r") as file:
    fourth_data = [line.strip() for line in file.readlines()]   

# Use the join() method to convert each item in the list into a string
first_data = "\n".join(first_data)  # Concatenate elements into strings using newline characters
second_data = "\n".join(second_data)
third_data = "\n".join(third_data)
fourth_data = "\n".join(fourth_data)

# Use the replace() method to remove all blank keys
cleaned_first_data = first_data.replace(" ", "")
cleaned_second_data = second_data.replace(" ", "")
cleaned_third_data = third_data.replace(" ", "")
cleaned_fourth_data = fourth_data.replace(" ", "")

# Convert the data into a comma separated list
first_list = first_data.split(",")
second_list = second_data.split(",")
third_list = third_data.split(",")
fourth_list = fourth_data.split(",")

# Make sure the lengths of the two lists are the same. If they are different, add null values.
max_length = max(len(first_list), len(second_list), len(third_list), len(fourth_list))
first_list.extend([""] * (max_length - len(first_list)))
second_list.extend([""] * (max_length - len(second_list)))
third_list.extend([""] * (max_length - len(third_list)))
fourth_list.extend([""] * (max_length - len(fourth_list)))

# Merge into table format
table_data = list(zip(fourth_list, first_list, second_list, third_list))

# Extract the first sixteen characters in timestamp.txt
with open("/Users/lilianlee/temporary_files/timestamp.txt", "r") as file:
    first_sixteen_chars = file.read(16)  # Read only the first 16 words

# Example: Convert the format "2023-06-25 21:30" to "2306252130"
roasting_batch_id = (
    first_sixteen_chars[2:4] +  # The last two characters of year
    first_sixteen_chars[5:7] +  # month
    first_sixteen_chars[8:10] +  # day
    first_sixteen_chars[11:13] +  # hour
    first_sixteen_chars[14:16]  # minute
)

print(f"Roasting Batch ID: {roasting_batch_id}")  # Print for confirmation

# Let the user enter bean_type and process_type
print("請輸入以下資料：")
bean_type = input("What is the bean type? ")
process_type = input("What is the process type? ")

# Confirm user input
print(f"Bean Type: {bean_type}, Process Type: {process_type}")

# Add two straight lines and fill in the 'bean_type' and 'process_type' entered by the user
for i in range(len(table_data)):
    table_data[i] = table_data[i] + (bean_type, process_type, roasting_batch_id)

# Define output file name
output_file = "/Users/lilianlee/temporary_files/output.csv" 

# Write table to CSV
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # 寫入表頭
    writer.writerow(["timestamp", "time", "temp1", "temp2", "bean_type", "process_type","roasting_batch_id"])
    # 寫入數據
    writer.writerows(table_data)

print(f"CSV file successfully saved as {output_file}")



