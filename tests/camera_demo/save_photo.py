from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
picam2.start()
time.sleep(2)
picam2.capture_file("test.jpg")