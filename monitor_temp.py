#!/usr/bin/python3
"""
Read the CPU temperature of a linux system
and post the data to an endpoint
"""
import glob
import requests

url = "http://192.168.1.81:6613/home_api/"


def read_cpu_temp():
    # Read all cpu temperature data files
    cpu_temp_files = glob.glob("/sys/class/thermal/thermal_zone*/temp")
    data = []
    for cpu_temp_file in cpu_temp_files:
        with open(cpu_temp_file) as file_handle:
            raw = file_handle.read().strip()
            data.append(float(raw)/1000)

    # calculate mean temperature
    temp_sum = 0
    for d in data:
        temp_sum += d

    temp = temp_sum / len(data)
    return temp

def read_hostname():
    with open("/etc/hostname") as file_handle:
        name = file_handle.read().strip()

    return name


if __name__ == "__main__":
    temp = read_cpu_temp()
    print(temp)
    name = read_hostname()
    print(name)
    res = requests.post(url + "server_temp",
                        json={
                            "name": name,
                            "value": temp
                        }
                        )
    print(res.json())
