import tempfile

# 임시 파일 생성
with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_file.write(b'This is a temporary file.')
    print(f"Temporary file created at {temp_file.name}")

# 임시 디렉토리 생성
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Temporary directory created at {temp_dir}")