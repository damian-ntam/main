#!/usr/bin/python
__author__ = "Melih TEKE"
__EMAIL__ = "melihteke@gmail.com"
import paramiko
import time
Channel = paramiko.SSHClient()
Channel.set_missing_host_key_policy(paramiko.AutoAddPolicy())
Channel.connect(hostname="192.168.178.66", username='admin', password='cisco', look_for_keys=False,allow_agent=False)
shell = Channel.invoke_shell()
shell.send("enable\n")
shell.send("cisco\n")
shell.send("terminal length 0\n")
shell.send("show ip int b\n")
shell.send("show arp \n")
time.sleep(2)
print shell.recv(100)
Channel.close()