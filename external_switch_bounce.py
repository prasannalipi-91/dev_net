from netmiko import ConnectHandler

file = open('D:/MMC-CCTV/B02-03-04to09-ext/device_input.csv','r')
file1 = open('D:/MMC-CCTV/B02-03-04to09-ext/port_bounce.txt','w')

for i in file:
    cisco = {
        "device_type": "cisco_ios",
        "host": i,
        "username": "mmcadmin",
        "password": "cisco123",
        }
    print("bouncing ports on " + i)
    net_connect = ConnectHandler(**cisco)
    output = net_connect.send_config_set(["interface range Gi1/3-10","shutdown","no shutdown"])
    file1.writelines( i + "\n" + output + "\n")


