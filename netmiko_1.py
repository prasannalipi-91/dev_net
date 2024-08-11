from netmiko import ConnectHandler

file = open('D:/MMC-CCTV/B02-03-04to09-ext/hc_device_input.csv','r')
file1 = open('D:/MMC-HC/AVS/MINI_PC_VLAN.txt','w') ## need to change with a proper name

j = ""
count = 0


def commandset(count):
    file = open('D:/MMC-CCTV/B02-03-04to09-ext/hc_device_input.csv','r')
    content = file.readlines()
    i = content[count]
    x = i.split(",")
    command2 = "vlan 2153"
    command4 = "name VLN_AVS_MINI_PC_2153"
    command9 = "do write"
    return(command2,command4,command9) # add the new commands on return value

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
        try:
            net_connect = ConnectHandler(**cisco)
            net_connect.enable()
            output = net_connect.send_config_set(commandset(count1))
            file1.writelines(x[0])
            file1.writelines(output)
            file1.writelines("\n")
        except:
            print("device is not reachable")
    else:
        output = net_connect.send_config_set(commandset(count1))
        file1.writelines(output)
        file1.writelines("\n")
file1.close()
file.close()