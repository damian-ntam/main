#!/usr/bin/env python
from jinja2 import Template
__author__  = "Melih TEKE"
__EMAIL__   = "melihteke@gmail.com"

template = Template('''
hostname {{hostname}}
aaa new-model
aaa session-id unique
aaa authentication login default local
aaa authorization exec default local none
vtp mode transparent
vlan 10,20,30,40,50,60,70,80,90,100,200
int {{mgmt_intf}}
no switchport
no shut
ip address {{mgmt_ip}} {{mgmt_subnet}}
''')

all_devices = ['switch1', 'switch2', 'switch3', 'switch4', 'switch5', 'switch6', 'switch7', 'switch8', 'switch9', 'switch10']

sw1 = {'hostname': 'switch1', 'mgmt_intf': 'gig0/0', 'mgmt_ip': '10.10.88.111', 'mgmt_subnet': '255.255.255.0'}

config_parameters = {'switch1': {'hostname':'switch1', 'mgmt_intf':'Gi0/0', 'mgmt_ip':'1.1.1.1','mgmt_subnet':'255.255.255.0'},
                     'switch2': {'hostname':'switch2', 'mgmt_intf':'Gi0/1', 'mgmt_ip':'2.2.2.2','mgmt_subnet':'255.255.255.0'},
                     'switch3': {'hostname':'switch3', 'mgmt_intf':'Gi0/2', 'mgmt_ip':'3.3.3.3','mgmt_subnet':'255.255.255.0'},
                     'switch4': {'hostname':'switch4', 'mgmt_intf':'Gi0/3', 'mgmt_ip':'4.4.4.4','mgmt_subnet':'255.255.255.0'},
                     'switch5': {'hostname':'switch5', 'mgmt_intf':'Gi1/3', 'mgmt_ip':'5.5.5.5','mgmt_subnet':'255.255.255.0'},
                     'switch6': {'hostname':'switch6', 'mgmt_intf':'Gi1/4', 'mgmt_ip':'6.6.6.6','mgmt_subnet':'255.255.255.0'},
                     'switch7': {'hostname':'switch7', 'mgmt_intf':'Gi1/3', 'mgmt_ip':'7.7.7.7','mgmt_subnet':'255.255.255.0'},
                     'switch8': {'hostname':'switch8', 'mgmt_intf':'Gi0/5', 'mgmt_ip':'8.8.8.8','mgmt_subnet':'255.255.255.0'},
                     'switch9': {'hostname':'switch9', 'mgmt_intf':'Gi0/4', 'mgmt_ip':'9.9.9.9','mgmt_subnet':'255.255.255.0'},
                     'switch10': {'hostname':'switch10', 'mgmt_intf':'Gi0/8', 'mgmt_ip':'10.10.10.10','mgmt_subnet':'255.255.255.0'},
                     }

for device in all_devices:
    print(template.render(config_parameters[device]))
    with open("rendered_configuration.txt" , "+a") as f:
        f.write("\n\n\n\n\n")
        f.write(device+"Configuration is being created")
        f.write(template.render(config_parameters[device]))
        f.write("\n------------------------------------------")
        f.close()

print(" ALL CONFIGURATIONS HAVE BEEN COMPLETED ")
