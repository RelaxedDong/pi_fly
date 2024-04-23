# -*- coding: utf-8 -*-
"""
@Time ： 2024/4/6 3:24 PM
@Auth ： donghao
"""
from picamera2 import Picamera2
picam2 = Picamera2()
picam2.start_and_record_video("test.mp4", duration=5)

