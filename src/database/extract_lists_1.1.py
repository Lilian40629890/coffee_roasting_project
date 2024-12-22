import re
import sys
import os

def find_multiple_lists_in_log(file_path, list_names):
    """
    在日志文件中找到指定多个列表名称及其值
    :param file_path: 日志文件路径
    :param list_names: 要查找的列表名称列表（list）
    :return: 包含所有列表匹配结果的字典
    """
    results = {list_name: [] for list_name in list_names}  # 初始化结果字典
    # 构造正则表达式，匹配任意一个列表名称
    pattern = rf"({'|'.join(map(re.escape, list_names))}):\s*\[.*?\]"
    try:
        with open(file_path, 'r') as file:
            for line in file:
                matches = re.findall(pattern, line)  # 查找所有匹配的列表
                for match in matches:
                    # 提取列表名称和值，存入结果字典
                    for list_name in list_names:
                        if line.startswith(f"{list_name}:"):
                            results[list_name].append(line.strip())
    except FileNotFoundError:
        print(f"找不到文件：{file_path}")
        return {}
    return results
    

# 使用示例

# 從命令列引數接收檔案路徑
log_file = sys.argv[1]  # 第一個命令列參數是檔案路徑

lists_to_find = ["'timex'", "'temp1'", "'temp2'"]  # 要查找的多个列表名称

found_lists = find_multiple_lists_in_log(log_file, lists_to_find)
if found_lists:
    print("找到以下列表:")
    
    # 設定儲存檔案的目錄
    output_dir = "/Users/lilianlee/coffee_database"
    os.makedirs(output_dir, exist_ok=True)  # 如果資料夾不存在則創建
    
    for list_name, entries in found_lists.items():
        print(f"\n{list_name}:")
        for entry in entries:
            print(entry)
        
        # 設定輸出的檔案路徑
        file_name = os.path.join(output_dir, f"{list_name}.txt")  # 使用列表名稱作為檔案名稱
        with open(file_name, "w") as file:
            for entry in entries:
                file.write(entry + "\n")
        print(f"已將數據儲存到檔案：{file_name}")
else:
    print("未找到符合条件的列表。")


