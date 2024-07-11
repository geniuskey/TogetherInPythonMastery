import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 예제 데이터셋 로드
tips = sns.load_dataset("tips")

# Seaborn으로 시각화
sns.set(style="whitegrid")
ax = sns.boxplot(x="day", y="total_bill", hue="smoker", data=tips)

# 그래프 저장
plt.savefig("boxplot.png")  # PNG 형식으로 저장
plt.savefig("boxplot.pdf")  # PDF 형식으로 저장
