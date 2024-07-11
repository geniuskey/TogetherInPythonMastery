from sklearn import datasets
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 데이터 로드
iris = datasets.load_iris()
X = iris.data
y = iris.target

# PCA 모델 생성 및 학습
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# PCA 결과 시각화
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Iris Dataset')
plt.show()
