import csv
import mysql.connector
import pytest
import os
import re

# Helper function to extract metadata from filename
def extract_file_metadata(filename):
    pattern = r"(\d{2}-\d{2}-\d{2})_(\d{4})_([^_]+)_([^_]+)\.csv"
    match = re.match(pattern, filename)
    if not match:
        raise ValueError(f"Filename {filename} does not match the expected format.")
    date, time, bean_type, process_type = match.groups()
    roasting_batch_id = date.replace("-", "") + time
    return bean_type, process_type, roasting_batch_id


# Function to process and upload data
def process_and_upload_data(file_path, db_connection):
    filename = os.path.basename(file_path)
    bean_type, process_type, roasting_batch_id = extract_file_metadata(filename)

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["bean_type"] = bean_type
            row["process_type"] = process_type
            row["roasting_batch_id"] = roasting_batch_id
            insert_data_into_mysql(row, db_connection)


# MySQL insert function
def insert_data_into_mysql(row, db_connection):
    cursor = db_connection.cursor()
    insert_query = """
    INSERT INTO your_table_name (timestamp, time, temp1, temp2, bean_type, process_type, roasting_batch_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    data = (
        row["timestamp"],
        row["time"],
        row["temp1"],
        row["temp2"],
        row["bean_type"],
        row["process_type"],
        row["roasting_batch_id"],
    )
    cursor.execute(insert_query, data)
    db_connection.commit()


# MySQL fetch function for testing
def fetch_data_from_mysql(db_connection):
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM your_table_name")
    return cursor.fetchall()


# Testing function
def test_process_and_upload_data():
    # Mock database connection
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="coffee_roasting_data",
    )

    test_file_path = "tests(for new data)/24-03-11_2144.laflore.washed.csv (testing data)"

    # Process and upload data
    process_and_upload_data(test_file_path, db_connection)

    # Fetch and validate data
    result = fetch_data_from_mysql(db_connection)
    assert len(result) > 0  # Ensure data is uploaded
    assert result[0]["bean_type"] == "sakura"
    assert result[0]["process_type"] == "washed"
    assert result[0]["roasting_batch_id"] == "2606252130"
    print("Success")

    db_connection.close()


# Execute test
if __name__ == "__main__":
    test_process_and_upload_data()
