def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# 제너레이터 객체 생성
counter = count_up_to(5)

# 제너레이터 값 하나씩 출력
for num in counter:
    print(num)
    
# 출력:
# 1
# 2
# 3
# 4
# 5
