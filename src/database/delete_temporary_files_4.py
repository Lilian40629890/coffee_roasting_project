import os

# 指定要刪除的檔案名稱
files_to_delete = ["linebreak.txt", "time.txt", "temp1.txt", "temp2.txt", "temp_output.txt", "timestamps.txt", "output.csv"]

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

