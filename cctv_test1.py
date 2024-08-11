from netmiko import ConnectHandler

file = open('D:/MMC-HC/BMS/07_12_2023_Acivity/python_cctv.csv','r')
file1 = open('D:/MMC-HC/BMS/07_12_2023_Acivity/activity_cctv.txt','w') ## need to change with a proper name

j = ""
count = 0


def commandset(count):
    file = open('D:/MMC-HC/BMS/07_12_2023_Acivity/python_python_cctv.csv','r')
    content = file.readlines()
    i = content[count]
    x = i.split(",")
    command1 = "interface " + x[4]
    command2 = "no shutdown"
 #   command2 = "description :: Trunk Port Connected To " + x[5] + " " + x[3] + " Located in L5 ::"
 ##   command3 = "switchport trunk native vlan " + x[2]
  #  command4 = "switchport trunk allowed vlan " + x[2]
  #  command5 = "switchport mode trunk"
  #  command6 = "spanning-tree guard loop"
  #  command7 = "no shutdown"
  #  command8 = "do write"
#   check the other commands to be added
    return(command1,command2) # add the new commands on return value

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
#        command = "show interface description | i " + x[2]
        print(x[1])
        print(x[3])
#        print(command)
#        print(commandset(count1))
        net_connect = ConnectHandler(**cisco)
        output = net_connect.send_config_set(commandset(count1))
        file1.writelines(output)
        print("Configuring " + x[1] + "interface " + x[4])
    else:
#        command = "show interface description | i " + x[2]
        output = net_connect.send_config_set(commandset(count1))
#        print(command)
        file1.writelines(output)
        print("Configuring " + x[1] + "interface " + x[4])
file1.close()
file.close()