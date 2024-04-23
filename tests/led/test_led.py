import time
from machine import Pin

led = Pin("LED", Pin.OUT)  # GPIO 引脚 25 控制板载 LED

while True:
    led.on()
    print('light')
    time.sleep(1)  # 等待1秒
    led.off()
    print('off')
    time.sleep(1)
