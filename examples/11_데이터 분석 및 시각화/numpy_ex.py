import numpy as np

# 배열 생성
arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")

# 다차원 배열 생성
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Matrix:\n{matrix}")

# 배열 연산
arr_sum = np.sum(arr)
print(f"Sum of array: {arr_sum}")

matrix_mean = np.mean(matrix, axis=0)
print(f"Mean of each column in matrix: {matrix_mean}")

# 배열 슬라이싱
arr_slice = arr[1:4]
print(f"Array slice: {arr_slice}")

# 선형 대수 연산
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix_a, matrix_b)
print(f"Matrix product:\n{matrix_product}")

# 난수 생성
random_array = np.random.rand(3, 3)
print(f"Random array:\n{random_array}")
