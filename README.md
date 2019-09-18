# FaceRecognition

> # 作业项目：人脸识别签到系统



界面：

![](https://littlebuzi.github.io/2019/08/09/python/face/1568803408485.png)



## 三、项目实现过程：



![](https://littlebuzi.github.io/2019/08/09/python/face/1568803348963.png)



### 人脸检测：

使用OpenCV的人脸检测器进行人脸的初步检测，使haarcascade_frontalface_default.xml训练进行人脸的二分类判定，完成人脸检测。换调用摄像头：“cv2.VideoCapture(1)”，使用Python+OpenCV进行视频中的人脸检测，人脸关键点定位：关键点定位的目标是在确知人脸位置的基础上，精确定位面部的关键点，如下图示意：

![](https://littlebuzi.github.io/2019/08/09/python/face/1568803533749.png)



### 图像采集：

采集1000张图片，转换为灰度图并报错，以自己设定好的规律命名图片文件，易于之后的读取后训练。

获得面部关键点的目的是进行人脸的对齐和标准化。标准化的人脸输入可以获得更高的人脸识别精度。



### 图像特征采集：

人脸特征提取是根据上述标准化的人脸区域图块，提取出数字化的特征。即完成从RGB信息到数值特征的变换。此环节需要尽量使得同一个人物的不同人脸所提取到的特征尽可能相似，而不同人物的人脸所提取的特征尽可能相异。



模型的训练：

人脸识别的模型的训练采用LBPH算法：

cv2.face.LBPHFaceRecognizer_create()

> [OpenCV人脸识别LBPH算法源码分析](https://www.cnblogs.com/zhaoweiwei/p/LBPH.html)

注册成功：

![](https://littlebuzi.github.io/2019/08/09/python/face/1568805892550.png)

签到成功：

![](https://littlebuzi.github.io/2019/08/09/python/face/1568805922061.png)



> 不同算法详细介绍：
>
> [人脸识别算法之特征脸方法（Eigenface、FisherFace、LBPH](https://www.cnblogs.com/little-monkey/p/8118938.html)



 LBPH算法：

原理：通过已知条件，利用特定关系逐步递推，最终得到结果。



1. 提取特征值并转换

![](https://littlebuzi.github.io/2019/08/09/python/face/1568805324851.png)

2. 生成数据集，训练，生成yml文件

   ![](https://littlebuzi.github.io/2019/08/09/python/face/1568805339521.png)

3. 计算（欧式）距离，输出相似度

   ![](https://littlebuzi.github.io/2019/08/09/python/face/1568805361705.png)



## 整体代码流程：

![](https://littlebuzi.github.io/2019/08/09/python/face/1568806231175.png)


![](https://littlebuzi.github.io/2019/08/09/python/face/1568807139089.png)
