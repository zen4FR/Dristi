from detection.yolo_detector import YOLODetector
from depth.depth_estimator import DepthEstimator
from captioning.caption_model import CaptionModel
from fusion.fuse import fuse_results
from tts.speak import speak

def run(image_path):
    detector = YOLODetector()
    depth_model = DepthEstimator()
    captioner = CaptionModel()
    
    det = detector.detect(image_path)
    depth = depth_model.estimate(image_path)
    caption = captioner.caption(image_path)
    
    final_text = fuse_results(det, depth, caption)
    print(final_text)
    speak(final_text)

if __name__ == "__main__":
    run("../samples/input/test.jpg")
