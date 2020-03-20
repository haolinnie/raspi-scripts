#!/usr/bin/python3
import os
import sys
import requests

url = "https://home.tigernie.com/home_api/room_humidity"

def read_dht():

    with os.popen("./dht/read_dht.out") as p:
        res = p.read()

    if res:
        res = res.split("\n")
        return res[:2]

    return None


if __name__ == "__main__":

    temp, humi = read_dht()
    humi = float(humi)

    if len(sys.argv) > 1:

        res = requests.post(url, json={"name": sys.argv[1], "value": humi})
        print(res)
        print(res.json())

    else:
        print("Temperature: ", temp)
        print("Humidity: ", humi)

