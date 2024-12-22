import sys
import os

# 定義三個要搜尋的指定文字
keywords = ["'timex'", "'temp1'", "'temp2'"]

# 從命令列引數中取得檔案路徑
input_file = sys.argv[1]  # 第一個命令列參數是檔案路徑

# 開啟原始檔案並讀取
with open(input_file, "r", encoding="utf-8") as file:
    content = file.read()

# 處理內容：根據指定的關鍵字進行斷行
for keyword in keywords:
    content = content.replace(keyword, "\n" + keyword)

# 設定儲存檔案的目錄
output_dir = "/Users/lilianlee/coffee_database"
os.makedirs(output_dir, exist_ok=True)  # 如果資料夾不存在則創建

# 儲存更新後的內容到暫時的檔案
output_file = "linebreak.txt"

with open(output_file, "w", encoding="utf-8") as temp_file:
    temp_file.write(content)

print(f"檔案處理完成，已儲存到 {output_file}")



