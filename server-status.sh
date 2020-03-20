#!/bin/bash

# Function takes 1 argument, server address
function check_server() {
   echo "Status of $1 " $(curl -s --head -o /dev/null -w "%{http_code}" $1)
} 

check_server https://tigernie.com
check_server https://home.tigernie.com

