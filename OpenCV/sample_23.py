import cv2 as cv
import numpy as np

def contours_demo(image):
    gray = cv.cvtColor(image ,cv.COLOR_BGR2GRAY)
    ret , binary = cv.threshold(gray ,0 ,255 ,cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary image" ,binary)

    contours , heriachy = cv.findContours(binary ,cv.RETR_TREE ,cv.CHAIN_APPROX_SIMPLE)

    for i ,contour in enumerate(contours):
        cv.drawContours(image ,contours ,i ,(0 ,0 ,255) ,2)
        print(i)

    cv.imshow("detect contours" ,image)

print("-------------- Hello Python --------------")
src1 = cv.imread("e:/PyAI/image/min01.jpg", cv.IMREAD_COLOR)
src2 = cv.imread("e:/PyAI/image/IZONE_Gray.jpg", cv.IMREAD_COLOR)
#crc = cv.imread("e:/PyAI/image/images.jpg", cv.IMREAD_COLOR)


cv.namedWindow("Input Image", cv.WINDOW_AUTOSIZE)
#cv.namedWindow("Input Image2" ,cv.WINDOW_AUTOSIZE)

cv.imshow("Input Image", src1)
#cv.imsh)ow("Input Image2" ,crc)



contours_demo(src1)

while True:
    if (cv.waitKey(100) == 27):
        break
# cv.waitKey(0)
cv.destroyAllWindows()

