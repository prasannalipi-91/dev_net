from netmiko import ConnectHandler

file = open('D:/MMC-HC/B03-MEETING/b03_meeting_input.csv','r')
file1 = open('D:/MMC-HC/B03-MEETING/b03_meeting_post_interface_status,txt','w') ## need to change with a proper name

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
    if x[1] != j:
        if x[1] != j and count != 1:
            net_connect.disconnect()
        j = x[1]
        cisco = {
            "device_type" : "cisco_ios",
            "host" : x[1].strip(),
            "username" : "mannaiuser1",
            "password" : "Cr!cket_2024",
            "secret" : "cisco123",
        }
        print(x[1])
#        print(command)
#        print(commandset(count1))
        net_connect = ConnectHandler(**cisco)
        net_connect.enable()
        command = "show interface description | in " + x[2].strip()
        output = net_connect.send_command(command)
        file1.writelines(x[0] + "\n")
        file1.writelines(output)
        file1.writelines("\n")
    else:
        command = "show interface description | in " + x[2].strip()
        output = net_connect.send_command(command)
        file1.writelines(output)
        file1.writelines("\n")
file1.close()
file.close()