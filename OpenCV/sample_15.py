import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

def template_demo():
    tp1 = cv.imread("e:/PyAI/image/min01_sample.jpg")   #比對樣本 小張的
    target = cv.imread("e:/PyAI/image/min01.jpg")       #對應目標 大張的
    cv.imshow("tp1 Image" ,tp1)
    cv.imshow("target Image" ,target)
    methods = [cv.TM_SQDIFF_NORMED ,cv.TM_CCORR_NORMED ,cv.TM_CCOEFF_NORMED]  #看這幾個公式
    th ,tw = tp1.shape[:2]

    for md in methods:
        print(md)
        result = cv.matchTemplate(target ,tp1 ,md)  #陣列
        min_val ,max_val ,min_loc ,max_loc  = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            t1 = min_loc
        else:
            t1 = max_loc
        br = (t1[0] + tw ,t1[1] + th)
        cv.rectangle(target ,t1 ,br ,(0 ,0 ,255) ,2)
        cv.imshow("match-" + np.str(md) ,target)
        cv.imshow("match-(result)" +np.str(md) ,result )




print("------------Hello Python-----------------------------------------------------")
src1 = cv.imread("e:/PyAI/image/IZONE_Gray.jpg", cv.IMREAD_COLOR)
src2 = cv.imread("e:/PyAI/image/IZONE_Gray.jpg", cv.IMREAD_COLOR)
#crc = cv.imread("e:/PyAI/image/images.jpg", cv.IMREAD_COLOR)

#cv.namedWindow("Input Image", cv.WINDOW_AUTOSIZE)
#cv.namedWindow("Input Image2" ,cv.WINDOW_AUTOSIZE)

#cv.imshow("Input Image", src1)
#cv.imsh)ow("Input Image2" ,crc)

template_demo()

while True:
    if (cv.waitKey(100) == 27):
        break
# cv.waitKey(0)
cv.destroyAllWindows()