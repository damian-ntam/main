#!/usr/bin/python
__author__  = "Melih TEKE"
__EMAIL__   = "melihteke@gmail.com"

import yaml
from jinja2 import Template

#yaml file is being opened in read-only mode
with open("network_dc.yml", "r") as yaml_file:
  yaml_data = yaml.load(yaml_file)    #yaml file data is converted to python dict


#Creating device templates -  Router template
router_template = Template("""
hostname {{hostname}}
int {{mgmt_intf}}
no shutdown
ip add {{mgmt_ip}} {{mgmt_subnet}}
lldp run
ip domain-name EnterpriseAutomation.net
ip ssh version 2
ip scp server enable
crypto key generate rsa general-keys modulus 1024
snmp-server community public RW
snmp-server trap link ietf
snmp-server enable traps snmp linkdown linkup
snmp-server enable traps syslog
snmp-server manager
logging history debugging
logging snmp-trap emergencies
logging snmp-trap alerts
logging snmp-trap critical
logging snmp-trap errors
logging snmp-trap warnings
logging snmp-trap notifications
logging snmp-trap informational
logging snmp-trap debugging
""")

#Creating device templates -  Switch template
switch_template = Template("""
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
snmp-server community public RW
snmp-server trap link ietf
snmp-server enable traps snmp linkdown linkup
snmp-server enable traps syslog
snmp-server manager
logging history debugging
logging snmp-trap emergencies
logging snmp-trap alerts
logging snmp-trap critical
logging snmp-trap errors
logging snmp-trap warnings
logging snmp-trap notifications
logging snmp-trap informational
logging snmp-trap debugging
\n\n
""")

selection = input(" Do you want the configs also generated as files ? ( select 'Yes' or 'No'")

#Based on our selection the script is either create a config file or only print to screen
if selection.lower() == "yes":
  for device,config in yaml_data['dc1'].items():
    if config['device_template'] == "vIOSL2_Template":
      device_template = switch_template
    elif config['device_template'] == "vIOSL3_Template":
      device_template = router_template
    print("rendering now device {0}" .format(device))
    device_config = device_template.render(config)
    print(device_config)
    print("=" * 30)
    with open("generated_config.txt", "a") as file:
      file.write(device_config)
      file.write("==" *30)
elif selection.lower() == "no":
  print("Your selection is 'No'. The program is being terminated")
else:
  print("Please start the program and enter correct value")






