#!/bin/bash


generate_post_data()
{
  cat <<EOF
{
  "name": "$1",
  "humidity": "$(dht/read_dht.out | sed '2q;d')"
}
EOF
}
curl -i \
-H "Accept: application/json" \
-H "Content-Type:application/json" \
-X POST --data "$(generate_post_data $1)" "http://192.168.1.69:6969/home_api/sensor_humidity"
