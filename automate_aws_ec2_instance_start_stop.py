import boto3

ec2 = boto3.client('ec2')
INSTANCE_ID = "i-0abcd1234efgh5678"

action = input("Enter 'start' or 'stop' EC2 instance: ").strip().lower()

if action == "start":
    ec2.start_instances(InstanceIds=[INSTANCE_ID])
    print(f"EC2 instance {INSTANCE_ID} started.")
elif action == "stop":
    ec2.stop_instances(InstanceIds=[INSTANCE_ID])
    print(f"EC2 instance {INSTANCE_ID} stopped.")
else:
    print("Invalid action!")
