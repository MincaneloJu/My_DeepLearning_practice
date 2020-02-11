import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def plot_demo(image):
    plt.hist(image.ravel() ,256 ,[0 ,256])
    plt.show("直方圖")


def image_hist(image):
    color = ("blue" ,"green" ,"red")
    for i ,color in enumerate(color):
        hist = cv.calcHist([image] ,[i] ,None ,[256] ,[0 ,256])
        plt.plot(hist ,color = color)
        plt.xlim([0 ,256])
    plt.show()

print("------------Hello Python------------")
src = cv.imread("e:/PyAI/image/minju1.jpg", cv.IMREAD_COLOR)
#crc = cv.imread("e:/PyAI/image/images.jpg", cv.IMREAD_COLOR)

cv.namedWindow("Input Image", cv.WINDOW_AUTOSIZE)
#cv.namedWindow("Input Image2" ,cv.WINDOW_AUTOSIZE)

cv.imshow("Input Image", src)
#cv.imsh)ow("Input Image2" ,crc)

image_hist(src)

while True:
    if (cv.waitKey(100) == 27):
        break
# cv.waitKey(0)
cv.destroyAllWindows()