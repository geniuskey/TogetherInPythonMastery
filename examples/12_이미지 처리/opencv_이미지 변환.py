import cv2
import numpy as np

# 이미지 읽기
image = cv2.imread('example.jpg')

# 원본 이미지의 세 점
points1 = np.float32([[50, 50], [200, 50], [50, 200]])

# 변환 후 이미지의 세 점
points2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Affine Transform 행렬 계산
M = cv2.getAffineTransform(points1, points2)

# 이미지 변환
transformed_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

# 이미지 표시
cv2.imshow('Original Image', image)
cv2.imshow('Transformed Image', transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
