import json

# JSON 파일 쓰기
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

with open('example.json', 'w') as file:
    json.dump(data, file, indent=4)

# JSON 파일 읽기
with open('example.json', 'r') as file:
    data = json.load(file)
    print(data)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
