from netmiko import ConnectHandler


file = open('D:/MMC-HC/MOD_PC/device_interface_check.csv','r')
file1 = open('D:/MMC-HC/MOD_PC/interface_status1.txt','w')

j = ""
count = 0

for i in file:
    x = i.split(",")
    count = count + 1
    if x[0] != j:
        if x[0] != j and count != 1:
            net_connect.disconnect()
        j = x[0]
        cisco = {
            "device_type": "cisco_ios",
            "host": x[0],
            "username": "mmcadmin",
            "password": "cisco123",
            "secret" : "cisco123"
        }
        net_connect = ConnectHandler(**cisco)
        net_connect.enable()
        command = "show interface description | in " + x[1].strip()
        output = net_connect.send_command(command)
        file1.writelines(x[0] + "\n")
        file1.writelines(output + "\n")
    else:
        net_connect = ConnectHandler(**cisco)
        net_connect.enable()
        command = "show interface description | in " + x[1].strip()
        output = net_connect.send_command(command)
        file1.writelines(output + "\n")
file.close()
file1.close()

