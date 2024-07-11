import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 서브플롯 생성
fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(x, y1, 'r', label='sin(x)')
axs[0].set_title('Sine Wave')
axs[0].legend()

axs[1].plot(x, y2, 'b', label='cos(x)')
axs[1].set_title('Cosine Wave')
axs[1].legend()

plt.tight_layout()
plt.show()
