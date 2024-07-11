import cv2

# 웹캠 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    # 프레임이 정상적으로 읽히지 않으면 종료
    if not ret:
        break

    # 그레이스케일 필터 적용
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 가우시안 블러 필터 적용
    blurred = cv2.GaussianBlur(frame, (15, 15), 0)

    # 프레임 표시
    cv2.imshow('Webcam - Original', frame)
    cv2.imshow('Webcam - Grayscale', gray)
    cv2.imshow('Webcam - Blurred', blurred)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 비디오 캡처 객체 해제 및 윈도우 닫기
cap.release()
cv2.destroyAllWindows()
