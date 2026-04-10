import os
from pathlib import Path
from ultralytics import YOLO

# Resolve project root (one level up from scripts/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

RUN_NAME = "new_training"
CHECKPOINT_PATH = PROJECT_ROOT / "runs" / "detect" / RUN_NAME / "weights" / "best.pt"
DATA_YAML = PROJECT_ROOT / "datasets" / "data.yaml"

# Resume only when a valid checkpoint already exists.
if CHECKPOINT_PATH.exists():
    model = YOLO(str(CHECKPOINT_PATH))
else:
    model = YOLO(str(PROJECT_ROOT / "yolov8n.pt"))

model.train(
    data=str(DATA_YAML),
    epochs=50,
    imgsz=640,
    project=str(PROJECT_ROOT / "runs" / "detect"),
    name=RUN_NAME,
    exist_ok=True,
    resume=CHECKPOINT_PATH.exists(),
)
