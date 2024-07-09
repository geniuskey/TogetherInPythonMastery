import data_processing_module

data = [5, 2, 9, 1, 5, 6]

# 정렬된 데이터 출력
sorted_data = data_processing_module.sort_data(data)
print(sorted_data)  # [1, 2, 5, 5, 6, 9]

# 평균 계산
average = data_processing_module.calculate_average(data)
print(average)  # 4.666666666666667

# 필터링된 데이터 출력
filtered_data = data_processing_module.filter_data(data, lambda x: x % 2 == 0)
print(filtered_data)  # [2, 6]
