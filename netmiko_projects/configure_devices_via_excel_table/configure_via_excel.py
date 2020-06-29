#!/usr/bin/env python
__author__      = "Melih TEKE"
from netmiko import ConnectHandler
from netmiko.ssh_exception import AuthenticationException, NetMikoTimeoutException
import xlrd
from pprint import pprint

workbook = xlrd.open_workbook(r"sample_device_table.xlsx")
sheet = workbook.sheet_by_index(0)

with open('R55_config') as f:
    R55_config = f.read().splitlines()
with open('Switch64_config') as f:
    Switch64_config = f.read().splitlines()
with open('Switch65_config') as f:
    Switch65_config = f.read().splitlines()
with open('Switch66_config') as f:
    Switch66_config = f.read().splitlines()
with open('Switch67_config') as f:
    Switch67_config = f.read().splitlines()

for index in range(1, sheet.nrows):
    hostname = sheet.row(index)[0].value
    ipaddr = sheet.row(index)[1].value
    username = sheet.row(index)[2].value
    password = sheet.row(index)[3].value
    enable_password = sheet.row(index)[4].value
    vendor = sheet.row(index)[5].value
    config_file = sheet.row(index)[6].value

    device = {
    'device_type': vendor,
    'ip': ipaddr,
    'username': username,
    'password': password,
    'secret': enable_password,
    }

    net_connect = ConnectHandler(**device)


    net_connect.enable()
    #output = net_connect.send_config_from_file(device['config'])
    output = net_connect.send_config_from_file(config_file)
    print("***** show ip configuration of Device *****")
    #output = net_connect.send_command("show ip int b")     #.send_command is used for to send specific command
    print(output)
    net_connect.disconnect()
