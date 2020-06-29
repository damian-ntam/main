#!/usr/bin/python
__author__ = "Melih TEKE"
__EMAIL__ = "melihteke@gmail.com"
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse
from pprint import pprint

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.178.65',
    'username': 'admin',
    'password': 'cisco',
}


net_connect = ConnectHandler(**iosv_l2_s1)
output = net_connect.send_command('show runn')
print(output)

with open("output.txt", "w") as f:
    f.write(output)
    f.close()
parsed_config = CiscoConfParse("output.txt")

if parsed_config.has_line_with(r"^router ospf"):
    ospf_config = parsed_config.find_all_children(r"^router ospf")

pprint(ospf_config)
