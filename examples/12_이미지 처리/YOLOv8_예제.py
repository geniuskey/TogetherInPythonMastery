import cv2
from ultralytics import YOLO

# YOLOv8 모델 로드
model = YOLO('yolov8n.pt')  # yolov8n.pt: YOLOv8 모델 파일

# 웹캠 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    # 프레임이 정상적으로 읽히지 않으면 종료
    if not ret:
        break

    # YOLOv8을 사용하여 객체 감지
    results = model(frame)

    # 결과에서 바운딩 박스와 레이블 추출
    for result in results:
        # results[0].boxes.xyxy 는 (N, 4) 모양의 바운딩 박스 좌표
        # results[0].boxes.conf 는 (N, 1) 모양의 신뢰도
        # results[0].boxes.cls 는 (N, 1) 모양의 클래스 ID
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            confidence = box.conf[0]
            class_id = int(box.cls[0])

            # 바운딩 박스 그리기
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            label = f"{model.names[class_id]}: {confidence:.2f}"
            cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 프레임 표시
    cv2.imshow('YOLOv8 - Real-time Object Detection', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 비디오 캡처 객체 해제 및 윈도우 닫기
cap.release()
cv2.destroyAllWindows()
