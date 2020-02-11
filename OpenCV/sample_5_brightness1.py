import cv2 as cv
import numpy as np

def constrast_brightness_demo(image ,c):
    h ,w ,ch = image.shape #要抓到圖片得 長、寬、通道數
    blank = np.zeros([h ,w ,ch] ,image.dtype)
    dst = cv.addWeighted(image ,c ,blank ,1-c ,0) #實現圖片得線性融合
    cv.imshow("contrast_brightness" ,dst)

print("------------Hello Python-----------------f-")

src1 = cv.imread("E:/PyAI/image/izone.jpg")
print(src1.shape)


#因為要開啟一個windows ，所以給WINDOWS 一個名稱
#預設是 WINDOWS_AUTOSIZE ，這行不打也沒關係
cv.namedWindow("Input Image 1" ,cv.WINDOW_AUTOSIZE)
cv.imshow("Input Image 1" ,src1)

constrast_brightness_demo(src1 ,1.2)   # 10 偏移值 可以不加(做調整用)
#希望按任何鍵，都可以關掉
cv.waitKey(0)
#不指定
cv.destroyAllWindows()
#cv.destroyWindow()  括弧裡面是 windows NAME  EX: src
