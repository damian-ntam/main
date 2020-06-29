from getpass import getpass
from netmiko import ConnectHandler
#Couldnt not make this worked by using connecthandler !!!!!!!!
#username = input('Enter your SSH username: ')
#password = getpass()

with open('commands_file.txt') as f:
    commands_list = f.read().splitlines()

with open('devices_file.txt') as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    print ('Connecting to device" ' + devices)
    ip_address_of_device = devices

    f5_device = {
        'device_type': 'f5_ltm',
        'ip': ip_address_of_device, 
        'username': 'mteke',
        'password': 'XXXXXXXXXX'
    }

    net_connect = ConnectHandler(**f5_device)
    output = net_connect.send_config_set(commands_list)
    print (output)

