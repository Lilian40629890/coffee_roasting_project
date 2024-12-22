# 定義一個函數來處理檔案的修改
def modify_file(file_name):
    # 讀取檔案內容
    with open(file_name, "r") as file:
        content = file.read()
    # 刪除前十個字與最後三個字
    modified_content = content[10:-3]
    # 儲存修改後的內容回原檔案
    with open(file_name, "w") as file:
        file.write(modified_content)

# 修改三個檔案
modify_file("timex.txt")
modify_file("temp1.txt")
modify_file("temp2.txt")

print("三個檔案已經修改完成。")
