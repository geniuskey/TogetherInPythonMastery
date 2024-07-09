# 제너레이터 표현식
squares = (x ** 2 for x in range(1, 11))

# 제너레이터 값 하나씩 출력
for square in squares:
    print(square)

# 출력:
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
