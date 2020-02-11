import cv2 as cv
import numpy as np

def video_demo():
    #iz = cv.imread("E:/PyAI/image/izone.mp4")
    capture = cv.VideoCapture(0)  #假設這台電腦不只一個監視器， 0代表 第1台
                                  #如果要讀video 就給他一個路徑名稱

    while(True):
        ret , frame = capture.read()  #一直讀影片
        frame = cv.flip(frame ,1) # 1 = 左右反轉  0 = 上下反轉   -1 = 左右上下反轉
        #讀完了沒 #讀近來得放在哪裡
        cv.imshow("Video" ,frame)
        c = cv.waitKey(50)   #每 50豪秒 讀取一次鍵盤
        if c == 27 :
            break


#希望知道每張 畫素
def get_image_info(image):
    print(type(image))
    print(image.shape)  # 長寬通道
    print(image.size)   # 畫面大小
    print(image.dtype)  #每個 p 單位     uint8 <= 8 bit
    #第四通道 => α 透明度
    pixel_data = np.array(image)   #rwodata
    video_demo()
    print(pixel_data)  #列印 每一點 (顏色) pixel 的  BGR 資訊


print("------------Hello Python------------------")

src = cv.imread("E:/PyAI/image/IZONE.jpg")

#因為要開啟一個windows ，所以給WINDOWS 一個名稱
#預設是 WINDOWS_AUTOSIZE ，這行不打也沒關係
cv.namedWindow("Input Image" ,cv.WINDOW_AUTOSIZE)
cv.imshow("Input Image" ,src)
get_image_info(src)

#希望按任何鍵，都可以關掉
cv.waitKey(0)
#不指定
cv.destroyAllWindows()
#cv.destroyWindow()  括弧裡面是 windows NAME  EX: src

