# -*- coding: utf-8 -*-
"""
@Time ： 2024/6/14 6:18 PM
@Auth ： donghao
"""
from machine import Pin
from machine import PWM

pwmPin = Pin(15)
pwmOutput = PWM(pwmPin)
pwmOutput.deinit()

pwmOutput.freq(int(50))  # 1/50hz = 0.02s = 20ms = 20000us


def duty():
    duty_cycle = float(input("Enter duty_cycle in percentage : "))
    duty_cycle = int(duty_cycle * 65535 / 100)
    print("duty_cycle = ", duty_cycle)
    return duty_cycle


try:
    while True:
        duty_cycle = duty()
        if 0 <= duty_cycle <= 65025:
            pwmOutput.duty_u16(duty_cycle)
        else:
            print("Unsuitable range, please enter again")
            continue
except KeyboardInterrupt:
    pwmOutput.deinit()
# 5/6 - 8.4
