import os

username = input("Enter username to create: ")

os.system(f"sudo useradd -m -s /bin/bash {username}")
os.system(f"echo '{username}:Password123' | sudo chpasswd")

print(f"User {username} created with default password.")
