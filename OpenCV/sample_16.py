import cv2 as cv
import numpy as np

def threshold_demo(image):
    gray = cv.cvtColor(image ,cv.COLOR_BGR2GRAY)
    ret ,binary = cv.threshold(gray ,0 ,255 ,cv.THRESH_BINARY|cv.THRESH_OTSU)
    #ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    #ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
    print("Threshold value %s" %ret)
    cv.imshow("binary" ,binary)


def big_image_binary(image):
    cw ,ch = 200 ,200
    h ,w = image.shape[:2]
    gray = cv.cvtColor(image ,cv.COLOR_BGR2GRAY)
    for row in range(0 ,h ,ch):
        for col in range(1 ,w ,cw):
            roi = gray[row:row+ch ,col:col+cw]
            ret ,dst =cv.threshold(roi ,0 ,255 ,cv.THRESH_BINARY|cv.THRESH_OTSU)
            gray[row:row +ch ,col:col +cw] = dst
            print(np.std(dst) ,np.mean(dst))

    cv.imshow("big_image_binary" ,gray)


print("------------Hello Python-----------------------------------------------------")
src1 = cv.imread("e:/PyAI/image/min01.jpg", cv.IMREAD_COLOR)
src2 = cv.imread("e:/PyAI/image/IZONE_Gray.jpg", cv.IMREAD_COLOR)
#crc = cv.imread("e:/PyAI/image/images.jpg", cv.IMREAD_COLOR)


cv.namedWindow("Input Image", cv.WINDOW_AUTOSIZE)
#cv.namedWindow("Input Image2" ,cv.WINDOW_AUTOSIZE)

cv.imshow("Input Image", src1)
#cv.imsh)ow("Input Image2" ,crc)
threshold_demo(src1)
big_image_binary(src1)

while True:
    if (cv.waitKey(100) == 27):
        break
# cv.waitKey(0)
cv.destroyAllWindows()