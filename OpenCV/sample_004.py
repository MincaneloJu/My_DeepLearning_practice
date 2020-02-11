import cv2 as cv

def color_space_demo(image):
    gray = cv.cvtColor(image ,cv.COLOR_BGR2GRAY)
    cv.imshow("grays" ,gray)

    hsv = cv.cvtColor(image ,cv.COLOR_BGR2HSV)
    cv.imshow("HSV" ,hsv)

    yuv = cv.cvtColor(image ,cv.COLOR_BGR2YUV)
    cv.imshow("YUV" ,yuv)

    ycrcb = cv.cvtColor(image ,cv.COLOR_BGR2YCrCb)
    cv.imshow("YCRCB" ,ycrcb)

print("------------Hello Python------------------")

src = cv.imread("E:/PyAI/image/IZONE.jpg")

#因為要開啟一個windows ，所以給WINDOWS 一個名稱
#預設是 WINDOWS_AUTOSIZE ，這行不打也沒關係
cv.namedWindow("Input Image" ,cv.WINDOW_AUTOSIZE)
cv.imshow("Input Image" ,src)


color_space_demo(src)
#get_image_info(src)

#希望按任何鍵，都可以關掉
cv.waitKey(0)
#不指定
cv.destroyAllWindows()
#cv.destroyWindow()  括弧裡面是 windows NAME  EX: src
