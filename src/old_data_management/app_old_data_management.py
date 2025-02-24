import os
import subprocess
import paramiko

# Configuration for NAS connection
# The following username and password are for demonstration purposes only.
# In real applications, it's recommended to use environment variables or other secure methods to store sensitive information.
NAS_HOST = "192.168.1.100"  # IP address of the NAS
NAS_USERNAME = "admin"      # Login username (example)
NAS_PASSWORD = "password"   # Login password (example)
NAS_FOLDER = "/Public/Coffee/Artisan/"  # Target folder on the NAS (example)
LOCAL_LOG_FOLDER = "/Users/lilianlee/coffee_database"  # Download the file to a local folder (example)

#data folder
DATA_FOLDER = '/Users/lilianlee/temporary_files'

# MySQL database configuration
# This is a sample configuration for testing purposes. For real projects, use a secure method, such as environment variables, to access sensitive information.
DB_CONFIG = {
    'host': 'localhost',        # MySQL host (example)
    'user': 'root',             # MySQL username (example)
    'password': 'password',     # MySQL password (example)
    'database': 'coffee'        # MySQL database name (example)
}

# Step 1: Connect to NAS and fetch log files
def connect_and_fetch_logs():
    try:
        print("Connecting to NAS...")
        # Use paramiko to establish SFTP connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(NAS_HOST, username=NAS_USERNAME, password=NAS_PASSWORD)
        
        # Download files using SFTP
        sftp = ssh.open_sftp()
        os.makedirs(LOCAL_LOG_FOLDER, exist_ok=True)
        
        # Make sure the directory exists
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
        script_paths = [
            "src/old_data_management/linebreak_logdata_1.py", 
            "src/old_data_management/extract_lists_1.1.py", 
            "src/old_data_management/file_modification_1.2.py", 
            "src/old_data_management/timestamps_1.3.py", 
            "src/old_data_management/integrate_lists_2.py",
            "src/old_data_management/export_sql_3.py", 
            "src/old_data_management/delete_temporary_files_4.py"
        ]
        
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
