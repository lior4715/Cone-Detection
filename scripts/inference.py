import os
from pathlib import Path
from ultralytics import YOLO

# Resolve project root (one level up from scripts/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

RUN_NAME = "new_training"
WEIGHTS_PATH = PROJECT_ROOT / "runs" / "detect" / RUN_NAME / "weights" / "best.pt"

if not WEIGHTS_PATH.exists():
    raise FileNotFoundError(
        f"Missing trained weights: '{WEIGHTS_PATH}'. Run scripts/train.py first."
    )

model = YOLO(str(WEIGHTS_PATH))

# Run inference on a video
results = model.predict(
    source=str(PROJECT_ROOT / "videos" / "fsd1.mp4"),
    save=True,
    show=True,
    conf=0.25,
)
