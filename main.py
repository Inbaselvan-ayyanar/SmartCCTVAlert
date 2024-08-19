import cv2
import time
from ultralytics import YOLO
from notification import alert

model = YOLO("yolov10n.pt") # load the yolo model

#find the focal length of the camera
def focal_length_finder(known_distance,image_width,known_width):

    return (known_distance*image_width)/known_width

#find the distance between the human and camera
def distance_finder(focal_length,image_width,known_width):

    return (focal_length*known_width)/image_width


def width_finder (image):
    
    width=0
    results =model(image)
    for result in results:
        for bbox in result.boxes:
            if bbox.cls==0:
                x1,y1,x2,y2=bbox.xyxy[0].int().tolist()
                width = x2-x1
                break
    return width

def main():
    
    reference_image= cv2.imread("img.jpg") #Replace the path with your reference image

    known_width=60 #Enter the actual width of the person in the reference image
    known_distance= 200 # Enter the actual distance between the person and the camera

    reference_image_width= width_finder(reference_image)

    result = model(reference_image)
    
    #calculate the focal length using the reference image
    focal_length= focal_length_finder(known_distance,reference_image_width,known_width)
    

    cap=cv2.VideoCapture(0)
    threshold_distance=200  #Distance threshold in cm


    while True:
        ret,frame=cap.read()
        if not ret:
            break
        results=model.predict(frame)

        
        for result in results:
            boxes=result.boxes.xyxy.numpy()
            scores=result.boxes.conf.numpy()
            class_id=result.boxes.cls.numpy().astype(int)
            
          
            for i, box in enumerate(boxes):

                
                if scores[i] > 0.8  and model.names[class_id[i]] == "person":
                    x1, y1, x2, y2 = map(int, box)
                    label = model.names[class_id[i]]
                    distance=distance_finder(focal_length,int(x2-x1),known_width)

                    if distance< threshold_distance:
                        cv2.putText(frame, f"{label} lesser than threshold distance - {round(distance, 2)} cm", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                        alert(frame)#notifing the owner
                        time.sleep(180)

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"{label} - {round(distance, 2)} cm", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("Human Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()