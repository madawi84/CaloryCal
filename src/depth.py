# depth.py
# Handles depth estimation

import cv2
import numpy as np

class DepthEstimator:
    def __init__(self):
        # Placeholder (replace with Depth Anything V2 later)
        pass

    def estimate(self, image):
        # Create dummy depth map (same size as image)
        h, w = image.shape[:2]
        depth_map = np.ones((h, w))

        return depth_map