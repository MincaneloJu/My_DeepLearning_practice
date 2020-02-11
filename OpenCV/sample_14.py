import cv2 as cv
from matplotlib import pyplot as plt



def back_projection_demo():
    sample = cv.imread("e:/PyAI/image/min01_sample.jpg")   #樣本
    target = cv.imread("e:/PyAI/image/min01.jpg")   #對應目標
    roi_hsv = cv.cvtColor(sample ,cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target ,cv.COLOR_BGR2HSV)

    #show image
    cv.imshow("sample" ,sample)
    cv.imshow("target" ,target)

    roiHist = cv.calcHist([roi_hsv] ,[0,1] ,None ,[36,48] ,[0,180 ,0 ,256])
                                             # bin[180 ,256] 太大，代表 對應時就會越要求越精準
                                             # bin[36 ,48] bin範圍變小 ，這樣大概顏色的會當成一個bin
    cv.normalize(roiHist ,roiHist ,0 ,255 ,cv.NORM_MINMAX)      #正規畫、歸一化
    dst = cv.calcBackProject([target_hsv] ,[0 ,1] ,roiHist ,[0 ,180 ,0 ,256] ,1)
    cv.imshow("back_projection_demo" ,dst)

print("------------Hello Python-----------------------------------------------------")
src1 = cv.imread("e:/PyAI/image/IZONE_Gray.jpg", cv.IMREAD_COLOR)
src2 = cv.imread("e:/PyAI/image/IZONE_Gray.jpg", cv.IMREAD_COLOR)
#crc = cv.imread("e:/PyAI/image/images.jpg", cv.IMREAD_COLOR)

#cv.namedWindow("Input Image", cv.WINDOW_AUTOSIZE)
#cv.namedWindow("Input Image2" ,cv.WINDOW_AUTOSIZE)

#cv.imshow("Input Image", src1)
#cv.imsh)ow("Input Image2" ,crc)

back_projection_demo()

while True:
    if (cv.waitKey(100) == 27):
        break
# cv.waitKey(0)
cv.destroyAllWindows()