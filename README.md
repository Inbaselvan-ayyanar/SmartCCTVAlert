# SmartCCTVAlert


Overview
A project that uses the CCTV feed and has the capability of alerting the owner in case of a human threshold detection. This distance metric gives the distance between the detected human and the camera with regard to real-time object detection via YOLO (You Only Look Once) and sends an alert via WhatsApp if the person is in the threshold distance.

Features

->Real-time human detection via YOLO

->Distance estimation between the human and the camera

->Automated WhatsApp alert notification when the threshold distance is breached

->Customizable distance threshold and alert settings


Prerequisites

->Python 3.9 or later

->Required Python libraries: opencv-python, pywhatkit

->YOLO model weights file, e.g. yolov10n.pt

->Reference image with known width and distance

Installation

1.Clone the repository
https://github.com/Inbaselvan-ayyanar/SmartCCTVAlert.git

cd SmartCCTVAlert

2. Install required packages
pip install -r requirements.txt

3. Download YOLO model weights:

4. Download YOLO

Edit WhatsApp's phone number in notification.py

 Usage

 -> Prepare a reference image:
    

       Ensure you have the reference image whose both width and distance values are known to calibrate the focal length.
     
 -> Run the script:
          Execute the script with the following command:
 
         python main.py
     

 Configuration

-> known_width : Here you have to enter the real width of a person's face.

-> known_distance : Here, you have to enter the actual distance of a person from the camera.

-> threshold_distance : It is the minimum distance of a person from the camera to avoid unnecessary alarm trigger.

Troubleshooting:

-> Ensure That Your Webcam Is Properly Working.

-> Ensure That The Yolo Model Weights File Is Downloaded And Placed In The Project Directory.

-> Ensure That The WhatsApp Number Is Proper In The notification. py File.

-> Make sure the reference image path is specified properly for the person width and distance between camera and human

Contact
For any questions or issues, please contact [a.inbaselvan@gmail.com].


