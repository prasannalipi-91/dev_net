from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoAuthenticationException

file = open('D:/MMC-CCTV/B02-03-04to09-ext/hc_device_input.csv','r')
file1 = open('D:/MMC-HC/hc_network_logs.txt','w') ## need to change with a proper name

j = ""
count = 0


def commandset(count):
    command_array = []
    file = open('D:/MMC-CCTV/B02-03-04to09-ext/hc_device_input.csv','r')
    content = file.readlines()
    i = content[count]
    x = i.split(",")
    file = open('D:/MMC-CCTV/B02-03-04to09-ext/hc_common_config.txt', 'r')
    for i in file:
        command_array.append(i.strip())
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
            "username" : "mannaiuser1",
            "password" : "Cr!cket_2024",
            "secret" : "cisco123",
        }
        try:
            print(x[0])
            net_connect = ConnectHandler(**cisco)
            net_connect.enable()
            output = net_connect.send_config_set(commandset(count1))
            file1.writelines(x[0])
            file1.writelines(output)
            print(output)
            file1.writelines("\n")
        except Exception as e:
            print(f"Unable to connect to the device: " + x[0])
            continue
    else:
        output = net_connect.send_config_set(commandset(count1))
        file1.writelines(output)
        file1.writelines("\n")
file1.close()
file.close()