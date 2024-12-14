import csv

# 讀取 list1.txt, list2.txt 和 list3.txt，並指派給變數 a, b, c
with open("timex.txt", "r") as file:
    first_data = [line.strip() for line in file.readlines()]

with open("temp1.txt", "r") as file:
    second_data = [line.strip() for line in file.readlines()]

with open("temp2.txt", "r") as file:
    third_data = [line.strip() for line in file.readlines()]

# 使用 join() 方法將列表中的每一項轉換成字串
first_data = "\n".join(first_data)  # 用換行符將元素連接成字串
second_data = "\n".join(second_data)
third_data = "\n".join(third_data)

# 使用 replace() 方法移除所有空白鍵
cleaned_first_data = first_data.replace(" ", "")
cleaned_second_data = second_data.replace(" ", "")
cleaned_third_data = third_data.replace(" ", "")

# 將數據依逗號分隔轉換為列表
first_list = first_data.split(",")
second_list = second_data.split(",")
third_list = third_data.split(",")


# 確保兩列表長度相同，若不同則補充空值
max_length = max(len(first_list), len(second_list), len(third_list))
first_list.extend([""] * (max_length - len(first_list)))
second_list.extend([""] * (max_length - len(second_list)))
third_list.extend([""] * (max_length - len(third_list)))

# 合併成表格格式
table_data = list(zip(first_list, second_list, third_list))

# 新增兩個直行並填入 'A' 和 'B'
for i in range(len(table_data)):
    table_data[i] = table_data[i] + ('sakura', '2') # 輸入豆種＋處理方式

# 定義輸出檔名
output_file = "output.sakura.csv" 

# 將表格寫入 CSV
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # 寫入表頭
    writer.writerow(["time", "temp1","temp2","bean_type","roasting_type"])
    # 寫入數據
    writer.writerows(table_data)




import os

# 指定要刪除的檔案名稱
files_to_delete = ["time.txt", "temp1.txt", "temp2.txt", "temp_output.txt" ]

# 刪除檔案
for file in files_to_delete:
    try:
        # 確認檔案是否存在，再進行刪除
        if os.path.exists(file):
            os.remove(file)
            print(f"{file} 已成功刪除")
        else:
            print(f"{file} 不存在")
    except Exception as e:
        print(f"刪除 {file} 時發生錯誤: {e}")

print(f"CSV 文件已成功儲存為 {output_file}")