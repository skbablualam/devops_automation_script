import os
import tarfile
from datetime import datetime

SOURCE_DIR = "/home/user/data"
BACKUP_DIR = "/home/user/backup"
DATE = datetime.now().strftime("%Y-%m-%d")
BACKUP_FILE = f"{BACKUP_DIR}/data_backup_{DATE}.tar.gz"

print("Creating backup...")

with tarfile.open(BACKUP_FILE, "w:gz") as tar:
    tar.add(SOURCE_DIR, arcname=os.path.basename(SOURCE_DIR))

print(f"Backup saved at {BACKUP_FILE}")
