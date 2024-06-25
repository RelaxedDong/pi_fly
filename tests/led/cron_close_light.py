# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/27 5:35 PM
@Auth ： donghao
"""
import datetime

from machine import Pin, PWM
from time import sleep
import time

# 设置PWM引脚和频率
pwm = PWM(Pin(15))
pwm.freq(50)  # 50Hz是标准的伺服电机频率

# 定义伺服电机旋转的脉宽值（微秒）

MIN_DUTY = 1000  # 对应0度
MAX_DUTY = 2000  # 对应180度


# 将微秒转换为占空比
def duty_us_to_duty(duty_us):
    return int(duty_us / 20000 * 65535)


def swich_light(is_open):
    if is_open:
        pwm.duty_u16(duty_us_to_duty(1000))
    else:
        pwm.duty_u16(duty_us_to_duty(2000))
    time.sleep(2)


def log(msg: str) -> None:
    now = datetime.datetime.now()
    fp = "/logs"
    f = open(fp, "a")
    f.write(f"[{now}] {msg}" + "\n\n")
    f.close()


while True:
    now = datetime.datetime.now()
    if now.hour == 22:
        log(f"close light")
        swich_light(False)
    else:
        log(f"wait for close")
        time.sleep(60 * 60)
