# 예제: 숫자의 제곱 리스트 생성
squares = [x ** 2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 예제: 짝수 필터링
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# 예제: 문자열 길이 리스트 생성
words = ["apple", "banana", "cherry"]
lengths = [len(word) for word in words]
print(lengths)  # [5, 6, 6]

# 중첩된 리스트 컴프리헨션
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
