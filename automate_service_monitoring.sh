#!/bin/bash

SERVICE="nginx"

if ! systemctl is-active --quiet "$SERVICE"; then
    echo "$(date) - $SERVICE is down. Restarting..." >> /var/log/service_monitor.log
    systemctl restart "$SERVICE"
    echo "$(date) - $SERVICE restarted." >> /var/log/service_monitor.log
else
    echo "$(date) - $SERVICE is running fine." >> /var/log/service_monitor.log
fi
