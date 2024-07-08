# 1. 로그 파일 작성

import os
from datetime import datetime


def write_log(message):
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, 'app.log')
    with open(log_file, 'a') as file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"{timestamp} - {message}\n")
    print(f"Log written: {message}")


# 예제 실행
write_log("Application started")
write_log("An error occurred")


# 2. 파일 포인터 조작\

def read_log(offset, length):
    log_file = 'logs/app.log'
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            file.seek(offset)
            data = file.read(length)
            print(f"Read data: {data}")
    else:
        print("Log file does not exist")


# 예제 실행
read_log(0, 50)


# 3. 대용량 파일 처리
def search_in_log(pattern):
    log_file = 'logs/app.log'
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            for line in file:
                if pattern in line:
                    print(f"Found pattern: {line.strip()}")
    else:
        print("Log file does not exist")


# 예제 실행
search_in_log("error")

# 4. 임시 파일 사용
import tempfile


def process_with_temp_file(data):
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        temp_file.write(data.encode())
        temp_file.seek(0)
        processed_data = temp_file.read().decode()
        print(f"Processed data: {processed_data}")


process_with_temp_file("Temporary data processing")

# 5. 압축 파일 처리
import zipfile


def backup_logs():
    log_dir = 'logs'
    backup_dir = 'backup'
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    backup_file = os.path.join(backup_dir, 'logs_backup.zip')
    with zipfile.ZipFile(backup_file, 'w') as zipf:
        for foldername, subfolders, filenames in os.walk(log_dir):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                zipf.write(file_path, os.path.relpath(file_path, log_dir))
    print(f"Logs backed up to {backup_file}")


def extract_backup():
    backup_file = 'backup/logs_backup.zip'
    extract_dir = 'extracted_logs'
    if not os.path.exists(extract_dir):
        os.makedirs(extract_dir)

    with zipfile.ZipFile(backup_file, 'r') as zipf:
        zipf.extractall(extract_dir)
    print(f"Logs extracted to {extract_dir}")


# 예제 실행
backup_logs()
extract_backup()


# 6. 파일 권한 설정
def set_log_file_permissions():
    log_file = 'logs/app.log'
    if os.path.exists(log_file):
        os.chmod(log_file, 0o600)  # 소유자 읽기/쓰기 권한 설정
        print(f"Permissions set for {log_file}")


# 예제 실행
set_log_file_permissions()
