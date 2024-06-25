import _thread
import time
from microdot import Microdot, send_file
from microdot.websocket import with_websocket

app = Microdot()
dfly_weight = 35  # 35g
motor_g = 32.5
running = True
balance_pct = int(dfly_weight / (motor_g * 4) * 100)  # 悬空时的占空比例

try:
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
except:
    pass


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


class OperationEnum(object):
    STOP = 0
    START = 1
    START_FLY = 2
    START_DOWN = 3
    LEFT_UP = 11
    LEFT_RIGHT = 12
    LEFT_LEFT = 13
    LEFT_DOWN = 14
    RIGHT_UP = 15
    RIGHT_LEFT = 16
    RIGHT_RIGHT = 17
    RIGHT_DOWN = 18


def get_pwm_pct(value, min_pwm_pct, max_pwm_cpt):
    from_min, from_max = 0, 100
    from_range = from_max - from_min
    to_range = max_pwm_cpt - min_pwm_pct
    scaled_value = float(value - from_min) / float(from_range)
    return min_pwm_pct + (scaled_value * to_range)


@app.route('/')
def index(request):
    return send_file('index.html')


@app.route('/control')
@with_websocket
async def control_fly(request, ws):
    while True:
        data = await ws.receive()
        receive_data = [int(d) for d in data.split(",")]
        print(receive_data)
        await ws.send('received')


try:
    app.run(debug=True, port=80)
except KeyboardInterrupt:
    pass

