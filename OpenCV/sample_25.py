

print("-------------- Hello Python --------------")
src1 = cv.imread("e:/PyAI/image/min01.jpg", cv.IMREAD_COLOR)
src2 = cv.imread("e:/PyAI/image/IZONE_Gray.jpg", cv.IMREAD_COLOR)
#crc = cv.imread("e:/PyAI/image/images.jpg", cv.IMREAD_COLOR)


cv.namedWindow("Input Image", cv.WINDOW_AUTOSIZE)
#cv.namedWindow("Input Image2" ,cv.WINDOW_AUTOSIZE)

cv.imshow("Input Image", src1)
#cv.imsh)ow("Input Image2" ,crc)



while True:
    if (cv.waitKey(100) == 27):
        break
# cv.waitKey(0)
cv.destroyAllWindows()

