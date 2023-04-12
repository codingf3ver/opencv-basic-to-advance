import numpy as np
import cv2


def mouse_events(event,x,y,flags,param):

    # if event == cv2.EVENT_LBUTTONDOWN: 
    #    cv2.circle(img,(x,y),3,(0,0,255),-1)
    #    points.append((x,y))
    #    if len(points)>=2:
    #        cv2.line(img,points[-1],points[-2],(255,0,0),5)
    #    cv2.imshow('image',img)

    #  This part will print the color of particular coordinates
    if event == cv2.EVENT_LBUTTONDOWN: 
        blue = img[y,x,0]
        green  = img[y,x,1]
        red = img[y,x,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        color_image = np.zeros((720,1080,3),np.uint8)
        color_image[:] = [blue,green,red]
        cv2.imshow('color',color_image)
        if cv2.waitKey(0) & 0xFF == ord('u'):
            cv2.destroyWindow('color')


           
# img = np.zeros((720,1080,3),np.uint8)
img = cv2.imread('../images/pic1.jpeg',1)
cv2.imshow('image',img)
points = []
cv2.setMouseCallback('image',mouse_events)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
