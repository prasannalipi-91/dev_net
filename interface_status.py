from netmiko import ConnectHandler
import subprocess

file = open('D:/MMC-HC/BMS/07_12_2023_Acivity/spanning.csv','r')
file1 = open('D:/MMC-HC/BMS/07_12_2023_Acivity/activity_log_spanning_intcheck.txt','w') ## need to change with a proper name

j = ""
count = 0


def commandset(count):
    file = open('D:/MMC-HC/BMS/07_12_2023_Acivity/python_input.csv','r')
    content = file.readlines()
    i = content[count]
    x = i.split(",")
    command = "default interface " + x[4]
    command1 = "interface " + x[4]
    command2 = "description :: Trunk Port Connected To " + x[5] + " " + x[3] + " Located in L5 ::"
    command3 = "switchport trunk native vlan " + x[2]
    command4 = "switchport trunk allowed vlan " + x[2]
    command5 = "switchport mode trunk"
    command6 = "spanning-tree guard loop"
    command7 = "no shutdown"
    command8 = "do write"
#   check the other commands to be added
    return(command,command1,command2,command3,command4,command5,command6,command7) # add the new commands on return value

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
        }
        command = "show interface " + x[2]
        print(x[0])
#        print(x[3])
#        print(command)
#        print(commandset(count1))
        net_connect = ConnectHandler(**cisco)
        output = net_connect.send_command(command)
#        for lines in output.r
#            print(lines)
#            if "VLAN" in i:
#                k = i.split(" ")
#                print(k[0] +  " " + k[1] + " " + k[2] + " " )
        file1.writelines(x[0] + "," + x[1] + "," + x[2] + "\n")
        file1.writelines(output + "\n")
        print("checking_spanning on " + x[0] + "interface " + x[2])
    else:
        command = "show interface " + x[2]
        output = net_connect.send_command(command)
#        for i in output:
#            if "VLAN" in i:
#                k = i.split(" ")
#                print(k[0] +  " " + k[1] + " " + k[2] + " " )
        file1.writelines(x[0] + "," + x[1] + "," + x[2] + "\n")
        file1.writelines(output + "\n")
        print("checking_spanning on " + x[0] + "interface " + x[2])
file1.close()
file.close()