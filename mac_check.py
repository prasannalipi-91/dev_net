from netmiko import ConnectHandler

file = open('D:/MMC-HC/BMS/07_12_2023_Acivity/mac_check_input.csv','r')
file1 = open('D:/MMC-HC/BMS/07_12_2023_Acivity/mac_check_output.txt','w') ## need to change with a proper name



def commandset(count):
    file = open('D:/MMC-HC/BMS/07_12_2023_Acivity/python_inputlevel5.csv','r')
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
    cisco = {
        "device_type" : "cisco_ios",
        "username" : "mmcadmin",
        "host" : x[1],
        "password" : "cisco123",
        }
    command = "show mac address-table | i 008d.f458.b338"
    net_connect = ConnectHandler(**cisco)
    output = net_connect.send_command(command)
    print(output)
    file1.writelines(output)
    print("checking the mac on " + x[0] + "ip address of " + x[1])
    net_connect.disconnect()
file1.close()
file.close()