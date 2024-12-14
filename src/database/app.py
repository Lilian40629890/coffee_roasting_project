import subprocess

def execute_scripts():
    # 定义脚本文件名
    scripts = ['data_cleaning.py', 'import_data.py', 'export_data.py']
    
    for script in scripts:
        try:
            # 使用 subprocess 执行脚本
            result = subprocess.run(['python', script], check=True, capture_output=True, text=True)
            print(f'{script} 执行成功')
            print(result.stdout)  # 打印脚本执行输出
        except subprocess.CalledProcessError as e:
            print(f'{script} 执行失败')
            print(e.stderr)  # 打印错误输出
            return False  # 如果有任何一个脚本执行失败，返回 False
    
    return True  # 如果所有脚本都成功执行，返回 True

# 执行脚本并打印结果
if execute_scripts():
    print('Success！')
else:
    print('Failed')
