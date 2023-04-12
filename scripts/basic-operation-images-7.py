import numpy as np
import cv2

img = cv2.imread('../images/pic1.jpeg',1)
img2  = cv2.imread('../images/pic2.jpeg',1)

print(img.shape)
print(img.size)
print(img.dtype)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
pillow = img[584:1355,707:1537]
pillow = cv2.resize(img[584:1355,707:1537], (242, 136))
h, w = 136, 183
pillow_resized = cv2.resize(pillow, (w, h))
img[924:924+h, 1017:1017+w] = pillow_resized

img=  cv2.resize(img, (512,512))
img2 = cv2.resize(img2,(512,512))
merge = cv2.addWeighted(img,0.35,img2,0.65,0)
cv2.imshow('image',merge)


if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()