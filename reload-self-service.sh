#!/bin/bash

function reload_server() {
   echo "[INFO] Reloading self-service"
   echo "[INFO] Stopping self-service in systemd"
   sudo systemctl stop self-service

   echo "[INFO] Pulling latest repo"
   cd /var/www/ssd_server && git pull
   source ./flask/bin/activate
   pip3 install -r requirements.txt

   echo "[INFO] Restarting systemd service"
   sudo systemctl start self-service

   echo "[INFO] Checking status"
   sudo systemctl status self-service | grep Active:

   echo "[INFO] Waiting for server to initialise"
   sleep 2

   echo "[INFO] Running quick test"
   curl http://127.0.0.1:5100/ssd_api/get_table
}

reload_server
