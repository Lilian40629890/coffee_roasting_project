import os
import pandas as pd
import mysql.connector
from mysql.connector import Error

# MySQL connection configuration
db_config = {
    'host': 'localhost',    
    'user': 'root',         
    'password': 'password', 
    'database': 'coffee'    
}

# Target folder path
folder_path = '/Public/Coffee/Artisan/new_roasting_data'

# Connect to MySQL database
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Successfully connected to MySQL database")
            return connection
    except Error as e:
        print(f"false: Unable to connect to MySQL database: {e}")
        return None

# Read and extract data from CSV files
def process_csv(file_path):
    try:
        #Read CSV file
        df = pd.read_csv(file_path)
        
        # Check if required columns are included and extract
        required_columns = ['timestamp', 'temp1', 'temp2']
        if not all(col in df.columns for col in required_columns):
            print(f"false: CSV file {file_path} Required columns are missing {required_columns}")
            return None
        return df[required_columns]  #Extract the required columns
    except Exception as e:
        print(f"false: Read CSV file {file_path} failed: {e}")
        return None

# Extract bean_type, process_type, and roasting_batch_id from file name
def extract_info_from_filename(filename):
    try:
        # Assume filename format: YY-MM-DD-tttt_beantype_processtype.csv
        base_name = os.path.splitext(filename)[0]  # Remove file extension
        parts = base_name.split('_')
        if len(parts) != 3:
            print(f"false: file name {filename} Incorrect format")
            return None, None, None
        
        # Extract bean_type and process_type
        bean_type = parts[1]
        process_type = parts[2]
        
        # Extract roasting_batch_id (combine YYMMDD and tttt)
        date_and_id = parts[0]  # YY-MM-DD-tttt
        date, batch_id = date_and_id.split('-')[:3], date_and_id.split('-')[3]
        roasting_batch_id = ''.join(date) + batch_id  # YYMMDDtttt
        
        return bean_type, process_type, roasting_batch_id
    except Exception as e:
        print(f"false: from file name {filename} extract information failed: {e}")
        return None, None, None

# Upload data to MySQL
def upload_to_mysql(df, bean_type, process_type, roasting_batch_id, connection):
    cursor = connection.cursor()
    try:
        # Insert data into existing table
        for _, row in df.iterrows():
            cursor.execute(
                "INSERT INTO roasting_data (timestamp, temp1, temp2, bean_type, process_type, roasting_batch_id) VALUES (%s, %s, %s, %s, %s, %s)",
                (row['timestamp'], row['temp1'], row['temp2'], bean_type, process_type, roasting_batch_id)
            )
        connection.commit()
        print(f"success to upload {len(df)} pieces of data to the database")
    except Error as e:
        print(f"false: Problem uploading data to database: {e}")
        connection.rollback()

# Loop through the folder and process all CSV files
def process_folder():
    connection = connect_to_mysql()
    if not connection:
        return
    
    # Browse all CSV files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            print(f"Processing file: {file_path}")
            
            # Extract bean_type, process_type, and roasting_batch_id from file name
            bean_type, process_type, roasting_batch_id = extract_info_from_filename(filename)
            if not bean_type or not process_type or not roasting_batch_id:
                continue  # Skip file if extraction fails
            
            # Read CSV file and process
            df = process_csv(file_path)
            if df is not None:
                upload_to_mysql(df, bean_type, process_type, roasting_batch_id, connection)
    
    # Close database connection
    if connection.is_connected():
        connection.close()
        print("MySQL database connection closed")

# Execute script
if __name__ == "__main__":
    process_folder()
