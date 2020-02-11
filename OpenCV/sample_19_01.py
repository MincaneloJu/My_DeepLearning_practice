import cv2 as cv
import numpy as np

def laplacian_demo(image):
    #dst = cv.Laplacian(image ,cv.CV_32F)
    #lpls = cv.convertScaleAbs(dst)

    kernel = np.array( [ [0 ,1 ,0] ,[1 ,-4 ,1] ,[0 ,1 ,0] ] )
    dst = cv.filter2D(image ,cv.CV_32F ,kernel=kernel)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("laplacian_demo" ,lpls)


print("-------------- Hello Python --------------")
src1 = cv.imread("e:/PyAI/image/min01.jpg", cv.IMREAD_COLOR)
src2 = cv.imread("e:/PyAI/image/IZONE_Gray.jpg", cv.IMREAD_COLOR)
#crc = cv.imread("e:/PyAI/image/images.jpg", cv.IMREAD_COLOR)


cv.namedWindow("Input Image", cv.WINDOW_AUTOSIZE)
#cv.namedWindow("Input Image2" ,cv.WINDOW_AUTOSIZE)

cv.imshow("Input Image", src1)
#cv.imsh)ow("Input Image2" ,crc)

laplacian_demo(src1)

while True:
    if (cv.waitKey(100) == 27):
        break
# cv.waitKey(0)
cv.destroyAllWindows()


