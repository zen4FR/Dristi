def fuse_results(detections, depth_info, caption):
    print("[FUSION] Fusing results")

    nearest = depth_info.get("nearest_object", "object")
    distance = depth_info.get("distance", "some distance")

    objects = ", ".join([obj["label"] for obj in detections])

    final_sentence = (
        f"{caption} "
        f"There is a {nearest} {distance} in front of you. "
        f"Detected objects include: {objects}."
    )

    return final_sentence
