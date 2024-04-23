# -*- coding: utf-8 -*-
"""
@Time ： 2024/4/23 1:52 PM
@Auth ： donghao
"""
# ls /dev/tty.usbmodem11201/
# 配置 Wi-Fi 参数
WIFI_SSID = "hao的iPhone"
WIFI_PASSWORD = "dt20171008."

# 创建 Wi-Fi 连接
from time import sleep

import network
import socket
from machine import Pin

wifi = network.WLAN(network.STA_IF)
wifi.active(True)  # 激活 Wi-Fi 接口
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

# 等待 Wi-Fi 连接成功
while not wifi.isconnected():
    print('wait Wi-Fi connect...')
    sleep(1)
    pass
print('connect success!')

# 获取本地 IP 地址
local_ip = wifi.ifconfig()[0]
# print(local_ip)
# 创建服务器套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((local_ip, 12345))  # 绑定到本地 IP 地址的端口 12345
server_socket.listen(1)

print("等待连接...")

client_socket, client_address = server_socket.accept()
print("接收来自", client_address)
led = Pin("LED", Pin.OUT)  # GPIO 引脚 25 控制板载 LED

try:
    while True:
        data = client_socket.recv(1024)
        if data:
            command = data.decode("utf-8")
            print("收到命令:", command)
            # 根据接收到的命令执行相应的动作
            if command == "LED_ON":
                # 执行打开 LED 的动作
                led.on()
            elif command == "LED_OFF":
                # 执行关闭 LED 的动作
                led.off()
        else:
            client_socket.close()
            break
except OSError:
    pass

print("连接已关闭")
server_socket.close()
