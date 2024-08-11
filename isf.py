from netmiko import ConnectHandler
from netmiko import redispatch
import time

file_jump = open('D:/MMC-HC/host_file.csv','r')

cisco = {
    "device_type": "cisco_ios",
    "host": "10.12.4.1",
    "username": "Prasanna",
    "password": "Dialog@123",
    "ssh_config_file": "./ssh_config",
}

for i in file_jump:
    net_connect = ConnectHandler(**cisco)
    print("mdf prompt is : " + format(net_connect.find_prompt()))
    j = i.split(",")
#    print(j[0])
    command = "ssh -l Prasanna 10.1.31.37"
    net_connect.write_channel(command)
    time.sleep(1)
#    output = net_connect.read_channel()
#    print(output)
    print("mdf prompt is : " + format(net_connect.find_prompt()))
#    if "Password" in output:
#        net_connect.write_channel("Dialog@123")
#        command = "show interface description"
#        final_output = net_connect.send_command(command)
#        print(final_output)