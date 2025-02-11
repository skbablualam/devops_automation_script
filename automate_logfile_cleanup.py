import os
import time

LOG_DIR = "/var/log"
DAYS = 7
now = time.time()

print(f"Deleting log files older than {DAYS} days...")

for file in os.listdir(LOG_DIR):
    file_path = os.path.join(LOG_DIR, file)
    if os.path.isfile(file_path) and file.endswith(".log"):
        if os.stat(file_path).st_mtime < now - (DAYS * 86400):
            os.remove(file_path)
            print(f"Deleted: {file_path}")

print("Log cleanup completed!")
