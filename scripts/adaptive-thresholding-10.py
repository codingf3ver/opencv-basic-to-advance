import  cv2


def adaptive_thresholding():

    _, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2);
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2);

    cv2.imshow("Image", img)
    cv2.imshow("THRESH_BINARY", th1)
    cv2.imshow("ADAPTIVE_THRESH_MEAN_C", th2)
    cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

if __name__ =="__main__":
    img = cv2.imread('../images/pic1.jpeg',0)
    adaptive_thresholding()