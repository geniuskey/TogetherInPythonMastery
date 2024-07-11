import cv2

# 웹캠 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)

# 첫 프레임에서 객체 선택
ret, frame = cap.read()
bbox = cv2.selectROI('Webcam - Select Object', frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow('Webcam - Select Object')

# CSRT 추적기 생성 및 초기화
tracker = cv2.TrackerCSRT_create()
tracker.init(frame, bbox)

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    # 프레임이 정상적으로 읽히지 않으면 종료
    if not ret:
        break

    # 객체 추적
    success, bbox = tracker.update(frame)

    # 객체가 추적되면 사각형 그리기
    if success:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # 프레임 표시
    cv2.imshow('Webcam - Object Tracking', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 비디오 캡처 객체 해제 및 윈도우 닫기
cap.release()
cv2.destroyAllWindows()
