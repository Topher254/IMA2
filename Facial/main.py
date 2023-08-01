from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')
results = model('1.jpg',show=True)

cv2.imshow("wewe",results)
cv2.waitKey(100000)
cv2.destroyAllWindows()

