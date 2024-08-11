from netmiko import ConnectHandler

file = open('D:/MMC-HC/BMS/14_12_2023_Activity_shut/port_shut_list1.csv','r')
file1 = open('D:/MMC-HC/BMS/14_12_2023_Activity_shut/port_shut_log_30042024.txt','w') ## need to change with a proper name

j = ""
count = 0


def commandset(count):
    file = open('D:/MMC-HC/BMS/14_12_2023_Activity_shut/port_shut_list1.csv','r')
    content = file.readlines()
    i = content[count]
    x = i.split(",")
    command1 = "interface " + x[3].strip()
    #command2 = "shutdown"
    command3 = "description :: Access Port Connected To BMS_LOOP SHUT " + x[0].strip() + " ::"
#    command3 = "do write"
#   check the other commands to be added
    return(command1,command3) # add the new commands on return value

for i in file:
    x = i.split(",")
    count = count + 1
    count1 = count - 1
    if x[2] != j:
        if x[2] != j and count != 1:
            commit = net_connect.send_command("write")
            file1.writelines(commit)
            net_connect.disconnect()
        j = x[2]
        cisco = {
            "device_type" : "cisco_ios",
            "host" : x[2].strip(),
            "username" : "mannaiuser1",
            "password" : "Cr!cket_2024",
            "secret" : "cisco123"
        }
        print(x[2])
        net_connect = ConnectHandler(**cisco)
        net_connect.enable()
        output = net_connect.send_config_set(commandset(count1))
        file1.writelines(output)
        print("shutting down the bms port of " + x[2] + " interface " + x[3])
    else:
#        command = "show interface description | i " + x[2]
        output = net_connect.send_config_set(commandset(count1))
#        print(command)
        file1.writelines(output)
        print("shutting down the bms port of " + x[2] + " interface " + x[3])
file1.close()
file.close()