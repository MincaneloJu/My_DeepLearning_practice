import cv2 as cv
import numpy as np

def measure_object(image):
    gray = cv.cvtColor(image ,cv.COLOR_BGR2GRAY)
    ret ,binary = cv.threshold(gray ,0 ,255 ,cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary image" ,binary)
    contours ,hireachy = cv.findContours(binary ,cv.RETR_EXTERNAL ,cv.CHAIN_APPROX_SIMPLE)
    for i ,contour in enumerate(contours):
        area = cv.contourArea(contour)
        x ,y ,w ,h = cv.boundingRect(contour)
        mm = cv.moments(contour)
        type(mm)
        cx = mm['m10'] / mm['m00']
        cy = mm['m01'] / mm['m00']
        cv.circle(image ,(np.int(cx) ,np.int) )

print("-------------- Hello Python --------------")
src1 = cv.imread("e:/PyAI/image/min01.jpg", cv.IMREAD_COLOR)
src2 = cv.imread("e:/PyAI/image/IZONE_Gray.jpg", cv.IMREAD_COLOR)
#crc = cv.imread("e:/PyAI/image/images.jpg", cv.IMREAD_COLOR)


cv.namedWindow("Input Image", cv.WINDOW_AUTOSIZE)
#cv.namedWindow("Input Image2" ,cv.WINDOW_AUTOSIZE)

cv.imshow("Input Image", src1)
#cv.imsh)ow("Input Image2" ,crc)

while True:
    if (cv.waitKey(100) == 27):
        break
# cv.waitKey(0)
cv.destroyAllWindows()