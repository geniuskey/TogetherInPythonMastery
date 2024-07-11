try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
else:
    print(content)
finally:
    file.close()
    print("파일을 닫았습니다.")
