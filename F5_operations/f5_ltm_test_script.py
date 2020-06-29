from f5.bigip import ManagementRoot

with open('commands_file.txt') as f:
    commands_list = f.read().splitlines()

with open('devices_file.txt') as f:
    devices_list = f.read().splitlines()

all_devices = []

for device in devices_list:
    mgmt = ManagementRoot(device, 'mteke', 'XXXXXXXXX')
    x = mgmt.tm.util.bash.exec_cmd('run', utilCmdArgs='-c "tmsh show running-config"')
    with open("config_device_"+device+".txt", "w") as f:
        f.write(x.commandResult)
    f.close()
    print(x.commandResult)

print("\n\n\nAll configs are pulled !!!!!!")

