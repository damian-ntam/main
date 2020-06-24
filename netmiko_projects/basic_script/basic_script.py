from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'f5_bigip',
    'ip': '192.168.178.23',
    'username': 'root',
    'password': 'f5password',
}

net_connect = ConnectHandler(**iosv_l2_s1)
output = net_connect.send_command('cat /config/bigip.conf')
print(output)


