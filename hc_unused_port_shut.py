from netmiko import ConnectHandler

file = open('D:/MMC-HC/HC_UNUSED/mod-pc.csv','r')
file1 = open('D:/MMC-HC/HC_UNUSED/MOD-ports-unshut_log.txt','w') ## need to change with a proper name

j = ""
count = 0


def commandset(count):
    command_array = []
    file = open('D:/MMC-HC/HC_UNUSED/mod-pc.csv','r')
    content = file.readlines()
    i = content[count]
    x = i.split(",")
    command_array.append("interface " + x[2])
    command_array.append("no shutdown")
    #file = open('D:/MMC-HC/AVS/common_config.txt', 'r')
    #for i in file:
    #    command_array.append(i.strip())
    return(command_array) # add the new commands on return value

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
            "username" : "mannaiuser1",
            "password" : "Cr!cket_2024",
            "secret" : "cisco123",
        }
#        print(command)
#        print(commandset(count1))
        net_connect = ConnectHandler(**cisco)
        net_connect.enable()
        print("un shutting down ports on : " + x[1])
        output = net_connect.send_config_set(commandset(count1))
        file1.writelines(x[0])
        file1.writelines(output)
        file1.writelines("\n")
    else:
        output = net_connect.send_config_set(commandset(count1))
        file1.writelines(output)
        file1.writelines("\n")
file1.close()
file.close()