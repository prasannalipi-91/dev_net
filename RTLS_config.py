from netmiko import ConnectHandler

file = open('D:/MMC-HC/AVS/avs_rtls_write.csv','r')
file1 = open('D:/MMC-HC/AVS/output_rtls_write.txt','w') ## need to change with a proper name

j = ""
count = 0


def commandset(count):
    file = open('D:/MMC-HC/AVS/avs_delta.csv','r')
    content = file.readlines()
    i = content[count]
    x = i.split(",")
    command1 = "do write"
    return(command1) # add the new commands on return value

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
            "secret" : "cisco123",
        }
        print(x[1])
        net_connect = ConnectHandler(**cisco)
        net_connect.enable()
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