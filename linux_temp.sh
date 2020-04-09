cat /sys/class/thermal/thermal_zone*/temp | awk '{ print ($1 / 1000) }'
