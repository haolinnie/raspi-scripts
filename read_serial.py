#!/usr/bin/python3
import time
import sys
import glob
import serial
import requests

url = "https://home.tigernie.com/home_api/"


def postData(url, name, x):
    res = requests.post(url + 'room_temp', 
                        json={'name': name, 'value': x})
    print(res)
    print(res.json())

# Initialise Serial
def getDevPort():
    serialPortFound = False
    if sys.platform == 'linux':
        ports = glob.glob('/dev/ttyACM*')
    elif sys.platform == 'darwin':
        ports = glob.glob('/dev/tty.usb*')

    if not ports:
        print('[ERROR] No USB ports found')
        sys.exit()

    # Open Serial port to Arduino to read data
    for port in ports:
        try:
            dev = serial.Serial(port=port,
                                baudrate=115200,
                                timeout=2,
                                writeTimeout=0)
            serialPortFound = True
            print("Established connection with {}".format(port))
        except:
            pass

    if not serialPortFound:
        print("[ERROR] Couldn't establish connection")
        sys.exit()
    return dev


def getData(dev):
    res = ""
    while res == "":
        dev.flushInput()
        dev.write(str.encode('?\n'))
        res = dev.readline().decode().strip()
    return res

if __name__ == "__main__":
    dev = getDevPort()
    x = getData(dev).split(',')[0]

    if len(sys.argv)==1:
        print(x)
    else:
        print(sys.argv[1], x)
        postData(url, sys.argv[1], x);

