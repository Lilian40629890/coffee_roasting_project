import csv
import sys

# 讀取檔案並將內容賦值給變數
with open("/Users/lilianlee/coffee_database/timex.txt", "r") as file:
    first_data = [line.strip() for line in file.readlines()]

with open("/Users/lilianlee/coffee_database/temp1.txt", "r") as file:
    second_data = [line.strip() for line in file.readlines()]

with open("/Users/lilianlee/coffee_database/temp2.txt", "r") as file:
    third_data = [line.strip() for line in file.readlines()]

with open("/Users/lilianlee/coffee_database/timestamp.txt", "r") as file:
    fourth_data = [line.strip() for line in file.readlines()]   

# 使用 join() 方法將列表中的每一項轉換成字串
first_data = "\n".join(first_data)  # 用換行符將元素連接成字串
second_data = "\n".join(second_data)
third_data = "\n".join(third_data)
fourth_data = "\n".join(fourth_data)

# 使用 replace() 方法移除所有空白鍵
cleaned_first_data = first_data.replace(" ", "")
cleaned_second_data = second_data.replace(" ", "")
cleaned_third_data = third_data.replace(" ", "")
cleaned_fourth_data = fourth_data.replace(" ", "")

# 將數據依逗號分隔轉換為列表
first_list = first_data.split(",")
second_list = second_data.split(",")
third_list = third_data.split(",")
fourth_list = fourth_data.split(",")

# 確保兩列表長度相同，若不同則補充空值
max_length = max(len(first_list), len(second_list), len(third_list), len(fourth_list))
first_list.extend([""] * (max_length - len(first_list)))
second_list.extend([""] * (max_length - len(second_list)))
third_list.extend([""] * (max_length - len(third_list)))
fourth_list.extend([""] * (max_length - len(fourth_list)))

# 合併成表格格式
table_data = list(zip(fourth_list, first_list, second_list, third_list))

# 讓用戶輸入 bean_type 和 process_type
bean_type = input("What is the bean type? ")
process_type = input("What is the process type? ")

# 新增兩個直行並填入用戶輸入的 'bean_type' 和 'process_type'
for i in range(len(table_data)):
    table_data[i] = table_data[i] + (bean_type, process_type)

# 定義輸出檔名
output_file = "/Users/lilianlee/coffee_database/output.csv" 

# 將表格寫入 CSV
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # 寫入表頭
    writer.writerow(["timestamp", "time", "temp1", "temp2", "bean_type", "process_type"])
    # 寫入數據
    writer.writerows(table_data)

print(f"CSV 文件已成功儲存為 {output_file}")



