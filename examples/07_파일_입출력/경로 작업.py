import os

# 경로 결합
directory = 'example_dir'
filename = 'example.txt'

file_path = os.path.join(directory, filename)
print(f"Full file path: {file_path}")

# 절대 경로 얻기
relative_path = 'example.txt'
absolute_path = os.path.abspath(relative_path)
print(f"Absolute path: {absolute_path}")

# 경로 분리
file_path = '/path/to/example.txt'
directory, filename = os.path.split(file_path)
print(f"Directory: {directory}")
print(f"Filename: {filename}")
