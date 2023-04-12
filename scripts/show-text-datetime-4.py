import cv2
from datetime import datetime
cap = cv2.VideoCapture(0)


while (cap.isOpened()):
    ret,frame  = cap.read()
 
    if ret:

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        font = cv2.FONT_HERSHEY_SIMPLEX
        date_time = str(datetime.now())
        # gray video
        frame = cv2.putText(frame,date_time,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('video demonstration by Tausif',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
