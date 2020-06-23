from netmiko import ConnectHandler

#Created the device dictionaries.
iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.178.66',
    'username': 'admin',
    'password': 'cisco',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.178.67',
    'username': 'admin',
    'password': 'cisco',
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.178.68',
    'username': 'admin',
    'password': 'cisco',
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.178.69',
    'username': 'admin',
    'password': 'cisco',
}

iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.178.71',
    'username': 'admin',
    'password': 'cisco',
}

with open('iosv_l2_cisco_access.txt') as f:
    lines = f.read().splitlines()
print (lines)

#Access layer device list
all_devices = [iosv_l2_s3, iosv_l2_s4, iosv_l2_s6]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)


with open('iosv_l2_distribution.txt') as f:
    lines = f.read().splitlines()
print (lines)

#Distribution layer device list
all_devices = [iosv_l2_s2, iosv_l2_s5]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

