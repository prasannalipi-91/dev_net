from netmiko import ConnectHandler

file = open('D:/MMC-HC/BMS_PDU/PDU_input.csv','r')
file1 = open('D:/MMC-HC/BMS_PDU/bms-pdu-config.txt','w') ## need to change with a proper name

j = ""
count = 0


def commandset(count):
    command_array = []
    file = open('D:/MMC-HC/BMS_PDU/PDU_input.csv', 'r')
    content = file.readlines()
    i = content[count]
    x = i.split(",")
    command_array.append("default interface " + x[1])
    command_array.append("interface " + x[1])
    command_array.append("description :: Access Port Connected To BMS-UPS " + x[2].strip() + " ::")
    file = open('D:/MMC-HC/BMS_PDU/common_config.txt', 'r')
    for i in file:
        command_array.append(i.strip())
    command_array.append("switchport access vlan " + x[3].strip())
    command_array.append("do write")
    return(command_array) # add the new commands on return value

for i in file:
    x = i.split(",")
    count = count + 1
    count1 = count - 1
    if x[0] != j:
        if x[0] != j and count != 1:
            net_connect.disconnect()
        j = x[0]
        cisco = {
            "device_type" : "cisco_ios",
            "host" : x[0],
            "username" : "mmcadmin",
            "password" : "cisco123",
            "secret" : "cisco123",
        }
        print(x[0])
#        print(command)
#        print(commandset(count1))
        net_connect = ConnectHandler(**cisco)
        net_connect.enable()
        output = net_connect.send_config_set(commandset(count1))
        file1.writelines(x[0] + "\n")
        file1.writelines(output)
        file1.writelines("\n")
    else:
        output = net_connect.send_config_set(commandset(count1))
        file1.writelines(output)
        file1.writelines("\n")
file1.close()
file.close()