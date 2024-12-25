# Coffee Data Management Project

This repository contains Python code and resources for managing and analyzing coffee roasting data.

## Features
- Organizes historical data in a structured MySQL database.
- Collects real-time roasting temperature data, and sythesize it to MySQL database. 
- Provides analysis tools for visualizing temperature trends.



# Data Management

### How to Collect Data
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the main application to organize new data: `src/new_data_management/app_new_data_management.py`

### New Data Management Scripts Overview
- **app_new_data.py**: Processes CSV files containing coffee roasting data by extracting timestamp, temp1, and temp2 columns dynamically. Parses bean_type and process_type from file names (e.g., YY-MM-DD-tttt_beantype_processtype.alog) and integrates the information before uploading it to a MySQL database, ensuring compatibility with existing database schema.

### Old Data Management Scripts Overview
- **linebreak_logdata_1.py**: Breaks the log data into lines for easier processing.
    - **extract_lists_1.1**: Extracts relevant data from the log and stores it in temporary files.
    - **file_modification_1.2.py**: Modifies the content of the temporary files for better organization.
    - **timestamps_1.3.py**: Converts timestamp data into a format usable by SQL.
- **integrate_lists_2.py**: Integrates the extracted lists into a table format.
- **import_sql_3.py**: Imports the table data into personal SQL database.
- **delete_temporary_files_4.py**: Deletes temporary files after processing is complete.

# Testing

### How to Run Test
1. Run the testing application: `python tests/testing_new_data.py`

### Test Script Overview
- **test_main.py**: Validates the correctness of data extraction and transformation logic., and verifies that data is successfully imported into the MySQL database.

# Analysis
# Project Outcome

## Security Disclaimer
The sensitive information (e.g., usernames and passwords) in this project is for demonstration purposes only. It is included to showcase how the project functions. 

For production environments, please follow these best practices:
1. Store sensitive information using environment variables.
2. Ensure that `.env` files or other configuration files are not committed to version control (e.g., by adding them to `.gitignore`).
3. Regularly update passwords and use strong passwords.

### Configuring Environment Variables
You can store sensitive information in a `.env` file and then use Python’s `os.getenv` method to retrieve it. For example:
```python
import os

DB_PASSWORD = os.getenv("DB_PASSWORD")


