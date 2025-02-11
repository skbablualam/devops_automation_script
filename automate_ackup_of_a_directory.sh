#!/bin/bash

SOURCE_DIR="/home/user/data"
BACKUP_DIR="/home/user/backup"
DATE=$(date +"%Y-%m-%d")
BACKUP_FILE="$BACKUP_DIR/data_backup_$DATE.tar.gz"

echo "Creating backup..."
tar -czf "$BACKUP_FILE" "$SOURCE_DIR"
echo "Backup saved at $BACKUP_FILE"
