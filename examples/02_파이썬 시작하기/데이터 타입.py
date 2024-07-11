"""파이썬 기본 데이터 타입 소개"""

"""리스트
리스트는 여러 값을 저장할 수 있는 데이터 타입입니다.
리스트는 대괄호 []로 감싸서 정의합니다."""
numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # 1
print(numbers[-1])  # 5
print(numbers[1:3])  # [2, 3]
numbers.append(6)
print(numbers)  # [1, 2, 3, 4, 5, 6]


"""튜플
튜플은 변경할 수 없는 리스트입니다. 
소괄호 ()로 감싸서 정의합니다."""
colors = ("red", "green", "blue")
print(colors[0])  # red


"""딕셔너리
딕셔너리는 키-값 쌍을 저장하는 데이터 타입입니다. 
중괄호 {}로 감싸서 정의합니다."""
person = {"name": "Alice", "age": 25}
print(person["name"])  # Alice
person["age"] = 26
print(person)  # {'name': 'Alice', 'age': 26}


"""세트
세트는 중복을 허용하지 않는 데이터 타입입니다. 
중괄호 {}를 사용하여 정의하며, 값의 순서는 무작위입니다."""
unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)  # {1, 2, 3, 4}
