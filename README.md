# Coffee Data Management Project

This repository contains Python code and resources for managing and analyzing coffee roasting data.

## Features
- Organizes historical data in a structured MySQL database.
- Collects real-time roasting temperature data, and sythesize it to MySQL database. 
- Provides analysis tools for visualizing temperature trends.

## How to Use
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the main application to organize new data: `python src/database/new_data/app_new_data.py`

## new data management scripts Overview
- **app_new_data.py**: Processes CSV files containing coffee roasting data by extracting timestamp, temp1, and temp2 columns dynamically. Parses bean_type and process_type from file names (e.g., YY-MM-DD-tttt_beantype_processtype.alog) and integrates the information before uploading it to a MySQL database, ensuring compatibility with existing database schema.

## old data management scripts Overview
- **linebreak_logdata_1.py**: Breaks the log data into lines for easier processing.
- **extract_lists_1.1**: Extracts relevant data from the log and stores it in temporary files.
- **modify_file_name_1.2.py**: Renames temporary files for better organization.
- **modify_file_content_1.3.py**: Modifies the content of the files based on certain rules.
- **timestamps_1.4.py**: Converts timestamp data into a format usable by SQL.
- **integrate_lists_2.py**: Integrates the extracted lists into a table format.
- **import_sql_3.py**: Imports the table data into an SQL database.
- **delete_temporary_files_3.5.py**: Deletes temporary files after processing is complete.

## Project Outcome
![Sample Chart](docs/sample_chart.png)
