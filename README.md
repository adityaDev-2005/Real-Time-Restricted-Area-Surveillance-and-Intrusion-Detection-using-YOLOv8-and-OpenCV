# SentinelAI: Real-Time Restricted Area Surveillance and Intrusion Detection using YOLOv8 and OpenCV

## Overview

SentinelAI is an AI-powered surveillance system developed using YOLOv8 and OpenCV for real-time monitoring of restricted areas. The system detects human presence, tracks individuals entering predefined regions of interest (ROI), and generates alerts when an intrusion is detected.

The project demonstrates how modern computer vision techniques can be applied to defense, security, and industrial surveillance applications.

---

## Features

* Person detection using YOLOv8
* Video-based surveillance
* Person counting
* Region of Interest (ROI) monitoring
* Intrusion detection
* Dynamic color-coded bounding boxes
* Intruder count inside ROI
* Status monitoring (SAFE / PERSON DETECTED / INTRUSION DETECTED)
* Automatic screenshot capture upon intrusion
* Intrusion logging with timestamps
* Person count logging

---

## System Workflow

Video Input

↓

YOLOv8 Person Detection

↓

Bounding Box Generation

↓

Center Point Calculation

↓

ROI Validation

↓

Intrusion Detection

↓

Alert Generation

↓

Screenshot Capture

↓

Log Storage

---

## Technologies Used

* Python
* OpenCV
* Ultralytics YOLOv8
* NumPy
* Datetime
* Time module

---

## Detection States

### SAFE

No people are detected.

### PERSON DETECTED

People are present but remain outside the restricted area.

### INTRUSION DETECTED

One or more individuals enter the predefined restricted region.

---

## Output

The system displays:

* Person count
* Intruder count
* System status
* Restricted area overlay
* Bounding boxes around detected persons
* Center points for ROI validation

Upon intrusion:

* A screenshot is automatically saved.
* Intrusion information is recorded inside `intrusion_log.txt`.

Person counts are periodically recorded inside `person_log.txt`.

---

## Applications

* Defense surveillance systems
* Military perimeter monitoring
* Restricted area protection
* Industrial safety monitoring
* Smart CCTV systems
* Border surveillance
* Warehouse security
* Campus security

---

## Future Improvements

* Object tracking using DeepSORT or ByteTrack
* Loitering detection
* Motion anomaly detection
* Weapon detection with custom YOLO models
* Face recognition and authorization
* Email and Telegram alerts
* Real-time dashboard
* Multi-camera monitoring
* Database integration
* Web deployment using FastAPI
* Audio alarms and notifications

---

## Project Structure

```text
SentinelAI/
│
├── main.py
├── street_people.mp4
├── intrusion_log.txt
├── person_log.txt
├── intrusion_YYYYMMDD_HHMMSS.jpg
├── requirements.txt
└── README.md
```

---

## Author

Aditya Mishra

B.Tech (Information Technology)

Interests:

* Computer Vision
* Machine Learning
* Reinforcement Learning
* Robotics
* Autonomous Systems
* AI for Defense Applications

We can expect this as output : 
<img width="1291" height="812" alt="image" src="https://github.com/user-attachments/assets/71aaaec4-a175-4070-80ab-5f331ee55472" />

