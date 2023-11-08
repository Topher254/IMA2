from ultralytics import YOLO
import cv2
import pyttsx3
import cvzone

engine = pyttsx3.init()
# create model
model = YOLO('yolov8l.pt')
classNames = [
    "Person", "chair", "staircase", "water", "pit"
]


def detect(file):
    imeji = cv2.imread(file,cv2.IMREAD_COLOR)
    results= model(imeji, stream=True)
    # stream uses generators; check for individual boxes
    for r in results:
        boxes = r.boxes
        # loop through
        for box in boxes:
            # find x and y coordinates
            x1,y1,x2,y2 = box.xyxy[0]
            a = int(x1) 
            b = int(y1)
            c = int(x2)
            d = int(y2)

            print("cordinates are",int(x1),int(y1),int(x2),int(y2))
            # lets create a rectangle bounded by this cordinates
            # cv2.rectangle(img,((x1,y1)),(0,255,0),3)
            cv2.rectangle(imeji,(a,b),(c,d),(0,255,0),3)
            

            # percentage confidence values
            confidence = round(box.conf[0].item(),2)
            confidence_display = str(confidence)
            font = cv2.FONT_HERSHEY_PLAIN
            # cv2.putText(img,confidence_display,(a,b),font,2,(255,0,0),3)
            # cvzone.putTextRect(img,confidence_display,(a,b))
            

            # classes
            class_id = box.cls[0].item()
            class_0 = 'Person'
            class_1 = 'Bicyle'
            class_2 = 'Car'
            class_56 = 'Chair'

            # BACKGROUND OF TEXT
            # not working
            rect_bgr = (77,26,120)
            # cv2.rectangle(img,(a,a+20),(b,b+20),(255,0,0),3)

            print("Class",class_id)
            print("confidence",confidence)
            print("-----")
                
            text_color = (255,0,255)
            if class_id == 0:
                texta = f"{class_0}_{confidence_display}"
                cv2.putText(imeji,texta,(a,b),font,2,text_color,3)
                engine.say("Person detected")
                engine.runAndWait()
            elif class_id == 1:
                texta = f"{class_1}_{confidence_display}"
                engine.say("Bicycle detected")
                engine.runAndWait()

            elif class_id == 3:
                texta = f"{class_2}_{confidence_display}"
                engine.say("Vehicle detected")
                engine.runAndWait()
            elif class_id == 56:
                texta = f"{class_56}_{confidence_display}"
                engine.say("Chair detected")
                engine.runAndWait()
            else:
                engine.say("Nothing in image")
                engine.runAndWait()