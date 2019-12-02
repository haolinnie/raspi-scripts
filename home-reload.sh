#!/bin/bash

function reload_server() {
   echo "[INFO] Stopping service in systemd"
   sudo systemctl stop home-service

   echo "[INFO] Pulling latest repo"
   cd /var/www/home-service-v2 && git pull

   echo "[INFO] Restarting systemd service"
   sudo systemctl start home-service

   echo "[INFO] Checking status"
   sudo systemctl status home-service | grep Active:

   echo "[INFO] Waiting for server to initialise"
   sleep 2

   echo "[INFO] Running quick test"
   curl http://127.0.0.1:6969/home_api/sensor_temp?n=10
}

reload_server
