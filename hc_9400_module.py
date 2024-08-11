from netmiko import ConnectHandler
from datetime import date


file = open('D:/MMC-HC/AVS/avs_delta.csv','r')
file1 = open('D:/MMC-HC/AVS/output_rtls.txt','w')

j = ""
count = 0

for i in file:
    x = i.split(",")
    count = count + 1
    count1 = count - 1
    if x[1] != j:
        if x[1] != j and count != 1:
            net_connect.disconnect()
        j = x[1]
        cisco = {
            "device_type" : "cisco_ios",
            "host" : x[1],
            "username" : "mmcadmin",
            "password" : "cisco123",
            "secret" : "cisco123",
        }
        command = "show running-config interface gigabitEthernet " + x[2] + " | i access vlan"
        net_connect = ConnectHandler(**cisco)
        net_connect.enable()
        output = net_connect.send_command(command)
        file1.writelines(x[0] + " " + x[1] + "\n")
        file1.writelines(x[2] + " " + output)
        file1.writelines("\n")
        print("checking vlans on : " + x[1])
    else:
        command = "show running-config interface gigabitEthernet " + x[2] + " | i access vlan"
        output = net_connect.send_command(command)
        file1.writelines(x[2] + " " + output)
        file1.writelines("\n")
file1.close()
file.close()
