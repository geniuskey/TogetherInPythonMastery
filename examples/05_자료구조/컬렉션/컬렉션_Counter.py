from collections import Counter

# 문자열에서 각 문자의 개수 세기
count = Counter("hello world")

print(count)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
