# DRISTI — AI-Based Assistive Vision System

**Semester project — Kathmandu University**

DRISTI helps visually impaired users understand their surroundings by converting an input **photo** into a spoken description using computer vision and lightweight transformer models.

---

## 🔎 Project Summary

- **Input:** single image (photo)  
- **Pipeline:** object detection (YOLOv8) → depth estimation (MiDaS) → image captioning (BLIP) → fusion → text-to-speech  
- **Output:** short spoken description + optional annotated image and JSON output  
- **Semester scope:** Photo-only MVP. Video/real-time will be implemented in a future semester.

---

## 🚀 Features

- Fast object detection with **YOLOv8**  
- Relative depth estimation using **MiDaS / DepthAnything**  
- Scene captioning via **BLIP** (Vision + Transformer)  
- Lightweight fusion engine (template-based NLG) — no large LLM required  
- Text-to-speech via **Coqui TTS** or system TTS  
- Modular code structure for easy extension

---

## 📁 Repository Structure
dristi/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│ ├── main.py
│ ├── detection/yolo_detector.py
│ ├── depth/depth_estimator.py
│ ├── captioning/caption_model.py
│ ├── fusion/fuse.py
│ ├── tts/speak.py
│ └── utils/image_utils.py
├── models/ # (ignored in git) pretrained weights
├── samples/
│ ├── input/
│ └── output/
├── docs/
│ └── architecture.md
└── notebooks/


---

## ⚙️ Quick Setup

> Tested on Python 3.9+. Use a virtual environment.

```bash
# 1. Clone repository
git clone https://github.com/<your-username>/dristi.git
cd dristi

# 2. Create & activate venv
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

Requirements (example):
ultralytics
torch
torchvision
opencv-python
transformers
timm
numpy
coqui-tts



🧠 Design / Architecture

See docs/architecture.md for the full architecture description, data flow diagram, and deployment plan.
Short flow:
Image → Preprocessing → YOLOv8 → MiDaS → BLIP → Fusion → TTS → Audio