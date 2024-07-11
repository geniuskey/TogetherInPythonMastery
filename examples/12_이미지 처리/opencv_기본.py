import cv2

# 이미지 읽기
image = cv2.imread('example.jpg')

# 이미지 표시
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 이미지 저장
cv2.imwrite('output.jpg', image)
