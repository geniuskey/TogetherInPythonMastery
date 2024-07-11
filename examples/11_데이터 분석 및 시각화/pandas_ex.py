import pandas as pd

# 데이터프레임 생성
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(f"DataFrame:\n{df}")

# 열 선택
names = df['Name']
print(f"Names:\n{names}")

# 조건 필터링
age_above_30 = df[df['Age'] > 30]
print(f"Age above 30:\n{age_above_30}")

# 새로운 열 추가
df['Salary'] = [70000, 80000, 90000]
print(f"DataFrame with Salary:\n{df}")

# 그룹화
grouped = df.groupby('City').mean(numeric_only=True)
print(f"Grouped by City:\n{grouped}")

# 데이터 병합
data1 = {'Key': ['A', 'B', 'C'], 'Value1': [1, 2, 3]}
data2 = {'Key': ['A', 'B', 'D'], 'Value2': [4, 5, 6]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
merged_df = pd.merge(df1, df2, on='Key', how='outer')
print(f"Merged DataFrame:\n{merged_df}")
