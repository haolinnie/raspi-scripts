#!/usr/bin/python3
import adafruit_dht
import board

import sys
import requests

dht_device = adafruit_dht.DHT11(board.D17)
temperature = dht_device.temperature
humidity = dht_device.humidity

#url = "http://192.168.1.69:6969/home_api/room_humidity"
url = "http://127.0.0.1:6969/home_api/room_humidity"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = { "name": sys.argv[1], "value": humidity }
        print(data)
        res = requests.post(url, json=data)
        print(res)
        print(res.json())
    else:
        print("Temperature: ", temperature)
        print("Humidity: ", humidity)

