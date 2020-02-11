import cv2 as cv
import numpy as np

def fill_color_demo(image):
    copyimage = image.copy()
    h ,w = image.shape[:2]   #只抓 高 跟 寬
    mask = np.zeros([h+2 ,w+2] ,np.uint8)
    (b ,g ,r) = copyimage[360 ,545]   # [y ,x]
    print("位置(545 ,360)處的像素 - 紅: %d ,綠:%d ,藍:%d " %(r ,g ,b) )
    cv.floodFill(copyimage ,mask ,(545 ,360) ,(0 ,255 ,255) ,(30 ,20 ,10) ,(40 ,40 ,40) ,cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color" ,copyimage)

def fill_binary():
    image = np.zeros([400 ,400 ,3] ,np.uint8)   # [h ,w ,c]
    image[100:300 ,100:300 ,:] = 255
    cv.imshow("fill_binary" ,image)

    mask = np.ones([400+2 ,400+2] ,np.uint8)

    #mask[99:301 ,99:301] = 0
    mask[119:281 ,119:281] = 0
    cv.floodFill(image ,mask ,(118 ,118) ,(0 ,0 ,255) ,cv.FLOODFILL_MASK_ONLY)
    #  (200 ,200) 這邊是沒用得
    cv.imshow("fill_binary1" ,image)



print("------------Hello Python-----------------f-")

src1 = cv.imread("E:/PyAI/image/minju.png")
print(src1.shape)


#因為要開啟一個windows ，所以給WINDOWS 一個名稱
#預設是 WINDOWS_AUTOSIZE ，這行不打也沒關係
cv.namedWindow("Input Image 1" ,cv.WINDOW_AUTOSIZE)
cv.imshow("Input Image 1" ,src1)

fill_color_demo(src1)
fill_binary()

#希望按任何鍵，都可以關掉
cv.waitKey(0)
#不指定
cv.destroyAllWindows()
#cv.destroyWindow()  括弧裡面是 windows NAME  EX: src
