from netmiko import ConnectHandler

file = open('D:/MMC-HC/BMS/07_12_2023_Acivity/check_1.csv','r')
file1 = open('D:/MMC-HC/BMS/07_12_2023_Acivity/activity_log_bms_check.txt','w') ## need to change with a proper name

j = ""
count = 0

for i in file:
    x = i.split(",")
    cisco = {
        "device_type" : "cisco_ios",
        "host" : x[0],
        "username" : "mmcadmin",
        "password" : "cisco123",
    }
    command = "show interface description | i Trunk"
    print(x[0])
    net_connect = ConnectHandler(**cisco)
    file1.writelines("\n")
    file1.writelines(format(net_connect.find_prompt()))
    file1.writelines("\n")
    file1.writelines(command)
    file1.writelines("\n")
    output = net_connect.send_command(command)
    file1.writelines(output)
    net_connect.disconnect()

