import os
import subprocess
import paramiko

# Configuration for NAS connection
NAS_HOST = "192.168.1.100"  # NAS 的 IP 位址
NAS_USERNAME = "admin"      # 登入用戶名
NAS_PASSWORD = "password"   # 登入密碼
NAS_FOLDER = "/Public/Coffee/Artisan/"  # NAS 上的目標資料夾
LOCAL_LOG_FOLDER = "/Users/lilianlee/coffee_database"  # 將檔案下載到本地的資料夾

# 數據文件夾
DATA_FOLDER = './data/'

# MySQL 資料庫配置
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'coffee'
}

# Step 1: Connect to NAS and fetch log files
def connect_and_fetch_logs():
    try:
        print("Connecting to NAS...")
        # 使用 paramiko 建立 SFTP 連線
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(NAS_HOST, username=NAS_USERNAME, password=NAS_PASSWORD)
        
        # 使用 SFTP 下載檔案
        sftp = ssh.open_sftp()
        os.makedirs(LOCAL_LOG_FOLDER, exist_ok=True)
        
        # 確保目錄存在
        try:
            file_list = sftp.listdir_attr(NAS_FOLDER)
        except IOError as e:
            raise Exception(f"Unable to access NAS folder {NAS_FOLDER}: {e}")
        
        for file_attr in file_list:
            if file_attr.filename.endswith('.log'):
                remote_file = os.path.join(NAS_FOLDER, file_attr.filename)
                local_file = os.path.join(LOCAL_LOG_FOLDER, file_attr.filename)
                print(f"Downloading {remote_file} to {local_file}")
                sftp.get(remote_file, local_file)
        
        sftp.close()
        ssh.close()
        print("NAS log files fetched successfully.")
    except Exception as e:
        print(f"Error connecting to NAS: {e}")
        raise

# Step 2: Process log files with your scripts
def process_logs_with_scripts():
    try:
        log_files = [f for f in os.listdir(LOCAL_LOG_FOLDER) if f.endswith('.log')]
        script_paths = ["linebreak_logdata_1.py", "extract_lists_1.1.py", "modify_file_name_1.2.py", "modify_file_content_1.3.py", "timestamps_1.4.py", "integrate_lists_2.py","export_sql_3.py", "delete_temporary_files_4.py"]
        
        for log_file in log_files:
            print(f"Processing {log_file}")
            for script in script_paths:
                print(f"Running {script} on {log_file}")
                result = subprocess.run(["python", script, os.path.join(LOCAL_LOG_FOLDER, log_file)], capture_output=True, text=True)
                if result.returncode != 0:
                    print(f"Error in {script}: {result.stderr}")
                    raise Exception(f"{script} failed on {log_file}")
                print(f"{script} completed for {log_file}.")
    except Exception as e:
        print(f"Error processing logs: {e}")
        raise

# Step 3: Main execution flow
if __name__ == "__main__":
    try:
        # Step 1: Fetch logs
        connect_and_fetch_logs()
        # Step 2: Process logs
        process_logs_with_scripts()
        # All done
        print("Success")
    except Exception as e:
        print(f"Script terminated with errors: {e}")
