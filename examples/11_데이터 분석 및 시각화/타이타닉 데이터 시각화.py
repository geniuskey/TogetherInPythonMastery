import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_df = pd.read_csv(url)

# Figure와 서브플롯 생성
fig, axes = plt.subplots(2, 2)

# 생존자와 사망자 수 시각화
sns.countplot(data=titanic_df, x='Survived', ax=axes[0, 0])
axes[0, 0].set_title('Survival Count')

# 성별에 따른 생존률 시각화
sns.barplot(data=titanic_df, x='Sex', y='Survived', ax=axes[0, 1])
axes[0, 1].set_title('Survival Rate by Sex')

# 나이 분포 시각화
sns.histplot(data=titanic_df, x='Age', bins=30, kde=True, ax=axes[1, 0])
axes[1, 0].set_title('Age Distribution')

# 클래스별 생존률 시각화
sns.barplot(data=titanic_df, x='Pclass', y='Survived', hue='Sex', ax=axes[1, 1])
axes[1, 1].set_title('Survival Rate by Class and Sex')

# 레이아웃 조정
plt.tight_layout()
plt.show()
