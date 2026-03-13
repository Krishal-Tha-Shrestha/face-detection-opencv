# Real-Time Face Detection System

Real-time face detection using Python, OpenCV and Android phone as camera via IP Webcam.

## Demo
![Face Detection Demo](demo.png)

## Libraries Used
- OpenCV
- NumPy
- urllib

## Setup
1. Install dependencies:
   pip install opencv-python numpy

2. Install **IP Webcam** app on Android phone

3. Open IP Webcam → tap **Start Server**

4. Replace IP address in script:
   url = "http://YOUR_IP:8080/shot.jpg"

5. Run:
   python detect.py

## How It Works
Uses Haar Cascade classifier with histogram equalization
for real-time face detection optimized for low-end hardware.

## Author
Krishal-Tha-Shrestha
