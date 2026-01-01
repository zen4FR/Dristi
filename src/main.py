from src.detection.yolo_detector import YOLODetector
from src.depth.depth_estimator import DepthEstimator
from src.captioning.caption_model import CaptionModel
from src.fusion.fuse import fuse_results
from src.tts.speak import speak


def run(image_path):
    print("=== DRISTI SYSTEM STARTED ===")

    detector = YOLODetector()
    depth_model = DepthEstimator()
    captioner = CaptionModel()

    detections = detector.detect(image_path)
    depth_info = depth_model.estimate(image_path)
    caption = captioner.caption(image_path)

    final_text = fuse_results(detections, depth_info, caption)

    print("\nFINAL OUTPUT:")
    print(final_text)

    speak(final_text)


if __name__ == "__main__":
    run("samples/input/test.jpg")
