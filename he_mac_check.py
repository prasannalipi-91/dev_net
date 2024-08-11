from netmiko import ConnectHandler
import re
import os

file = open('D:/HE/he_device_input.csv','r')
file1 = open('D:/HE/he_mac_check.txt','w')

mac_addresses = [
    "8c16.4531.8c58",
    "c018.034e.f4af",
    "3464.a97e.b537",
    "28f1.0e1d.6e98",
    "3464.a97e.a52a",
    "f4ee.08bc.24c0"
]


for i in file:
    x = i.split(",")
    cisco = {
        "device_type" : "cisco_ios",
        "host" : x[0],
        "username" : "mannaiuser",
        "password" : "M@nn@iP@ssw0rd",
        "secret" : "cisco123",
    }
    counter = 0
    while True:
        counter = counter + 1
        print("ssh attempt number  " + str(counter) )
        try:
            net_connect = ConnectHandler(**cisco)
            net_connect.enable()
            for elements in mac_addresses:

                command = "show mac address-table | inc " + elements.strip()
                #print(elements + "   " + command)
                output = net_connect.send_command(command)
                print(x[0] + "\n")
                print(output + "\n")
                #print(output)
            break
        except:
            print("cannot connect")

file1.close()
file.close()