# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/2 7:59 PM
@Auth ： donghao
"""
from machine import Pin, PWM
import time

pwm_motor = PWM(Pinled = Pin("LED", Pin.OUT))
pwm_motor.freq(1000)
while True:
    for x in range(65536):
        pwm_motor.duty_u16(x)
    time.sleep(0.0001)
    for x in range(65536, 0, -1):
        pwm_motor.duty_u16(x)
    time.sleep(0.0001)
