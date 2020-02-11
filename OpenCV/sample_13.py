import cv2 as cv
import numpy as np

def create_rgb_hist(image):
    h ,w ,c = image.shape
    rgbHist = np.zeros( [16*16*16 ,1] ,np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row ,col ,0]
            g = image[row ,col ,1]
            r = image[row ,col ,2]
            index = np.int(b/bsize) *16 *16 + np.int(g/bsize) *16 + np.int(r/bsize)
            rgbHist[np.int(index) ,0] = rgbHist[np.int(index) ,0 ] +1

    print(rgbHist)
    return rgbHist

def hist_compare(image1 ,image2):
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)

    match1 = cv.compareHist(hist1 ,hist2 ,cv.HISTCMP_BHATTACHARYYA)  #巴氏
    match2 = cv.compareHist(hist1 ,hist2 ,cv.HISTCMP_CORREL)         #相關性
    match3 = cv.compareHist(hist1 ,hist2 ,cv.HISTCMP_CHISQR)         #卡方
    print("巴氏 : %s   相關性 : %s      卡方 : %s " %(match1 ,match2 ,match3))

print("------------Hello Python-----------------------------------------------------")
src1 = cv.imread("e:/PyAI/image/IZONE_Gray.jpg", cv.IMREAD_COLOR)
src2 = cv.imread("e:/PyAI/image/IZONE_Gray.jpg", cv.IMREAD_COLOR)
#crc = cv.imread("e:/PyAI/image/images.jpg", cv.IMREAD_COLOR)

cv.namedWindow("Input Image", cv.WINDOW_AUTOSIZE)
#cv.namedWindow("Input Image2" ,cv.WINDOW_AUTOSIZE)

cv.imshow("Input Image", src1)
#cv.imsh)ow("Input Image2" ,crc)


hist_compare(src1 ,src2)

while True:
    if (cv.waitKey(100) == 27):
        break
# cv.waitKey(0)
cv.destroyAllWindows()