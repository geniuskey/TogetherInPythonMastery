import cv2

# 이미지 읽기
image = cv2.imread('example.jpg')

# 이미지 크기 얻기
(h, w) = image.shape[:2]

# 이미지 중심 계산
center = (w // 2, h // 2)

# 회전 행렬 생성 (45도 회전)
M = cv2.getRotationMatrix2D(center, 45, 1.0)

# 이미지 회전
rotated_image = cv2.warpAffine(image, M, (w, h))

# 이미지 표시
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
