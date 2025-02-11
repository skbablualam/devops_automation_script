#!/bin/bash

echo "Enter username to create:"
read username

sudo useradd -m -s /bin/bash "$username"
echo "$username:Password123" | sudo chpasswd
echo "User $username created with default password."
