import pandas as pd
import pymysql

# 确保正确引用 output_file
from integrate_lists_2 import output_file

# 使用 f-string 來插入變數
file_path = f"/users/lilianlee/coffee_database/{output_file}"
# 確認檔案存在
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
    exit(1)

df = df.fillna(0)  # Replace NaN values ​​with 0

# Establish MySQL connection
# This is a sample configuration for testing purposes. For real projects, use a secure method, such as environment variables, to access sensitive information.
connection = pymysql.connect(
    host="localhost",     # MySQL host (example)
    user="root",          # MySQL username (example)
    password="password",  # MySQL password (example)
    database="coffee",    # MySQL database name
)

cursor = connection.cursor()

#Insert data
for index, row in df.iterrows():
    sql = """
    INSERT INTO coffee.coffee_roasting_database (timestamp, time, temp1, temp2, bean_type, process_type, roasting_batch_id) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, tuple(row))

# Submit and close
connection.commit()
cursor.close()
connection.close()

print("Data successfully inserted!")
