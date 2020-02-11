import cv2 as cv

def face_detect_demo(image):
    gray = cv.cvtColor(image ,cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier("E:/PyAI/haarcascades/haarcascade_frontalface_alt.xml")
    faces = face_detector.detectMultiScale(gray ,1.1 ,5)
    for x ,y ,w ,h in faces:
        cv.rectangle(image ,(x ,y) ,(x+w ,y+h) ,(0 ,0 ,255) ,2)
    cv.imshow("face_detect_demo" ,image)


print("-------------- Hello Python --------------")
src1 = cv.imread("e:/PyAI/image/min01.jpg", cv.IMREAD_COLOR)
src2 = cv.imread("e:/PyAI/image/IZONE_Gray.jpg", cv.IMREAD_COLOR)
#crc = cv.imread("e:/PyAI/image/images.jpg", cv.IMREAD_COLOR)


cv.namedWindow("Input Image", cv.WINDOW_AUTOSIZE)
#cv.namedWindow("Input Image2" ,cv.WINDOW_AUTOSIZE)

cv.imshow("Input Image", src1)
#cv.imsh)ow("Input Image2" ,crc)

face_detect_demo(src1)

while True:
    if (cv.waitKey(100) == 27):
        break
# cv.waitKey(0)
cv.destroyAllWindows()

