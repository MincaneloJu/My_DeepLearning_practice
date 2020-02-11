import  cv2 as cv
import numpy as np

def access_pixels(image):
    # 影像資訊
    print(image.shape)

    #單獨讀取 影像  長 、 寬 、 通道數 資訊
    height = image.shape[0]
    weight = image.shape[1]
    channel = image.shape[2]
    print("width : %s ,height :%s ,channel : %s"  %(height ,weight ,channel))
    for row in range(height):
        for col in range(weight):
            for c in range(channel):
                pv = image[row ,col ,c]
                image[row ,col ,c] = 255 - pv
    cv.imshow("haha_pixels" ,image)

# 用裡面提供的函數 用not 相當於對每個點做 255 - pixels
def inverse(image):
    dddd = cv.bitwise_not(image)
    cv.imshow("inverse" ,dddd)

def creat_image():


    m1 = np.ones([3 ,3] ,np.float32)
    m1.fill(123.456)
    print(m1)
    m2 = m1.reshape([1 ,9])
    print(m2)
'''
    img = np.ones([400 ,400 ,1] ,np.uint8)
    img = img*127
    cv.imshow("create_image_lalala" ,img)



    img = np.zeros( [400 ,400 ,3]  ,np.uint8)
    for x in range(0 ,2):
        img[ : , : , x ] = np.ones([400 ,400]) + 199   # (打成*255 也可以，只是運算)
    cv.imshow("creat_imagessss" ,img)    
'''


print("------------Hello Python------------------")

src = cv.imread("E:/PyAI/image/IZONE.jpg")

#因為要開啟一個windows ，所以給WINDOWS 一個名稱
#預設是 WINDOWS_AUTOSIZE ，這行不打也沒關係
cv.namedWindow("Input Image" ,cv.WINDOW_AUTOSIZE)
cv.imshow("Input Image" ,src)

inverse(src)

#進入函式前的時間 (clock)
t1 = cv.getTickCount()
#access_pixels(src)
#函式跑完後的時間 (clock)
t2 = cv.getTickCount()

time = (t2 - t1) / cv.getTickFrequency()
print("time : %s ms" %(time*1000))


creat_image()

#希望按任何鍵，都可以關掉
cv.waitKey(0)
#不指定
cv.destroyAllWindows()
#cv.destroyWindow()  括弧裡面是 windows NAME  EX: src
