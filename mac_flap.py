from netmiko import ConnectHandler
import re
import os

file = open('D:/MMC-HC/BMS/07_12_2023_Acivity/mac_flap_input.csv','r')
file1 = open('D:/MMC-HC/BMS/07_12_2023_Acivity/mac_flap_check.txt','w')

cisco = {
    "device_type": "cisco_ios",
    "host": "172.20.242.1",
    "username": "mannaiuser1",
    "password": "Cr!cket_2024",
    "secret": "cisco123"
}
net_connect = ConnectHandler(**cisco)
net_connect.enable()

for i in file:
    j = i.split(",")
    command1 = "show logg | i " +  j[0].strip()
    #command2 = "name VLN_Careinn_EP_2169"
    #command3 = "do write"
    output = net_connect.send_command(command1)
    file1.writelines(command1 + "\n")
    file1.writelines(output + "\n")
    print("cheking on " + j[0])

file1.close()