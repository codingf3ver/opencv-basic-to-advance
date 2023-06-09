import numpy as np
import cv2

def mouse_events(event,x,y,flags,param):

    #  left mouse click will give you the coordinates
    if event == cv2.EVENT_LBUTTONDOWN: 
        print(x,', ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x,y), font, 1.5, (255,255,0),2)
        cv2.imshow('image',img)

    # right click will give you the rgb of the points
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green  = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', '+str(red)
        cv2.putText(img, strBGR, (x,y), font, 1.5, (0,255,0),2)
        cv2.imshow('image',img)

           
if __name__ == "__main__":

    events =  [ i for i in dir(cv2) if 'EVENT' in i]
    #    print(events)
    # img = np.zeros((720,1080,3),np.uint8)
    img = cv2.imread('../images/pic1.jpeg',1)
    cv2.imshow('image',img)

    cv2.setMouseCallback('image',mouse_events)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
