# SmartCCTVAlert

Overview
The CCTV Proximity Alert System is designed to monitor a CCTV feed and notify the owner if a human is detected within a specified threshold distance. It uses YOLO (You Only Look Once) for real-time object detection, calculates the distance between the detected human and the camera, and sends an alert via WhatsApp if the person is within the threshold distance.

Features
Real-time human detection using YOLO
Distance estimation between the human and the camera
Automated WhatsApp alert notification when the threshold distance is breached
Customizable distance threshold and alert settings
Prerequisites
Python 3.9 or later
Required Python libraries: opencv-python, ultralytics, pywhatkit
YOLO model weights file (e.g., yolov10n.pt)
Reference image with known width and distance

Installation

1.Clone the repository
https://github.com/Inbaselvan-ayyanar/SmartCCTVAlert.git

cd SmartCCTVAlert

2.Install required packages
pip install -r requirements.txt

3.Download YOLO model weights:

4.Download the YOLOv5 model weights (e.g., yolov10n.pt) and place them in the project directory.
Configure your WhatsApp number:

Edit the notification.py file to include your WhatsApp phone number.

Usage

->Prepare a reference image:

       Ensure you have a reference image (img.jpg) with a known width and distance to calibrate the focal length.

->Run the script:
       
       python main.py
       

Configuration

->known_width: Enter the actual width of the person in the reference image.

->known_distance: Enter the actual distance between the person and the camera in the reference image.

->threshold_distance: Set the distance threshold in centimeters for triggering alerts.

Troubleshooting

->Ensure that your webcam is working properly.

->Verify that the YOLO model weights file is correctly downloaded and placed in the project directory.

->Make sure your WhatsApp number is correctly configured in the notification.py file.

->Ensure the reference image path is specified properly with the correct calculaion of the person width and dustance between camera and human


Contact
For any questions or issues, please contact [a.inbaselvan@gmail.com].


