#!/usr/bin/python3
import adafruit_dht
import board

import sys
import requests

dht_device = adafruit_dht.DHT11(board.D17)
temperature = dht_device.temperature
humidity = dht_device.humidity

url = "https://home.tigernie.com/home_api/sensor_humidity"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        res = requests.post(url, data={
                                     "name": sys.argv[1],
                                     "humidity": humidity,
                                    })
        print(res)
        print(res.json())
    else:
        print("Temperature: ", temperature)
        print("Humidity: ", humidity)

