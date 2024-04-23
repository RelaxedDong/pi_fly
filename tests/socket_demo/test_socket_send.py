# -*- coding: utf-8 -*-
"""
@Time ： 2024/4/23 1:53 PM
@Auth ： donghao
"""
import socket

# 树莓派 Pico 的 IP 地址和端口号
PICO_IP = "172.20.10.4"  # 替换为你的树莓派 Pico 的 IP 地址
PICO_PORT = 12345
# 命令列表
# commands = ["LED_ON", "LED_OFF", "MOTOR_ON", "MOTOR_OFF"]
# 创建套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # 连接到树莓派 Pico 的服务器
    client_socket.connect((PICO_IP, PICO_PORT))
        # 从命令列表中选择一个命令发送
        # if command in commands:
            # 发送命令到树莓派 Pico
    client_socket.send('LED_OFF'.encode("utf-8"))
except KeyboardInterrupt:
    pass
finally:
    # 关闭套接字连接
    client_socket.close()
