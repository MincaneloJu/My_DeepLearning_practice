import cv2 as cv
import numpy as np

def blur_demo(image):
    det = cv.blur(image ,(5 ,5))
    cv.imshow("blur" ,det)


def median_blur_demo(image):
    det = cv.medianBlur(image ,5)   # 5 的意思 5X5
    cv.imshow("median_blur" ,det)

def custon_blur_demo(image):
    kernel = np.array( [ [0 ,-1 ,0] ,[-1 ,5 ,-1] ,[0 ,-1 ,0] ] ,np.float32 )
    det = cv.filter2D(image ,-1 ,kernel=kernel)
    cv.imshow("custon_blur_demo" ,det)



print("------------Hello Python------------")
src = cv.imread("e:/PyAI/image/minju1.jpg" ,cv.IMREAD_COLOR)
crc = cv.imread("e:/PyAI/image/TnTaxDl.jpg" ,cv.IMREAD_COLOR)
cv.namedWindow("Input Image" ,cv.WINDOW_AUTOSIZE)
cv.namedWindow("Input Image2" ,cv.WINDOW_AUTOSIZE)
cv.imshow("Input Image" ,src)
cv.imshow("Input Image2" ,crc)

blur_demo(src)

median_blur_demo(crc)

custon_blur_demo(src)

while True:
    if (cv.waitKey(100)==27):
        break
#cv.waitKey(0)
cv.destroyAllWindows()