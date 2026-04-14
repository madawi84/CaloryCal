# segmentation.py
# Handles food detection and segmentation using YOLO

from ultralytics import YOLO

class FoodSegmenter:
    def __init__(self, model_path):
        # Load trained YOLO model
        self.model = YOLO(model_path)

    def predict(self, image_path):
        # Run inference
        results = self.model(image_path)
        return results[0]