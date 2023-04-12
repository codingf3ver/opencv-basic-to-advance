import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'h264')
out  = cv2.VideoWriter('images/video_output.mp4',fourcc,20,(1280,720))

while (cap.isOpened()):
    ret,frame  = cap.read()

    # ret boolean value
    
    if ret:

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)
        # color live video
        # cv2.imshow('frame',frame)

        # gray video
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
