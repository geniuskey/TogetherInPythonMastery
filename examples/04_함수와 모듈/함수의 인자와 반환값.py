# 평균 계산 함수 정의
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count


# 함수 호출
data = [5, 2, 9, 1, 5, 6]
average = calculate_average(data)
print(average)  # 4.666666666666667
