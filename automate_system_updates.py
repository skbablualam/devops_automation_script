import os

print("Updating system packages...")
os.system("sudo apt update && sudo apt upgrade -y")
print("System update completed!")
