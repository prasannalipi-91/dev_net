import re

from netmiko import ConnectHandler

file = open('D:/MMC-HC/AVS/avs_input.csv','r')
file1 = open('D:/MMC-HC/AVS/RTLS_vlan.txt','w')

for i in file:
    j = i.split(",")
    cisco = {
        "device_type": "cisco_ios",
        "host": j[1],
        "username": "mmcadmin",
        "password": "cisco123",
        "secret" : "cisco123"
    }
    try:
        net_connect = ConnectHandler(**cisco)
        net_connect.enable()
        command = "show running-config interface gigabitEthernet " + j[2] + " | i access vlan"
        output = net_connect.send_command(command)
        file1.writelines(j[0] + "\n" + j[1].strip() + "\n")
        file1.writelines(output + "\n")

    except:
        file1.writelines(j[0] + "\n" + j[1].strip() + "\n")
        file1.writelines("Not Reachable \nNA\nNA\nNA\nNA\nNA\n")

        print(f"Unable to connect to the device: " + i)

file1.close()

file1 = open('D:/Inventory-tool/hc_switch_status.txt','r')
file2 = open('D:/Inventory-tool/hc_switch_status_modified.txt','w')

emptyline_pattern = re.compile(r'^\s*$')

for i in file1:
    empty_line_found = False
    if emptyline_pattern.match(i):
        empty_line_found = True
    else:
        file2.writelines(i)
file1.close()
file2.close()