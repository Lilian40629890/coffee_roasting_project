# Sample Data
This project processes two types of datasets. The data format was updated this year July, resulting in differences in the processing methods. 

## Data Format
1. New Data: 
 - Key Characteristics:
   - In csv format.
   - Naming: Unified in file naming. 
     YY-MM-DD_TTTT_beantype_processtype.csv
 - Processing Workflow:
   - Please refer to `src/new_data_management/app_new_data_management.py`
2. Old Data: 
 - Key Characteristics:
   - In log format.
   - Naming: Not unified in file naming. 
     YY-MM-DD_TTTT_descirption.csv
 - Processing Workflow:
   - Please refer to 'src/old_data_management/app_old_data_management.py'

## Explanation of Key Differences
- Format: New data are stored in csv format, where as old data are stored in log.
- Naming: New data has unified naming rules, where as old data has different descriptions.