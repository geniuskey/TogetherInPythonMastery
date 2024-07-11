import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 샘플 데이터셋 로드
tips = sns.load_dataset('tips')

# 산점도 생성
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time')
plt.title('Total Bill vs Tip')
plt.show()

# 히트맵 생성
corr = tips.select_dtypes(include=['number']).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# 박스플롯 생성
sns.boxplot(data=tips, x='day', y='total_bill', hue='sex')
plt.title('Total Bill by Day and Sex')
plt.show()
