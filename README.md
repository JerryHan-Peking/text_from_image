# 2019.04作业：图像文本检测和文本识别

内容 ： MTWI 2018 挑战赛

# 1 按正确方向切割图片的方法

已知：某矩形4个连续顶点的坐标a,b,c,d;ad,bc为相对顶点

需求：裁剪出该矩形，并保持正向

(1)若四点如下所示（坐标轴顶点在左上角）

![Image text](https://github.com/JerryHan-Peking/text_from_image/blob/master/example.png)

分析ab,bc与x轴的夹角;若ab更接近水平,ac对调

(2)b在a的下方，否则ab对调，cd对调

(3)a在d的左方，否则ad对调，bc对调
 
 代码见https://github.com/JerryHan-Peking/text_from_image/blob/master/cv2_cutting.py
