import cv2

# 이미지 읽기
image = cv2.imread('example.jpg')

# 블러 필터 적용
blurred_image = cv2.GaussianBlur(image, (7, 7), 0)

# 이미지 표시
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
