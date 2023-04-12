import cv2

img = cv2.imread('images/pic2.jpeg',0)
cv2.imshow('image',img)

key  = cv2.waitKey(5000)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('images/pic2_copy.png',img)
    cv2.destroyAllWindows()