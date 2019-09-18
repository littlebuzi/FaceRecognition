import os
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from tkinter import *

import cv2

root = tk.Tk()  # 生成主窗口
root.title("人脸课室签到系统")   # 窗体名称
root.geometry("1100x510")   # 指定窗体大小

label = ttk.Label(root, text="欢迎使用“天天向上签到系统”")
label.pack()

def click1(event):

    os.system("python D:/人脸/myface/faceRecognition5/face_data_collect.py")
    os.system("python D:/人脸/myface/faceRecognition5/face_training.py")
    messagebox.showinfo("提示", "注册成功！")

def click2(event):
    os.system("python D:/人脸/myface/faceRecognition5/face_recognition.py")
    #messagebox.showinfo("提示", "签到成功！")

button1 = ttk.Button(root, text="注册")
button1.bind("<Button-1>", click1)
button1.pack(side=tk.LEFT)

button2 = ttk.Button(root, text="签到")
button2.bind("<Button-1>", click2)
button2.pack(side=tk.RIGHT)

root.mainloop()  
