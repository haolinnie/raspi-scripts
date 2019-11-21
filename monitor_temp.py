#!/usr/bin/python3
import os
import time
import requests


url = "https://home.tigernie.com/home_api/"

def measure_temp():
    temp = float(os.popen("vcgencmd measure_temp").readline().strip().replace("temp=","").split("'")[0])
    return temp


def send_temp():
    name = os.popen("hostname").readline().strip()
    temp = measure_temp()
    res = requests.post(url+"pi_temp",
                        data={
                            "name": name,
                            "temperature": temp
                        }
                        )
    print(res)
    print(res.json())


def print_temp():
    name = os.popen("hostname").readline().strip()
    temp = measure_temp()
    print(name)
    print(temp)


if __name__ == "__main__":
    send_temp()
