import os
import uuid
import cv2
import time

# folder for images and path
IMAGES_PATH = os.path.join('data','images')
number_of_images = 20

# capture from camera
capture = cv2.VideoCapture(0)
for imgnum in range(number_of_images):
    print("Collecting image ", imgnum)
    ret, frame = capture.read()
    imgname = os.path.join(IMAGES_PATH,f'{str(uuid.uuid1())}.jpg')
    cv2.imwrite("img.png",frame)
    cv2.imshow('frame',frame)
    time.sleep(0.5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()

