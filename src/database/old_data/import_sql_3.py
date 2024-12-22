import pandas as pd
import pymysql

from integrate_lists_2 import output_file

# 使用 f-string 來插入變數
file_path = f"/users/lilianlee/{output_file}"

# 讀取 CSV 檔案
df = pd.read_csv(file_path)

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
    INSERT INTO coffee.coffee_roasting_database (timestamp, time, temp1, temp2, bean_type, process_type) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, tuple(row))

# 提交並關閉
connection.commit()
cursor.close()
connection.close()

print("Data successfully inserted!")

