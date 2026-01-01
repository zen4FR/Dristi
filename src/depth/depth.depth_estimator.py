class DepthEstimator:
    def __init__(self):
        print("[DEPTH] Depth estimator initialized")

    def estimate(self, image_path):
        print(f"[DEPTH] Estimating depth for {image_path}")

        # Dummy depth info
        depth_info = {
            "nearest_object": "person",
            "distance": "near"
        }

        print(f"[DEPTH] Depth info: {depth_info}")
        return depth_info
