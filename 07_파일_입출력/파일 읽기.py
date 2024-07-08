# 파일 전체 읽기
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# 파일 한 줄씩 읽기
with open('example.txt', 'r', encoding='utf-8') as file:
    line = file.readline()
    while line:
        print(line, end='')  # 파일 내용 출력 (줄 바꿈 없이)
        line = file.readline()

# 파일 전체를 줄 단위로 읽기
with open('example.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')
