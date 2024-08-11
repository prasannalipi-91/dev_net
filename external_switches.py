from netmiko import ConnectHandler

file = open('D:/MMC-CCTV/B02-03-04to09-ext/device_input.csv','r')
file2 = open('D:/MMC-CCTV/B02-03-04to09-ext/mac_address_details.csv','r')
file3 = open('D:/MMC-HC/BMS/07_12_2023_Acivity/activity_cctv_B01-B04_ext.txt','w') ## need to change with a proper name

j = ""
count = 0


for i in file:
    cisco = {
        "device_type": "cisco_ios",
        "host": i,
        "username": "mmcadmin",
        "password": "cisco123",
    }
    print("checking mac address on : " + i)
    net_connect = ConnectHandler(**cisco)
    file3.writelines(i + "\n")
    for j in file2:
        file2 = open('D:/MMC-CCTV/B02-03-04to09-ext/mac_address_details.csv', 'r')
        command = "show mac address-table | i " + j
        output = net_connect.send_command(command)
        file3.writelines(output + "\n")
    net_connect.disconnect()

