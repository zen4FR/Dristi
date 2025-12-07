DRISTI: AI-Based Assistive Vision System
System Architecture Document
Semester Project – Kathmandu University
1. Overview

DRISTI is an assistive vision system designed to help visually impaired users understand their surroundings using computer vision and audio feedback.
For this semester, the system processes images (photos) instead of real-time video.
Next semester, the system will be extended to continuous video input.

    The system performs:

    1. Object Detection

    2. Depth Estimation

    3. Image Captioning

    4. Multimodal Fusion

    5. Text-to-Speech Output

All components are based on pretrained models to ensure feasibility within the semester timeframe.

2. High-Level Architecture
 ┌────────────────┐
 │  Image Input    │  <- photo captured by camera / uploaded
 └────────────────┘
          │
          ▼
 ┌────────────────┐
 │ Preprocessing  │  (resize, normalize, RGB → tensor)
 └────────────────┘
          │
          ▼
 ┌─────────────────────────┐
 │   Object Detector       │ YOLOv8
 │  (detection/)           │
 └─────────────────────────┘
          │
          ▼
 ┌─────────────────────────┐
 │   Depth Estimator       │ MiDaS / DepthAnything
 │   (depth/)              │
 └─────────────────────────┘
          │
          ▼
 ┌─────────────────────────┐
 │   Caption Generator     │ BLIP Transformer
 │    (captioning/)        │
 └─────────────────────────┘
          │
          ▼
 ┌─────────────────────────┐
 │   Fusion Engine         │ merges detections, depth, caption
 │     (fusion/)           │ into structured text
 └─────────────────────────┘
          │
          ▼
 ┌─────────────────────────┐
 │   Text-to-Speech (TTS)  │ Coqui TTS / OS TTS
 │       (tts/)            │
 └─────────────────────────┘
          │
          ▼
 ┌─────────────────────────┐
 │     Audio Output        │ plays final description to user
 └─────────────────────────┘


3. Component Description
3.1 Input Layer

Accepts a single image (.jpg, .png) from:

camera capture

file upload

Stored at samples/input/.

3.2 Preprocessing

Located in: src/utils/image_utils.py

Responsible for:

loading image with OpenCV

resizing to model-required resolution

normalizing pixel values

converting to tensor (PyTorch)

3.3 Object Detection (YOLOv8)

Located in: src/detection/yolo_detector.py

Model: YOLOv8n (lightweight, fast)
Outputs:

object classes

bounding boxes

confidence scores

Used for basic scene understanding.

3.4 Depth Estimation (MiDaS / DepthAnything)

Located in: src/depth/depth_estimator.py

Outputs:

pixel-wise depth map

approximate nearest object

relative distance (near, mid, far)

Helps user identify obstacles.

3.5 Captioning Model (BLIP)

Located in: src/captioning/caption_model.py

Model: BLIP (Bootstrapped Language-Image Pretraining)

Purpose:

Generate high-level descriptions

Provide context beyond object labels
Example:

“A man sitting in a living room with a table in front.”

3.6 Fusion Engine

Located in: src/fusion/fuse.py

Combines:

YOLO detections

Depth estimation

BLIP caption

Generates final structured description:

nearest object

position

caption

hazard information (if needed)

Example output:

“There is a chair 1.2 meters in front of you.
Scene appears to be an indoor room with a table and person.”

This step uses template-based NLG, not an LLM (lightweight and fast).

3.7 Text-to-Speech (TTS)

Located in: src/tts/speak.py

Two options:

Coqui TTS (offline)

System TTS (Windows/macOS built-in)

Outputs final speech audio:

Saved to samples/output/audio/

Played for user


4. Data Flow Diagram
Image → Preprocessing → YOLO → MiDaS → BLIP → Fusion → TTS → Audio
All intermediate outputs (JSON + annotated images) stored in:

samples/output/

5. Model Storage Structure
models/
│
├── yolov8n.pt
├── midas/
│   └── weights.pth
└── blip/
    └── model.bin


Models are pretrained and downloaded automatically when running the code.

6. Technologies Used
Component	Library / Model
Programming	Python 3.9+
CV Framework	PyTorch
Object Detection	YOLOv8
Depth Estimation	MiDaS / DepthAnything
Captioning	BLIP
Transformers	HuggingFace Transformers
Preprocessing	OpenCV
Fusion / NLG	Custom logic (Python)
Audio	Coqui TTS / OS TTS
7. Deployment Strategy
Phase 1 (This Semester)

Fully functional photo → audio pipeline

Evaluate accuracy and usability

Produce a working demo

Phase 2 (Next Semester)

Extend to real-time video pipeline

Add tracking

Add obstacle warnings

Optimize speed for mobile device

8. Conclusion

This architecture ensures:

practical development within the semester

clarity of components

easy future extension

complete alignment with the submitted proposal

DRISTI will deliver an efficient, modular, and expandable assistive vision system.