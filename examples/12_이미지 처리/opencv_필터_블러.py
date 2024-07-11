import cv2

# 이미지 읽기
image = cv2.imread('example.jpg')

# 평균 블러 필터 적용
average_blur = cv2.blur(image, (5, 5))

# 가우시안 블러 필터 적용
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

# 이미지 표시
cv2.imshow('Original Image', image)
cv2.imshow('Average Blur', average_blur)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
