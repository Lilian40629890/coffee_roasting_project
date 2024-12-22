import os
import pandas as pd
import mysql.connector
from mysql.connector import Error

# MySQL连接配置
db_config = {
    'host': 'localhost',    # 替换为你的MySQL主机地址
    'user': 'root',         # 替换为你的MySQL用户名
    'password': 'password', # 替换为你的MySQL密码
    'database': 'coffee'    # 替换为你的数据库名称
}

# 目標資料夾路徑
folder_path = '/Public/Coffee/Artisan/new_roasting_data'

# 連接MySQL資料庫
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("成功連接到MySQL資料庫")
            return connection
    except Error as e:
        print(f"錯誤: 無法連接到MySQL資料庫: {e}")
        return None

# 读取并提取CSV文件中的数据
def process_csv(file_path):
    try:
        # 读取CSV文件
        df = pd.read_csv(file_path)
        
        # 检查是否包含所需的列并提取
        required_columns = ['timestamp', 'temp1', 'temp2']
        if not all(col in df.columns for col in required_columns):
            print(f"错误: CSV文件 {file_path} 缺少必要的列 {required_columns}")
            return None
        return df[required_columns]  # 提取所需的列
    except Exception as e:
        print(f"错误: 读取CSV文件 {file_path} 失败: {e}")
        return None

# 从文件名中提取bean_type和process_type
def extract_info_from_filename(filename):
    try:
        # 假设文件名格式：YY-MM-DD-tttt_beantype_processtype.alog
        base_name = os.path.splitext(filename)[0]  # 去除文件后缀
        parts = base_name.split('_')
        if len(parts) != 3:
            print(f"错误: 文件名 {filename} 格式不正确")
            return None, None
        # 提取bean_type和process_type
        bean_type = parts[1]
        process_type = parts[2]
        return bean_type, process_type
    except Exception as e:
        print(f"错误: 从文件名 {filename} 提取信息失败: {e}")
        return None, None

# 上传数据到MySQL
def upload_to_mysql(df, bean_type, process_type, connection):
    cursor = connection.cursor()
    try:
        # 插入数据到已有表格
        for _, row in df.iterrows():
            cursor.execute(
                "INSERT INTO roasting_data (timestamp, temp1, temp2, bean_type, process_type) VALUES (%s, %s, %s, %s, %s)",
                (row['timestamp'], row['temp1'], row['temp2'], bean_type, process_type)
            )
        connection.commit()
        print(f"成功上传 {len(df)} 条数据到数据库")
    except Error as e:
        print(f"错误: 上传数据到数据库时出现问题: {e}")
        connection.rollback()

# 遍历文件夹并处理所有CSV文件
def process_folder():
    connection = connect_to_mysql()
    if not connection:
        return
    
    # 浏览资料夹中的所有CSV文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            print(f"处理文件: {file_path}")
            
            # 从文件名中提取bean_type和process_type
            bean_type, process_type = extract_info_from_filename(filename)
            if not bean_type or not process_type:
                continue  # 如果无法提取信息，跳过此文件
            
            # 读取CSV文件并处理
            df = process_csv(file_path)
            if df is not None:
                upload_to_mysql(df, bean_type, process_type, connection)
    
    # 关闭数据库连接
    if connection.is_connected():
        connection.close()
        print("已关闭MySQL数据库连接")

# 执行脚本
if __name__ == "__main__":
    process_folder()