#!/usr/bin/python
__author__ = "Melih TEKE"
__EMAIL__ = "melihteke@gmail.com"

#This script shows all router ospf process for listed devices in the network.

from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse
from pprint import pprint

#created list of the devices
ip_address = ["192.168.178.64", "192.168.178.66", "192.168.178.67", "192.168.178.68", "192.168.178.69"]


#login to device with for loop
for ip in ip_address:
    iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': ip,
    'username': 'admin',
    'password': 'cisco',}
    net_connect = ConnectHandler(**iosv_l2_s1)
    output = net_connect.send_command('show runn')
    #print(output)

    with open("output.txt", "w") as f:
        f.write(output)
        f.close()
    parsed_config = CiscoConfParse("output.txt") #configuration is parsed
    pprint(ip+" is being parsed")
    if parsed_config.has_line_with(r"^router ospf"):
        ospf_config = parsed_config.find_all_children(r"^router ospf")
        pprint(ospf_config)
