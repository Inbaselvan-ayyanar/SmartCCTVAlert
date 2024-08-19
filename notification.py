import cv2
import pywhatkit
import datetime


def alert(img):

    date = datetime.datetime.now()
    date.strftime("%c")
    picture="captured_Image.jpg"
    cv2.imwrite(picture,img)
    if not picture:
        return
    phone_number = "+91" #Modify the owner number
    caption = f"alert at {date}"

    pywhatkit.sendwhats_image(phone_number, picture, caption)
   

    


