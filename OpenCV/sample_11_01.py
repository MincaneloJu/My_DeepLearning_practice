import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def equahist_demo(image):
    gray = cv.cvtColor(image ,cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("equahist_demo" ,dst)

def clahe_demo(image):
    gray = cv.cvtColor(image ,cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2 , tileGridSize=(8 ,8))
    dst = clahe.apply(gray)
    cv.imshow("clahe_demo" ,dst)



print("------------Hello Python------------")
src = cv.imread("e:/PyAI/image/IZONE_Gray.jpg", cv.IMREAD_COLOR)
#crc = cv.imread("e:/PyAI/image/images.jpg", cv.IMREAD_COLOR)

cv.namedWindow("Input Image", cv.WINDOW_AUTOSIZE)
#cv.namedWindow("Input Image2" ,cv.WINDOW_AUTOSIZE)

cv.imshow("Input Image", src)
#cv.imsh)ow("Input Image2" ,crc)

equahist_demo(src)
clahe_demo(src)

while True:
    if (cv.waitKey(100) == 27):
        break
# cv.waitKey(0)
cv.destroyAllWindows()