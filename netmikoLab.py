from netmiko import ConnectHandler
from getpass import getpass

USERNAME = input("Enter your SSH username: ")
PASSWORD = getpass("Enter your SSH password: ")

device = {
    'ip': '192.168.0.0',
    'username': USERNAME,
    'password': PASSWORD,
    'device_type': 'cisco_ios'
}

c = ConnectHandler(**device)
