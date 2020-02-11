import cv2 as cv
import numpy as np



print("------------Hello Python-----------------f-")

src1 = cv.imread("E:/PyAI/image/minju.png")
print(src1.shape)


#因為要開啟一個windows ，所以給WINDOWS 一個名稱
#預設是 WINDOWS_AUTOSIZE ，這行不打也沒關係
cv.namedWindow("Input Image 1" ,cv.WINDOW_AUTOSIZE)
cv.imshow("Input Image 1" ,src1)

face = src1[15:650 ,150:835]   #[y (h) ,x (w)]
cv.imshow("face image" ,face)

gray = cv.cvtColor(face ,cv.COLOR_BGR2GRAY)
backface = cv.cvtColor(gray ,cv.COLOR_GRAY2BGR)
src1[15:650 ,150:835] = backface  #[y (h) ,x (w)]
cv.imshow("face" ,src1)




#希望按任何鍵，都可以關掉
cv.waitKey(0)
#不指定
cv.destroyAllWindows()
#cv.destroyWindow()  括弧裡面是 windows NAME  EX: src
