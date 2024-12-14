# 定義三個要搜尋的指定文字
keywords = ["'timex'", "'temp1'", "'temp2'"]

# 開啟原始檔案並讀取
with open("input.txt", "r", encoding="utf-8") as file:
    content = file.read()

# 處理內容：根據指定的關鍵字進行斷行
for keyword in keywords:
    content = content.replace(keyword, "\n" + keyword)

# 將更新後的內容儲存到暫時的檔案
with open("temp_output.txt", "w", encoding="utf-8") as temp_file:
    temp_file.write(content)

print("檔案處理完成，已儲存到 temp_output.txt")


