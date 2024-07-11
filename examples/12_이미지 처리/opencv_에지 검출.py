import cv2

# 이미지 읽기
image = cv2.imread('example.jpg')

# 그레이스케일 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 에지 검출
edges = cv2.Canny(gray_image, 50, 150)

# 이미지 표시
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
