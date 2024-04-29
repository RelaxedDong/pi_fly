# -*- coding: utf-8 -*-
"""
@Time ： 2024/4/29 9:45 AM
@Auth ： donghao
"""
import json
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('connect', namespace='/ws')
def test_connect():
    print('Client connected')


@socketio.on('disconnect', namespace='/ws')
def test_disconnect():
    print('Client disconnected')


@socketio.on('position', namespace='/ws')
def handle_position(position):
    print(position)
    # 在这里执行你的后端逻辑，比如将接收到的位置信息存储到数据库中


if __name__ == '__main__':
    socketio.run(app, debug=True, port=8888)
