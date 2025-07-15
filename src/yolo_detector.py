import os
import json
from ultralytics import YOLO
import cv2

IMAGE_DIR = "data/raw/telegram_messages/images"
OUTPUT_JSON = "data/raw/yolo_detections.json"

# Load model
model = YOLO("yolov8n.pt")  # You can use yolov8s.pt or yolov8m.pt for better accuracy

def run_detection():
    results = []
    for filename in os.listdir(IMAGE_DIR):
        if filename.lower().endswith(('.jpg', '.png')):
            filepath = os.path.join(IMAGE_DIR, filename)
            detections = model(filepath)[0]
            for box in detections.boxes:
                result = {
                    "image_file": filename,
                    "class_id": int(box.cls[0]),
                    "class_name": model.names[int(box.cls[0])],
                    "confidence": float(box.conf[0]),
                    "bbox": [float(x) for x in box.xyxy[0].tolist()]
                }
                results.append(result)

    with open(OUTPUT_JSON, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"✅ YOLO detections saved to {OUTPUT_JSON}")
