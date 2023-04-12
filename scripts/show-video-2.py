import cv2


def show_video(cap,output):

    while (cap.isOpened()):
        ret,frame  = cap.read()
        # ret boolean value
        if ret:

            print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            output.write(frame)
            # color live video
            # cv2.imshow('frame',frame)
            # gray video
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame',gray)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'h264')
    output  = cv2.VideoWriter('../images/video_output.mp4',fourcc,20,(1280,720))
    show_video(cap,output)
    cap.release()
    output.release()
    cv2.destroyAllWindows()
