import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


"""데이터 준비
타이타닉 데이터셋을 로드하고, 전처리합니다."""
# 데이터 로드
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_df = pd.read_csv(url)

# 필요한 열 선택 및 결측값 처리
titanic_df = titanic_df[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
titanic_df['Age'].fillna(titanic_df['Age'].mean(), inplace=True)

# 범주형 변수 처리
titanic_df = pd.get_dummies(titanic_df, columns=['Sex'], drop_first=True)

# 특징과 타겟 변수 분리
X = titanic_df.drop('Survived', axis=1)
y = titanic_df['Survived']

# 데이터셋을 학습 세트와 테스트 세트로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 특징 스케일링
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


"""모델 학습 및 평가
로지스틱 회귀 모델을 사용하여 타이타닉 생존자 예측 모델을 학습시키고 평가합니다."""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 로지스틱 회귀 모델 생성
model = LogisticRegression()

# 모델 학습
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 평가
accuracy = accuracy_score(y_test, y_pred)
print("정확도:", accuracy)
print("분류 보고서:\n", classification_report(y_test, y_pred))
print("혼동 행렬:\n", confusion_matrix(y_test, y_pred))