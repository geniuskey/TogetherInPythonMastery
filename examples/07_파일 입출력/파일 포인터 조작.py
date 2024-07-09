with open('example.txt', 'r') as file:
    file.seek(10)  # 파일 포인터를 10번째 위치로 이동
    content = file.read()
    print(content)
    position = file.tell()  # 현재 파일 포인터 위치 반환
    print(f"Current file pointer position: {position}")