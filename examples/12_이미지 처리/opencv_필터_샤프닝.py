import cv2
import numpy as np

# 이미지 읽기
image = cv2.imread('example.jpg')

# 샤프닝 커널 생성
sharpen_kernel = np.array([[-1, -1, -1],
                           [-1,  9, -1],
                           [-1, -1, -1]])

# 샤프닝 필터 적용
sharpened_image = cv2.filter2D(image, -1, sharpen_kernel)

# 이미지 표시
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
