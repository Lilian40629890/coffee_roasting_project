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

df = df.fillna(0)  # 將 NaN 值替換為 0

# 建立 MySQL 連線
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="coffee",
)

cursor = connection.cursor()

# 插入數據
for index, row in df.iterrows():
    sql = """
    INSERT INTO coffee.coffee_roasting_database (timestamp, time, temp1, temp2, bean_type, process_type, roasting_batch_id) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, tuple(row))

# 提交並關閉
connection.commit()
cursor.close()
connection.close()

print("Data successfully inserted!")
