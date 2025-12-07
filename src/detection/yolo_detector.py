from ultralytics import YOLO

class YOLODetector:
    def __init__(self, model_path="../models/yolov8n.pt"):
        self.model = YOLO(model_path)
    
    def detect(self, image_path):
        return self.model(image_path)
