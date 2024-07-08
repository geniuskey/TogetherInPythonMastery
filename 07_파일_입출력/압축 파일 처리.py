import zipfile

# ZIP 파일 생성
with zipfile.ZipFile('example.zip', 'w') as zipf:
    zipf.write('example.txt')
    zipf.write('another_example.txt')

# ZIP 파일 읽기
with zipfile.ZipFile('example.zip', 'r') as zipf:
    zipf.extractall('extracted_files')
