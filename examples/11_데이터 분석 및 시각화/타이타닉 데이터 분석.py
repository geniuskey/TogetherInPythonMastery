import pandas as pd
import numpy as np

# 데이터 로드
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_df = pd.read_csv(url)

# 데이터 미리보기
print(titanic_df.head())

# 데이터 요약
print(titanic_df.describe())

# 결측값 처리
titanic_df = titanic_df.fillna(0)

# 특정 열 선택
age_and_fare = titanic_df[['Age', 'Fare']]
print(age_and_fare.head())

# 새로운 열 추가
titanic_df['FamilySize'] = titanic_df['SibSp'] + titanic_df['Parch'] + 1
print(titanic_df.head())

# 성별로 그룹화하여 생존률 계산
gender_survival_rate = titanic_df.groupby('Sex')['Survived'].mean()
print(gender_survival_rate)

# 특정 조건 데이터 필터링
children = titanic_df[titanic_df['Age'] < 18]
print(children.head())
