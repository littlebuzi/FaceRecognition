import cv2
import os

# 调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2

cap = cv2.VideoCapture(1)

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_id = input('\n 请输入用户id:')

print('\n 正在启动摄像头. 请看着摄像头并等待 ...')

count = 0

while True:

    # 从摄像头读取图片
    sucess, img = cap.read()

    # 转为灰度图片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 检测人脸
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+w), (255, 0, 0))

        count += 1

        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(img, 'num:%d' % (count), (x + 30, y + 30), font, 1, (255, 0, 255), 4)

        # 保存图像
        cv2.imwrite("data/User." + str(face_id) + '.' + str(count) + '.jpg', gray[y: y + h, x: x + w])
        cv2.imshow('image', img)

    # 保持画面的持续。

    k = cv2.waitKey(1)

    if k == 27:   # 通过esc键退出摄像
        break

    elif count >= 1000:  # 得到1000个样本后退出摄像
        break

# 关闭摄像头

cap.release()

cv2.destroyAllWindows()