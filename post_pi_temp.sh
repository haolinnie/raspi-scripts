
generate_post_data()
{
  cat <<EOF
{
  "name": "$(hostname)",
  "value": "$(vcgencmd measure_temp | tr "=|'" "\n" | sed "2q;d")"
}
EOF
}
curl -i \
-H "Accept: application/json" \
-H "Content-Type:application/json" \
-X POST --data "$(generate_post_data)" "http://192.168.1.69:6969/home_api/server_temp"
