# Data Management

## How to Collect Data
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
- Run main application for new data: `src/new_data_management/app_new_data_management.py`
- Run main application for old data: `src/old_data_management/app_old_data_management.py`

## New Data Management Scripts Overview
- **app_new_data_management.py**: Processes CSV files containing coffee roasting data by extracting timestamp, temp1, and temp2 columns dynamically. Parses bean_type and process_type from file names (e.g., YY-MM-DD-TTTT_beantype_processtype.alog) and integrates the information before uploading it to a MySQL database, ensuring compatibility with existing database schema.

## Old Data Management Scripts Overview
- **linebreak_logdata_1.py**: Breaks the log data into lines for easier processing.
    - **extract_lists_1.1**: Extracts relevant data from the log and stores it in temporary files.
    - **file_modification_1.2.py**: Modifies the content of the temporary files for better organization.
    - **timestamps_1.3.py**: Converts timestamp data into a format usable by SQL.
- **integrate_lists_2.py**: Integrates the extracted lists into a table format.
- **import_sql_3.py**: Imports the table data into personal SQL database.
- **delete_temporary_files_4.py**: Deletes temporary files after processing is complete.