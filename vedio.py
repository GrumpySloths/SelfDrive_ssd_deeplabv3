import cv2
import os
import time
# folder_path="./data/frame"
# 遍历文件夹中的所有图像文件
flag=True
index=1
while(flag):
    file_path="./data/frame/%d.jpg"%index
    if os.path.exists(file_path):
        img=cv2.imread(file_path)
        cv2.imshow("Image",img)
        index+=1
        key=cv2.waitKey(10)
        if key==27:
            break
    else:
        print("file not exist,program exit")
        break
# for i in range(1,300):
    

#     img = cv2.imread("./data/frame/%i.jpg"%i)
#     # 显示图像
#     cv2.imshow('Image', img)
#     # 等待按键按下
#     key = cv2.waitKey(100)
#     # 按下esc键退出循环
#     if key == 27:
#         break
