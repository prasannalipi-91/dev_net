from netmiko import ConnectHandler

file = open('D:/MMC-CCTV/B02-03-04to09-ext/test_input.csv','r')
file1 = open('D:/MMC-HC/MOD_PC/interface_status.txt','w') ## need to change with a proper name

j = ""
count = 0


def commandset(count):
    command_array = []
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
            "host" : x[0].strip(),
            "username" : "mmcadmin",
            "password" : "cisco123",
            "secret" : "cisco123",
        }
        print(x[0])
#        print(command)
#        print(commandset(count1))
        net_connect = ConnectHandler(**cisco)
        net_connect.enable()
        command = "show interface description | in " + x[1].strip()
        output = net_connect.send_command(command)
        file1.writelines(x[0] + "\n")
        file1.writelines(output)
        file1.writelines("\n")
    else:
        command = "show interface description | in " + x[1].strip()
        output = net_connect.send_command(command)
        file1.writelines(output)
        file1.writelines("\n")
file1.close()
file.close()