class CaptionModel:
    def __init__(self):
        print("[CAPTION] Caption model initialized")

    def caption(self, image_path):
        print(f"[CAPTION] Generating caption for {image_path}")

        # Dummy caption
        caption = "A person sitting on a chair indoors."

        print(f"[CAPTION] Caption: {caption}")
        return caption
