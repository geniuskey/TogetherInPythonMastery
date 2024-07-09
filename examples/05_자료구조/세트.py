# 세트 정의
numbers = {1, 2, 3, 4, 5}

# 요소 추가
numbers.add(6)
print(numbers)  # {1, 2, 3, 4, 5, 6}

# 요소 삭제
numbers.remove(3)
print(numbers)  # {1, 2, 4, 5, 6}

# 다른 세트와의 연산
evens = {2, 4, 6, 8}
print(numbers.union(evens))  # {1, 2, 4, 5, 6, 8}
print(numbers.intersection(evens))  # {2, 4, 6}
print(numbers.difference(evens))  # {1, 5}
