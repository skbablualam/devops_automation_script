import os
import subprocess
from datetime import datetime

SERVICE = "nginx"
LOG_FILE = "/var/log/service_monitor.log"

def is_service_running(service):
    status = subprocess.run(["systemctl", "is-active", "--quiet", service])
    return status.returncode == 0

def log_message(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - {message}\n")

if not is_service_running(SERVICE):
    log_message(f"{SERVICE} is down. Restarting...")
    os.system(f"sudo systemctl restart {SERVICE}")
    log_message(f"{SERVICE} restarted successfully.")
else:
    log_message(f"{SERVICE} is running fine.")
