# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/11 11:24 AM
@Auth ： donghao
"""
from time import sleep
from machine import Pin
from machine import PWM

pwm = PWM(Pin(5))
pwm.freq(50)  # 1/50hz = 0.02s = 20ms



# 1ms 1/20 * 100 = 5% duty cycle
# 2ms 2/20 * 100 = 10% duty cycle

# Function to set an angle
# The position is expected as a parameter

def setServoCycle(position):
    pwm.duty_u16(position)
    sleep(0.01)


while True:
    for pos in range(1000, 9000, 50):
        print(pos)
        setServoCycle(pos)
    for pos in range(9000, 1000, -50):
        print(pos)
        setServoCycle(pos)
