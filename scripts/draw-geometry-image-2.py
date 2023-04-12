import cv2

img = cv2.imread('images/pic2.jpeg',1)

img  = cv2.line(img,(0,0),(255,255),(255,0,0),15)
cv2.imshow('image',img)


if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

