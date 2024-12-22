import os
import re
import sys
from datetime import datetime, timedelta

# 解析檔案名稱中的時間
def parse_time_from_filename(filename):
    match = re.match(r"(\d{2})-(\d{2})-(\d{2})_(\d{4})", filename)
    if match:
        year = "20" + match.group(1)  # 假設年份是20XX
        month = match.group(2)
        day = match.group(3)
        hour = match.group(4)[:2]
        minute = match.group(4)[2:]
        time_str = f"{year}-{month}-{day} {hour}:{minute}"
        return datetime.strptime(time_str, "%Y-%m-%d %H:%M")
    return None

# 讀取 timex.txt 中的數值列表
def read_timex_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        values = [float(val.strip()) for val in content.split(",")]
    return values

# 將數值轉換為符合 SQL TIMESTAMP 格式的 timestamp
def convert_to_timestamp(start_time, time_values):
    timestamp = [
        (start_time + timedelta(seconds=val)).strftime("%Y-%m-%d %H:%M:%S")
        for val in time_values
    ]
    return timestamp

# 將結果寫入新檔案，以逗號分隔的列表形式
def write_timestamp_file(output_path, timestamp):
    with open(output_path, "w") as file:
        file.write(", ".join(timestamp))  # 將列表轉為逗號分隔的字串

# 主邏輯
def process_file(filename, timex_file, output_file):
    # 1. 從檔案名稱解析起始時間
    start_time = parse_time_from_filename(filename)
    if not start_time:
        raise ValueError("無法從檔案名稱解析起始時間")

    # 2. 讀取 timex.txt 中的數值
    time_values = read_timex_file(timex_file)

    # 3. 轉換數值為符合 SQL TIMESTAMP 的格式
    timestamp = convert_to_timestamp(start_time, time_values)

    # 4. 將 timestamps 寫入新的檔案
    write_timestamp_file(output_file, timestamp)
    print(f"已成功將 timestamp 寫入 {output_file}")

# 使用範例
if __name__ == "__main__":
    # 從命令列引數取得檔案名稱
    if len(sys.argv) < 2:
        print("請提供檔案名稱作為命令列參數")
        sys.exit(1)

    input_filename = sys.argv[1]  # 取得命令列傳遞的檔案名稱
    timex_file = "timex.txt"  # 假設的輸入檔案
    output_dir = "/Users/lilianlee/coffee_database"  # 指定的儲存目錄
    os.makedirs(output_dir, exist_ok=True)  # 如果資料夾不存在，則創建

    # 產生完整的輸出檔案路徑
    output_file = os.path.join(output_dir, "timestamp.txt")

    process_file(input_filename, timex_file, output_file)



