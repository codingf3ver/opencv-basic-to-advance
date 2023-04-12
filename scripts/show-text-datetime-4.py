import cv2
from datetime import datetime

def add_text_in_live_video(cap):

    while (cap.isOpened()):
        ret,frame  = cap.read()

        if ret:
            # print width and heoght of the resolution
            print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            font = cv2.FONT_HERSHEY_SIMPLEX
            date_time = str(datetime.now())
            # gray video
            #  adding text or date time into the videos
            frame = cv2.putText(frame,date_time,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
            cv2.imshow('video demonstration by Tausif',frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    
if __name__ == "__main__": 
    cap = cv2.VideoCapture(0) 
    add_text_in_live_video(cap)
    cap.release()
    cv2.destroyAllWindows()   