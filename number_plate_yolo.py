from ultralytics import YOLO
import cv2
import easyocr

# YOLO model load
model = YOLO("yolov8n.pt")

# OCR reader
reader = easyocr.Reader(['en'])

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))

    results = model(frame)

    for r in results:

        boxes = r.boxes.xyxy

        for box in boxes:

            x1, y1, x2, y2 = map(int, box)

            plate = frame[y1:y2, x1:x2]

            if plate.size == 0:
                continue

            text = reader.readtext(plate)

            for t in text:

                plate_number = t[1]

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                cv2.putText(frame, plate_number,
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2)

                print("Plate:", plate_number)

    cv2.imshow("Plate Detection", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()