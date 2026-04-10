# Cone Detection using YOLOv8

## Overview
The project implements cone detection using YOLOv8. Given a dataset of cones, the project distinguishes between orange, blue and yellow cones (also distinguishes between regular and large orange cones).
The project can train the model from scratch while also being able to use pretrained weights and resume training from a certain block of progress.
The project draws a rectangle with the cone's color and confidence score (from 0 to 1).

Operating System: Windows 11

## Installation and Setup

### Prerequisites

1. Python 3.12
2. Git

### Steps

1. Clone this repository:
   
   ```bash
   git clone https://github.com/lior4715/Cone-Detection
   ```
   
2. Install required dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```

### Datasets

1. Dataset sourced from Roboflow.
2. Contains labeled images of traffic cones (blue, orange, and yellow classes).
3. Ensure the dataset is placed in the datasets directory.

## Run instructions

### Training

To train the model copy the code:
```bash
python scripts/train.py
```
Ensure the dataset is configured properly in datasets/data.yaml and according to the project structure below.

### Inference

To perform an inference on a video, copy the code:
```bash
python scripts/inference.py
```

### Project Structure

```plaintext
BGRacing/
├── datasets/
│   ├── train/
│   ├── valid/
│   └── data.yaml
├── runs/
├── scripts/
│   ├── train.py
│   └── inference.py
├── videos/
|   └── fsd1.mp4
└── README.md
```

### Results

Video from the type .avi will start running when the inference is ran. Example video of the result is in:
```plaintext
runs/detect/predict/fsd1.avi
```

## Approach

### Self-learning

I, as a year 1 CS student, didn't have any idea on how to create this project and make this assignment.
At first I started using ChatGPT and asked for directions. He recommended using Python and YOLOv8 model due to the project being relatively small.
I started learning Python basics that are necessary for this project and came back to this project while learning over time some more.
Eventually, I started installing the dependencies and had a hard time completing it. Each dependency created its own problem but in the end, found a way to get them to work.

## Project

### 1. Dataset Preparation:
   Used Roboflow to get a dataset that distinguishes between color, downloaded it to my project.
   Using this data, I acquired traffic cone images of different colors and the labels that fit to their size.


### 2. Model Training:
   For training, I used YOLOv8n (nano), which a smaller model compared to the default model of YOLOv8. I chose it mainly because of the "lacking" hardware that im     working on. Since I have no available GPUs to use, I had to use the nano model for faster training.
   Adjusted confidence threshold to improve precision.


### 3. Inference:
   Conducted object detection on example videos.
