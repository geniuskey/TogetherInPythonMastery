# 샘플 이미지 사용을 위해 `pip install scikit-image` 필요
import cv2
from skimage import data

# 얼굴 인식기 로드 (haarcascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 이미지 읽기
bgr_image = data.astronaut()   # 이 부분은  `cv2.imread('example.jpg')` 로 대체 가능합니다.
image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)

# 얼굴 인식
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 얼굴 주변에 사각형 그리기
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# 이미지 표시
cv2.imshow('Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
