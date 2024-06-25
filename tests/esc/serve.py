from machine import Pin, PWM
from time import sleep

# 设置PWM引脚和频率
pwm = PWM(Pin(15))
pwm.freq(50)  # 50Hz是标准的伺服电机频率

# 定义伺服电机旋转的脉宽值（微秒）
MIN_DUTY = 0  # 对应0度
MAX_DUTY = 2400  # 对应180度


# 将微秒转换为占空比
def duty_us_to_duty(duty_us):
    return int(duty_us / 20000 * 65535)


try:
    # 不断旋转伺服电机
    while True:
        # 从最小角度旋转到最大角度
        for duty_us in range(MIN_DUTY, MAX_DUTY, 50):
            pwm.duty_u16(duty_us_to_duty(duty_us))
            sleep(0.01)

        # 从最大角度旋转到最小角度
        # for duty_us in range(MAX_DUTY, MIN_DUTY, -50):
        #     pwm.duty_u16(duty_us_to_duty(duty_us))
        #     sleep(0.01)

except KeyboardInterrupt:
    pwm.deinit()
