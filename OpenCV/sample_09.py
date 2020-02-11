import cv2 as cv
import numpy as np


def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0 :
        return 0
    else:
        return pv

def gaussian_noise(image):
    h ,w ,c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0 ,20 ,3)
            b = image[row ,col ,0]
            g = image[row ,col ,1]
            r = image[row ,col ,2]
            image[row ,col ,0] = clamp(b + s[0])
            image[row ,col ,1] = clamp(g + s[1])
            image[row ,col ,2] = clamp(r + s[2])
    cv.imshow("gaussian_noise" ,image)

print("------------Hello Python------------")
src = cv.imread("e:/PyAI/image/minju1.jpg", cv.IMREAD_COLOR)
#crc = cv.imread("e:/PyAI/image/TnTaxDl.jpg", cv.IMREAD_COLOR)

cv.namedWindow("Input Image", cv.WINDOW_AUTOSIZE)
# cv.namedWindow("Input Image2" ,cv.WINDOW_AUTOSIZE)

cv.imshow("Input Image", src)
# cv.imshow("Input Image2" ,crc)

gaussian_noise(src)

while True:
    if (cv.waitKey(100) == 27):
        break
# cv.waitKey(0)
cv.destroyAllWindows()