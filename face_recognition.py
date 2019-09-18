import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX

idnum = 0

names = ['user1', 'user2','user3','user4']

cam = cv2.VideoCapture(1)
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

i = 0
a = 0

user1=0
user2=0
user3=0
user4=0

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH))
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        idnum, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        if confidence < 50:
            idnum = names[idnum]
            confidence = "{0}%".format(round(100 - confidence))

            import tkinter
            import tkinter.messagebox 

            if idnum=='user1':
                if wuzifeng==0:
                    import xlwt
                    from xlwt import Workbook
                    book = Workbook(encoding='utf-8')
                    sheet1 = book.add_sheet('Sheet 1')
                    sheet1.write(0, 0, "姓名")
                    sheet1.write(0, 1, "状态")
                    sheet1.write(1,0, str(idnum))
                    sheet1.write(1,1, "签到成功")
                    book.save(r'qiandao.xls')

                    tkinter.messagebox.showinfo('提示','user1:签到成功！')
                    wuzifeng=wuzifeng+1

            if idnum == 'user2':
                if zenjiaxin == 0:

                    sheet1.write(2, 0, str(idnum))
                    sheet1.write(2, 1, "签到成功")
                    book.save(r'qiandao.xls')

                    tkinter.messagebox.showinfo('提示', 'user2:签到成功！')
                    zenjiaxin = zenjiaxin + 1

            if idnum == 'user3':
                if linzhuowen == 0:

                    sheet1.write(3, 0, str(idnum))
                    sheet1.write(3, 1, "签到成功")
                    book.save(r'qiandao.xls')

                    tkinter.messagebox.showinfo('提示', 'user3:签到成功！')
                    linzhuowen = linzhuowen + 1

            if idnum == 'user4':
                if liujinghe == 0:

                    sheet1.write(4, 0, str(idnum))
                    sheet1.write(4, 1, "签到成功")
                    book.save(r'qiandao.xls')

                    tkinter.messagebox.showinfo('提示', 'user4:签到成功！')
                    liujinghe = liujinghe + 1

        else:
            idnum = "Unknown"
            confidence = "{0}%".format(round(100 - confidence))

        cv2.putText(img, str(idnum), (x+5, y-5), font, 1, (0, 0, 255), 1)
        cv2.putText(img, str(confidence), (x+5, y+h-5), font, 1, (0, 0, 0), 1)

    cv2.imshow('camera', img)
    k = cv2.waitKey(10)
    if k == 27:
        break

    if k == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()