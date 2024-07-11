import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
import scipy.stats as st

# 샘플 데이터 생성
data = {'feature': [i for i in range(100)], 'target': [1 if i % 2 == 0 else 0 for i in range(100)]}
df = pd.DataFrame(data)
X = df[['feature']]
y = df['target']

# 데이터셋을 학습 세트와 테스트 세트로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 랜덤 포레스트 분류기 생성
rf = RandomForestClassifier(random_state=42)

# 하이퍼파라미터 분포 정의
param_dist = {
    'n_estimators': st.randint(10, 100),
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': st.randint(2, 11)
}

# 랜덤 서치 객체 생성
random_search = RandomizedSearchCV(estimator=rf, param_distributions=param_dist, n_iter=100, cv=5, n_jobs=-1, scoring='accuracy', random_state=42)

# 랜덤 서치 수행
random_search.fit(X_train, y_train)

print("Best Parameters:", random_search.best_params_)
print("Best Cross-Validation Score:", random_search.best_score_)

# 최적 모델로 예측
best_model = random_search.best_estimator_
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Test Set Accuracy:", accuracy)