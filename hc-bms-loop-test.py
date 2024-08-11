from netmiko import ConnectHandler
import re

file = open('D:/MMC-CCTV/B02-03-04to09-ext/hc_device_input.csv','r')
file1 = open('D:/MMC-CCTV/B02-03-04to09-ext/hc_bms_loop_status.txt','w')

for i in file:
    x = i.split(",")
    cisco = {
        "device_type": "cisco_ios",
        "host": x[0],
        "username": "mannaiuser1",
        "password": "Cr!cket_2024",
        "secret" : "cisco123"
    }
    try:
        print("checking interface status on  : " + x[0])
        net_connect = ConnectHandler(**cisco)
        net_connect.enable()
        command = "show cdp neighbors"
        output = net_connect.send_command(command)
        file1.writelines(i + "\n")
        file1.writelines(output + "\n")
    except:
        print(f"Unable to connect to the device: " + x[0])

file1.close()


pattern = re.compile(r'\b[\w-]+-ACC-SW-\w+\b')
pattern1 = re.compile(r'^[0-9\.]+')

with open('D:/MMC-CCTV/B02-03-04to09-ext/hc_bms_loop_status.txt','r') as file:
    lines = file.readlines()

for index, element in enumerate(lines):
    if pattern1.match(element):
        ip_address = pattern1.match(element).group(0)
    if pattern.match(element):
        next_index = index + 1
        print(ip_address + "," +  element.strip() + lines[next_index])


