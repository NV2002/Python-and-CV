import cv2
import numpy as np

video = cv2.VideoCapture("Bootcamp/Green.mp4")
image = cv2.imread("Bootcamp/bgimg.jpg")

while True:
    ret,frame = video.read()
    frame = cv2.resize(frame,(640,480))
    image = cv2.resize(image,(640,480))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_g = np.array([32,94,132])
    u_g = np.array([179,255,255])

    mask = cv2.inRange(hsv,l_g,u_g)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    final = frame-res
    green_screen = np.where(final==0,image,final)
    cv2.imshow("Video",green_screen)
    key = cv2.waitKey(5)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()