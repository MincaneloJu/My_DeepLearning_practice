import cv2 as cv
import numpy as np

def edge_demo(image):
    blurred = cv.GaussianBlur(image ,(3 ,3) ,0)
    gray = cv.cvtColor(blurred ,cv.COLOR_BGR2GRAY)
    # X Gradient
    xgrad = cv.Sobel(gray ,cv.CV_16SC1 ,1 ,0)

    #Y Gradient
    ygrad = cv.Sobel(gray ,cv.CV_16SC1 ,0 ,1)

    #edge
    edge_output = cv.Canny(xgrad ,ygrad ,50 ,150)
    cv.imshow("edge_demo" ,edge_output)

    dst = cv.bitwise_and(image ,image ,mask=edge_output)
    cv.imshow("Color Edge" ,dst)


print("-------------- Hello Python --------------")
src1 = cv.imread("e:/PyAI/image/min01.jpg", cv.IMREAD_COLOR)
src2 = cv.imread("e:/PyAI/image/IZONE_Gray.jpg", cv.IMREAD_COLOR)
#crc = cv.imread("e:/PyAI/image/images.jpg", cv.IMREAD_COLOR)


cv.namedWindow("Input Image", cv.WINDOW_AUTOSIZE)
#cv.namedWindow("Input Image2" ,cv.WINDOW_AUTOSIZE)

cv.imshow("Input Image", src1)
#cv.imsh)ow("Input Image2" ,crc)

edge_demo(src1)

while True:
    if (cv.waitKey(100) == 27):
        break
# cv.waitKey(0)
cv.destroyAllWindows()


