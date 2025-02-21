from ultralytics import YOLO
import torch
import cv2
import time

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

model = YOLO("yolov8x.pt").to(device)
cap = cv2.VideoCapture("Traffic1.mp4")

# Set frame dimensions
frame_width = 640
frame_height = 480

class_names = model.names  # Predefined COCO dataset classes

# FPS calculation
prev_time = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (frame_width, frame_height))
    start_time = time.time()  # Start time for FPS calculation

    # Object detection
    results = model(frame, device=device)
    
    vehicle_count = 0  

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
            class_id = int(box.cls[0])  # Class ID
            conf = box.conf[0].item()  # Confidence score
            
            # Consider only vehicle-related classes (car, truck, bus, motorcycle)
            if class_names[class_id] in ["car", "truck", "bus", "motorcycle"]:
                vehicle_count += 1
                color = (0, 255, 0)  # Green for vehicles
            else:
                color = (255, 0, 0)  # Blue for other objects

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            
            # Add label with class name and confidence score
            label = f"{class_names[class_id]} {conf:.2f}"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Calculate FPS
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    # Display vehicle count & FPS
    cv2.putText(frame, f"Vehicles: {vehicle_count}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.putText(frame, f"FPS: {fps:.2f}", (20, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

    cv2.imshow("Traffic Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
    

