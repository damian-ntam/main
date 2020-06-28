from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.178.23',
    'username': 'cisco',
    'password': 'admin',
}

net_connect = ConnectHandler(**iosv_l2_s1)
output = net_connect.send_command('show version')
print(output)


