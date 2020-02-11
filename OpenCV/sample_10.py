import cv2 as cv
import numpy as np

def bi_image(image):
    dst = cv.bilateralFilter(image ,0 ,85 ,10)
    cv.imshow("bi_image" ,dst)

def mean_shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image ,10 ,50)
    cv.imshow("mean_shift_demo" ,dst)


print("------------Hello Python------------")
src = cv.imread("e:/PyAI/image/minju1.jpg", cv.IMREAD_COLOR)
crc = cv.imread("e:/PyAI/image/images.jpg", cv.IMREAD_COLOR)

cv.namedWindow("Input Image", cv.WINDOW_AUTOSIZE)
cv.namedWindow("Input Image2" ,cv.WINDOW_AUTOSIZE)

cv.imshow("Input Image", src)
cv.imshow("Input Image2" ,crc)


bi_image(crc)
mean_shift_demo(crc)

while True:
    if (cv.waitKey(100) == 27):
        break
# cv.waitKey(0)
cv.destroyAllWindows()