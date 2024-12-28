import os

#Specify the file name to be deleted
files_to_delete = [
    "/Users/lilianlee/temporary_files/linebreak.txt", 
    "/Users/lilianlee/temporary_files/timex.txt", 
    "/Users/lilianlee/temporary_files/temp1.txt", 
    "/Users/lilianlee/temporary_files/temp2.txt", 
    "/Users/lilianlee/temporary_files/timestamp.txt", 
    "/Users/lilianlee/temporary_files/output.csv"]

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

