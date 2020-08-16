#!/usr/bin/env python
__author__      = "Melih TEKE"

def l2_interface_config(vlan,encap):
	print("switchport mode access")
	print("switchport access vlan %s" %(vlan))
	print("switchport encapsulation %s" %(encap))
	print("no shutdown")

def l3_interface_config(ip,mask,mtu):
	print("ip address %s %s" %(ip, mask))
	print("ip mtu %s" %(mtu))
	print("no shutdown")

#Creating interfaces by using list
int = []
for i in range(0,21):
	int.append("1/" + str(i))

#Creating dictionary based on interface number and interface type matching
dic_l2_l3_map = {"1/0" : "l3",
		"1/1" : "l2",
		 "1/2" : "l3",
		 "1/3" : "l2",
		 "1/4" : "l2",
		 "1/5" : "l2",
		 "1/6" : "l2",
		 "1/7" : "l2",
		 "1/8" : "l3",
		 "1/9" : "l2",
		 "1/10" : "l3",
		 "1/11" : "l2",
		 "1/12" : "l2",
		 "1/13" : "l3",
		 "1/14" : "l2",
		 "1/15" : "l2",
		 "1/16" : "l2",
		 "1/17" : "l2",
		 "1/18" : "l2",
		 "1/19" : "l2",
		 "1/20" : "l2"}


#Config generation based on either L2 or L3
for y in int:
	if dic_l2_l3_map[y] == "l2":
		print("interface Ethernet" + y)
		l2_interface_config("100","isl")
	elif dic_l2_l3_map[y] == "l3":
		print("interface Ethernet" + y)
		l3_interface_config("192.168.20.34","255.255.255.0","1500")
	else:
		print("Please specify a correct input")
