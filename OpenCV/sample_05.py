import cv2 as cv
import numpy as np

#兩張 pixels 相加
def add_demo(m1 ,m2):
    dst = cv.add(m1 ,m2)
    cv.imshow("add_demo" ,dst)

#兩張  pixels 相減
def subtract_demo(m1 ,m2):
    dst = cv.subtract(m1 ,m2)
    cv.imshow("subtract_demo" ,dst)

def divide_demo(m1 ,m2):
    dst = cv.divide(m1 ,m2)
    cv.imshow("divide_demo" ,dst)

def logic_demo(m1 ,m2):
    dst = cv.bitwise_and(m1 ,m2)
    cv.imshow("logic_demo" ,dst)


print("------------Hello Python-----------------f-")

src1 = cv.imread("E:/PyAI/image/linux.jpg")
src2 = cv.imread("E:/PyAI/image/windows2.jpg")
print(src1.shape)
print(src2.shape)

#因為要開啟一個windows ，所以給WINDOWS 一個名稱
#預設是 WINDOWS_AUTOSIZE ，這行不打也沒關係
cv.namedWindow("Input Image 1" ,cv.WINDOW_AUTOSIZE)
cv.imshow("Input Image 1" ,src1)
cv.namedWindow("Input Image 2" ,cv.WINDOW_AUTOSIZE)
cv.imshow("Input Image 2" ,src2)

add_demo(src1 ,src2)
subtract_demo(src1 ,src2)
divide_demo(src1 ,src2)
logic_demo(src1 ,src2)

#希望按任何鍵，都可以關掉
cv.waitKey(0)
#不指定
cv.destroyAllWindows()
#cv.destroyWindow()  括弧裡面是 windows NAME  EX: src
