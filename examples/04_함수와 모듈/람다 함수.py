# 데이터 필터링 함수 정의
def filter_data(data, condition):
    return list(filter(condition, data))


# 람다 함수를 사용하여 짝수만 필터링
data = [5, 2, 9, 1, 5, 6]
filtered_data = filter_data(data, lambda x: x % 2 == 0)
print(filtered_data)  # [2, 6]
