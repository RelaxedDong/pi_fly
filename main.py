# -*- coding: utf-8 -*-
"""
@Time ： 2024/4/23 9:53 PM
@Auth ： donghao
"""
import machine
import time

# 设置 GPIO 引脚号
pin_number = 16  # 这里假设使用 GPIO 0

# 初始化 GPIO 引脚
pin = machine.Pin(pin_number, machine.Pin.OUT)

# 将 GPIO 引脚设置为高电平
pin.value(1)
time.sleep(10)  # 等待一秒

# 将 GPIO 引脚设置为低电平
pin.value(0)
time.sleep(1)  # 等待一秒

# 最后记得释放 GPIO 引脚
pin.deinit()
