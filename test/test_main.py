import os  # 导入 os 模块
import pandas as pd

# Mocked MySQL connection configuration for testing
db_config = {
    'host': 'localhost',    
    'user': 'root',         
    'password': 'password', 
    'database': 'coffee'    
}

# Path to the testing CSV file
test_file_path = 'test/sample_data/for new data/24-03-11_2144.laflore.washed.csv'

# Simulate database connection
def mock_connect_to_mysql():
    print("Mock: Connected to MySQL database (simulation)")
    return True  # Simulated connection object

# Simulate reading and processing CSV
def process_csv(file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Check if required columns are included and extract
        required_columns = ['timestamp', 'temp1', 'temp2']
        if not all(col in df.columns for col in required_columns):
            print(f"false: CSV file {file_path} missing required columns: {required_columns}")
            return None
        return df[required_columns]  # Extract required columns
    except Exception as e:
        print(f"false: Error reading CSV file {file_path}: {e}")
        return None

# Mock function to extract bean_type, process_type and roasting_batch_id from file name
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

# Mock upload function
def mock_upload_to_mysql(df, bean_type, process_type, roasting_batch_id, connection):
    print("Mock: Uploading data to MySQL (simulation)")
    print(f"Bean Type: {bean_type}, Process Type: {process_type}, Roasting Batch ID: {roasting_batch_id}")
    print(df.head())  # Print a preview of the data for verification

# Main test execution function
def test_process_file():
    # Mock database connection
    connection = mock_connect_to_mysql()
    if not connection:
        return
    
    # Process the test file
    print(f"Processing test file: {test_file_path}")
    bean_type, process_type, roasting_batch_id = extract_info_from_filename(test_file_path)  # 修正：增加 roasting_batch_id
    if not bean_type or not process_type or not roasting_batch_id:
        return  # Skip if extraction fails
    
    # Read and process the CSV
    df = process_csv(test_file_path)
    if df is not None:
        # Mock upload data to database
        mock_upload_to_mysql(df, bean_type, process_type, roasting_batch_id, connection)
    else:
        print("false: Data processing failed")

# Execute test script
if __name__ == "__main__":
    test_process_file()


# Main test execution function
def test_process_file():
    # Mock database connection
    connection = mock_connect_to_mysql()
    if not connection:
        return
    
    # Process the test file
    print(f"Processing test file: {test_file_path}")
    bean_type, process_type = extract_info_from_filename(test_file_path)
    if not bean_type or not process_type:
        return  # Skip if extraction fails
    
    # Read and process the CSV
    df = process_csv(test_file_path)
    if df is not None:
        # Mock upload data to database
        mock_upload_to_mysql(df, bean_type, process_type, roasting_batch_id, connection)
    else:
        print("false: Data processing failed")

# Execute test script
if __name__ == "__main__":
    test_process_file()
