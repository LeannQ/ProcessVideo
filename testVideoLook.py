# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:25:15 2020

@author: dbk
"""

import pygame as pg
from  moviepy.editor import *
from moviepy.editor import VideoFileClip
from moviepy.video.io.preview import imdisplay
import time

data_dir = 'G:/ECPH_LY/Data/协助同事/康丽利/超星视频词条加工（丽利）/1/070.机器学习与人工智能（梁）'
videofile = data_dir + '/1.2.3.“西尔勒中文屋子”实验——“图灵测试”的变体.mp4'
clip = VideoFileClip(videofile).subclip(0,10)
#存储视频在第10秒的帧图像
#clip.save_frame('frame.jpeg',t=10)
clip.show()
'''
#视频剪辑预览
threads = 8
newclip = clip.fx(vfx.loop).set_duration(50)
preview(newclip)
'''
'''
#视频帧预览
screen = pg.display.set_mode(clip.size)

for t in range(5,10):
    imdisplay(clip.get_frame(t), screen)
    time.sleep(1)
'''