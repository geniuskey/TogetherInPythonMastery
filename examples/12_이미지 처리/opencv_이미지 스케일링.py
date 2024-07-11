import cv2

# 이미지 읽기
image = cv2.imread('example.jpg')

# 이미지 축소
scaled_down = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

# 이미지 확대
scaled_up = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)

# 이미지 표시
cv2.imshow('Original Image', image)
cv2.imshow('Scaled Down', scaled_down)
cv2.imshow('Scaled Up', scaled_up)
cv2.waitKey(0)
cv2.destroyAllWindows()
