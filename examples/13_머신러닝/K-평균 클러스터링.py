import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 샘플 데이터 생성
np.random.seed(42)
X = np.random.rand(100, 2)

# K-평균 클러스터링 모델 생성 및 학습
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# 클러스터 할당
clusters = kmeans.labels_

# 클러스터링 결과 시각화
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
plt.title('K-Means Clustering')
plt.show()
