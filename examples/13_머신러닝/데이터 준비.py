from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

"""데이터 준비
머신러닝 모델을 학습시키기 위해서는 데이터를 준비해야 합니다. 
여기서는 Scikit-learn의 내장 데이터셋인 Iris 데이터셋을 사용하여 
데이터를 준비하는 방법을 설명합니다."""
# 데이터 로드
iris = load_iris()
X = iris.data  # 특징 데이터
y = iris.target  # 타겟 레이블

# 데이터셋을 학습 세트와 테스트 세트로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("학습 세트 크기:", X_train.shape)
print("테스트 세트 크기:", X_test.shape)


"""모델 학습
Scikit-learn에서 제공하는 다양한 머신러닝 알고리즘 중 하나를 사용하여 모델을 
학습시킬 수 있습니다. 여기서는 가장 간단한 알고리즘 중 하나인 K-최근접 이웃
(K-Nearest Neighbors, KNN) 알고리즘을 사용하여 모델을 학습시킵니다."""
from sklearn.neighbors import KNeighborsClassifier

# KNN 분류기 생성
knn = KNeighborsClassifier(n_neighbors=3)

# 모델 학습
knn.fit(X_train, y_train)


"""예측
학습된 모델을 사용하여 테스트 데이터에 대한 예측을 수행합니다."""
# 테스트 세트에 대한 예측
y_pred = knn.predict(X_test)

print("예측값:", y_pred)


"""모델 평가
모델의 성능을 평가하기 위해 여러 가지 지표를 사용할 수 있습니다. 
여기서는 정확도(accuracy)를 사용하여 모델의 성능을 평가합니다."""
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 정확도 계산
accuracy = accuracy_score(y_test, y_pred)
print("정확도:", accuracy)

# 분류 보고서 출력
print("분류 보고서:\n", classification_report(y_test, y_pred))

# 혼동 행렬 출력
print("혼동 행렬:\n", confusion_matrix(y_test, y_pred))