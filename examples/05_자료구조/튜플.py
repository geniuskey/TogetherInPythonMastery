# 튜플 정의
colors = ("red", "green", "blue")

# 요소 접근
print(colors[1])  # green

# 요소 변경 시도 (오류 발생)
# colors[1] = "yellow"  # TypeError: 'tuple' object does not support item assignment

# 튜플 언패킹
r, g, b = colors
print(r, g, b)  # red green blue
