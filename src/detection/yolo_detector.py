class YOLODetector:
    def __init__(self):
        print("[YOLO] Detector initialized")

    def detect(self, image_path):
        print(f"[YOLO] Running detection on {image_path}")

        # Dummy detection result
        detections = [
            {"label": "person", "position": "center"},
            {"label": "chair", "position": "front"}
        ]

        print(f"[YOLO] Detected objects: {detections}")
        return detections
