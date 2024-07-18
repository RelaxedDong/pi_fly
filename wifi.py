# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/13 11:17 AM
@Auth ： donghao
"""
import network


def open_wifi(ssid, password):
    """
    Description: This is a function to activate AP mode

    Parameters:

    ssid[str]: The name of your internet connection
    password[str]: Password for your internet connection

    Returns: Nada
    """
    # Just making our internet connection
    ap = network.WLAN(network.AP_IF)
    ap.config(essid=ssid, password=password)
    print("start open wifi")
    if ap.active():
        print('Wifi Still Active!')
        return
    ap.active(True)
    while ap.active() == False:
        pass
    print('AP Mode Is Active, You can Now Connect')
    print('IP Address To Connect to:: ' + ap.ifconfig()[0])
