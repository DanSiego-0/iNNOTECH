import cv2 
import numpy as np

# Path to config and weight
PATH_TO_CONFIG = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
PATH_TO_WEIGHT = 'frozen_inference_graph.pb'

cap = cv2.VideoCapture(0) # 0 stands for webcam placement in the usb port
cap.set(3,640)
cap.set(4,480)

# Import class names 
classNames = []
classList = 'coco.names'

# Import class names to classNames
with open(classList,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Get ids and names detected 
net = cv2.dnn_DetectionModel(PATH_TO_WEIGHT,PATH_TO_CONFIG)
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)

while True:
    success,img = cap.read()
    classIDs, confidence, bbox = net.detect(img,confThreshold = 0.5)

    print(classIDs,bbox)

    if len(classIDs) != 0:
    # Identify object 
        for classID, confi,box in zip(classIDs.flatten(),confidence.flatten(),bbox):
            cv2.rectangle(img,box,color=(0,255,0),thickness=3)
            cv2.putText(img,classNames[classID-1],(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)

    cv2.imshow("Img",img)
    cv2.waitKey()