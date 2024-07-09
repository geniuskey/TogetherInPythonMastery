# 딕셔너리 정의
person = {"name": "Alice", "age": 25, "city": "New York"}

# 값 접근
print(person["name"])  # Alice

# 값 변경
person["age"] = 26
print(person)  # {'name': 'Alice', 'age': 26, 'city': 'New York'}

# 새로운 키-값 쌍 추가
person["email"] = "alice@example.com"
print(person)  # {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}

# 키-값 쌍 삭제
del person["city"]
print(person)  # {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}
