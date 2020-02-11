import cv2 as cv
import numpy as np

#def extrace(image):
#    hsv = cv.cvtColor(image ,cv.COLOR_BGR2HSV)
#    cv.imshow("HSV" ,hsv)
#    low_hsv = np.array([35 ,43 ,46])
#    high_hsv = np.array([77 ,255 ,255])
#    dst = cv.inRange(hsv , low_hsv ,high_hsv)
#    cv.imshow("result" ,dst)



def video_demo():
    #iz = cv.imread("E:/PyAI/image/izone.mp4")
    capture = cv.VideoCapture(0)  #假設這台電腦不只一個監視器， 0代表 第1台
                                  #如果要讀video 就給他一個路徑名稱
    while(True):
        ret , frame = capture.read()  #一直讀影片
        frame = cv.flip(frame ,1) # 1 = 左右反轉  0 = 上下反轉   -1 = 左右上下反轉
        hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
        low_hsv = np.array([35, 43, 46])
        high_hsv = np.array([77, 255, 255])
        dst = cv.inRange(hsv ,low_hsv ,high_hsv)
        #讀完了沒 #讀近來得放在哪裡
        cv.imshow("Video" ,frame)
        cv.imshow("mask" ,dst)
        c = cv.waitKey(50)   #每 50豪秒 讀取一次鍵盤
        if c == 27 :
            break

print("------------Hello Python-----------------f-")

src = cv.imread("E:/PyAI/image/IZONE.jpg")

#因為要開啟一個windows ，所以給WINDOWS 一個名稱
#預設是 WINDOWS_AUTOSIZE ，這行不打也沒關係
cv.namedWindow("Input Image" ,cv.WINDOW_AUTOSIZE)
cv.imshow("Input Image" ,src)



#video_demo()
b ,g , r = cv.split(src)
cv.imshow("blue" ,b)
cv.imshow("green" ,g)
cv.imshow("red" ,r)

src1 = cv.merge([b ,g ,r])
cv.imshow("src1 Image" ,src1)
#extrace(src)
#get_image_info(src)

#希望按任何鍵，都可以關掉
cv.waitKey(0)
#不指定
cv.destroyAllWindows()
#cv.destroyWindow()  括弧裡面是 windows NAME  EX: src
