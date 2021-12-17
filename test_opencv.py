# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:58:21 2020

@author: dbk
"""

import cv2
import time
import os

data_dir = 'G:/ECPH_LY/Data/协助同事/康丽利/超星视频词条加工（丽利）/1/070.机器学习与人工智能（梁）'
videofile = data_dir + '/1.2.3.“西尔勒中文屋子”实验——“图灵测试”的变体.mp4'
cap = cv2.VideoCapture(videofile)  #打开视频

start_time = time.time()
counter = 0
fps = cap.get(cv2.CAP_PROP_FPS)
while cap.isOpened():
    ret, frame = cap.read()
    key = cv2.waitKey(1)
    if key == ord(' '):
        cv2.waitKey(0)
    if key == ord('q'):
        break
    counter += 1
    if (time.time() - start_time) != 0:#实时显示帧数
        cv2.putText(frame, "FPS {0}".format(float('%.1f' % (counter / (time.time() - start_time)))), (500, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),
                    3)
        cv2.imshow('frame', frame)
        print("FPS: ", counter / (time.time() - start_time))
        counter = 0
        start_time = time.time()
    time.sleep(1 / fps)#按原帧率播放

cap.release()
cv2.destroyAllWindows()
    
'''
while (1):
    ret, frame = cap.read()  # 读取一帧视频
    # ret 读取了数据就返回True,没有读取数据(已到尾部)就返回False
    # frame 返回读取的视频数据--一帧数据
    cv2.imshow("capture", frame)  # 显示视频帧

    if cv2.waitKey(1000) & 0xFF == ord('q'):  # 等候40ms,播放下一帧，或者按q键退出
        break
cap.release()  # 释放视频流
cv2.destroyAllWindows() # 关闭所有窗口
'''