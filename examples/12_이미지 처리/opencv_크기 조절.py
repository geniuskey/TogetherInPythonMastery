import cv2

# 이미지 읽기
image = cv2.imread('example.jpg')

# 이미지 크기 조절
resized_image = cv2.resize(image, (300, 150))

# 이미지 표시
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
