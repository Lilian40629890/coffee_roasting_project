import os

#Specify the file name to be deleted
files_to_delete = ["linebreak.txt", "time.txt", "temp1.txt", "temp2.txt", "timestamps.txt", "output.csv"]

# Delete files
for file in files_to_delete:
    try:
        # Confirm whether the file exists and then delete it
        if os.path.exists(file):
            os.remove(file)
            print(f"{file} deleted successfully")
        else:
            print(f"{file} does not exist")
    except Exception as e:
        print(f"An error occurred while deleting {file} : {e}")

