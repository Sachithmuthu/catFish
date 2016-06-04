import numpy as np
import cv2
from data_excel import*

data=data_excel()

cap = cv2.VideoCapture('/home/sachith/safe/cctv.mp4')

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
fgbg = cv2.createBackgroundSubtractorMOG2(0,0,False)

params = cv2.SimpleBlobDetector_Params()

#params.minThreshold = 10;
#params.maxThreshold = 255;

params.filterByArea = True
params.minArea = 700
#params.maxArea = 1000    <<<<<<<<<<<<<<<<<-------------

params.filterByCircularity = False
params.minCircularity = 0.2

params.filterByConvexity = False
params.minConvexity = 0.87

params.filterByInertia = False
params.minInertiaRatio = 0.01


ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else : 
    detector = cv2.SimpleBlobDetector_create(params)

while(1):
    ret, frame = cap.read()

    image = fgbg.apply(frame,learningRate=0.02)
    
    points = detector.detect(image)
    blob_image = cv2.drawKeypoints(frame, points, np.array([]), (255,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    for kp in points :
        x=round(kp.pt[0])
        y=round(kp.pt[1])
        print "[x=%d,y=%d]" %(x,y)
        data.writeExcel(x,y)
    #--------------------------------------------------------------------------------------------------------------------------------    
    #cv2.imshow('frame',image)
    cv2.imshow('frame',blob_image)

    if cv2.waitKey(1) & 0xFF == ord('z'):
        break

cap.release()
cv2.destroyAllWindows()
