import cv2 as cv
import numpy as np

def extrace(image):
    hsv = cv.cvtColor(image ,cv.COLOR_BGR2HSV)
    cv.imshow("HSV" ,hsv)
    low_hsv = np.array([35 ,43 ,46])
    high_hsv = np.array([77 ,255 ,255])
    dst = cv.inRange(hsv , low_hsv ,high_hsv)
    cv.imshow("result" ,dst)



print("------------Hello Python------------------")

src = cv.imread("E:/PyAI/image/IZONE.jpg")

#因為要開啟一個windows ，所以給WINDOWS 一個名稱
#預設是 WINDOWS_AUTOSIZE ，這行不打也沒關係
cv.namedWindow("Input Image" ,cv.WINDOW_AUTOSIZE)
cv.imshow("Input Image" ,src)



extrace(src)
#get_image_info(src)

#希望按任何鍵，都可以關掉
cv.waitKey(0)
#不指定
cv.destroyAllWindows()
#cv.destroyWindow()  括弧裡面是 windows NAME  EX: src
