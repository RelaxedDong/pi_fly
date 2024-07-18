import time
from microdot import Microdot, send_file
from microdot.websocket import with_websocket

app = Microdot()
dfly_weight = 35  # 35g
motor_g = 32.5
balance_pct = int(dfly_weight / (motor_g * 4))  # 悬空时的占空比例

import _thread

from machine import PWM, Pin
from wifi import open_wifi

led = Pin("LED", Pin.OUT)  # GPIO 引脚 25 控制板载 LED
gpio_motor1 = 2  # front left, clockwise
gpio_motor2 = 28  # front right, counter clockwise
gpio_motor3 = 15  # rear left, counter clockwise
gpio_motor4 = 16  # rear right, clockwise
wifi_ssid = 'dfly'
wifi_pwd = '88888888'

pwm_freq = 50
open_wifi(wifi_ssid, wifi_pwd)
motor1 = PWM(Pin(gpio_motor1))
motor2 = PWM(Pin(gpio_motor2))
motor3 = PWM(Pin(gpio_motor3))
motor4 = PWM(Pin(gpio_motor4))
motor1.freq(pwm_freq)  # 1/50hz = 0.02s = 20ms = 20000us
motor2.freq(pwm_freq)
motor3.freq(pwm_freq)
motor4.freq(pwm_freq)


def FATAL_ERROR(msg: str) -> None:
    em: str = "Fatal error @ " + str(time.ticks_ms()) + " ms: " + msg
    print(em)
    fp = "error_log.txt"
    f = open(fp, "a")
    f.write(em + "\n\n")
    f.close()


def _set_duty(duty_cycle_pct):
    return int(duty_cycle_pct * 65535 / 100)


def flush_led(flush_times, sleep_time):
    for x in range(flush_times):
        led.on()
        time.sleep(sleep_time)
        led.off()
        time.sleep(sleep_time)


def set_duty_cycle(duty_pct):
    motor1.duty_u16(_set_duty(duty_pct))
    motor2.duty_u16(_set_duty(duty_pct))
    motor3.duty_u16(_set_duty(duty_pct))
    motor4.duty_u16(_set_duty(duty_pct))


def destroy_motor():
    set_duty_cycle(0)
    motor1.deinit()
    motor2.deinit()
    motor3.deinit()
    motor4.deinit()


def map_remote_to_pwm(remote_value):
    # 遥控器输入范围
    min_remote = 1000
    max_remote = 2000
    # 占空比范围
    min_pwm = 0
    max_pwm = 10
    # 计算对应的占空比
    pwm = min_pwm + (max_pwm - min_pwm) * (remote_value - min_remote) / (max_remote - min_remote)
    return pwm


@app.route('/')
def index(request):
    return send_file('index.html')


receive_data = []
fly_running = False
running_computing = True
finished = False


@app.route('/control')
@with_websocket
async def control_fly(request, ws):
    global receive_data
    global fly_running
    while True:
        data = await ws.receive()
        receive_data = [int(d) for d in data.split(",")]
        print("receive_data", receive_data)
        if receive_data[0] == 0:  # wait for command
            flush_led(3, 1)
            fly_running = False
        elif receive_data[0] == -1:  # 测试连接
            flush_led(3, 0.3)
            await ws.send('opened')
            fly_running = True


def main():
    global finished
    while running_computing:
        print('running computing...')
        try:
            if fly_running:
                throttle = receive_data[3]
                if throttle == 1500:
                    set_duty_cycle(5 + 5 * balance_pct)
                else:
                    pct = map_remote_to_pwm(throttle)
                    set_duty_cycle(pct)
            else:
                print('wait for start...')
                time.sleep(5)
        except Exception as e:
            FATAL_ERROR(str(e))
    finished = True


_thread.start_new_thread(main, ())

try:
    app.run(debug=True, port=80)
except KeyboardInterrupt:
    pass
finally:
    running_computing = False
    print("main exit...")
while not finished:
    pass
print("Thread has finished...")
