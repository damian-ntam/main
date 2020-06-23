
#!/bin/python3

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.178.64',
    'username': 'admin',
    'password': 'cisco'
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.178.65',
    'username': 'admin',
    'password': 'cisco'
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.178.66',
    'username': 'admin',
    'password': 'cisco'
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.178.67',
    'username': 'admin',
    'password': 'cisco'
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.178.68',
    'username': 'admin',
    'password': 'cisco'
}

iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.178.69',
    'username': 'admin',
    'password': 'cisco'
}

iosv_l2_s7 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.178.71',
    'username': 'admin',
    'password': 'cisco'
}



all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3, iosv_l2_s4, iosv_l2_s5, iosv_l2_s6, iosv_l2_s7]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_command('show runn')
    print (output)

    with open("generate_config_"+str(devices['ip']), "w") as f:
        print("GENERATE CONFIG IS BEING SAVED TO FILE!!!")
        f.write(output)
    f.close()

