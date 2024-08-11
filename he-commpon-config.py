from netmiko import ConnectHandler

file = open('D:/HE/he-device-all-input.csv','r')
file1 = open('D:/HE/he-device-common_snmp_log.txt','w') ## need to change with a proper name

j = ""
count = 0


def commandset(count):
    command_array = []
    file = open('D:/HE/he-device-all-input.csv','r')
    content = file.readlines()
    i = content[count]
    x = i.split(",")
    #command_array.append("vlan 3600")
    #command_array.append("name HE-CORP")
    #command_array.append("do write")
    #command_array.append("default interface " + x[2])
    #command_array.append("interface " + x[2])
    #command_array.append("description :: " + x[5].strip() + " | " + x[3].strip() + " ::")
    #command_array.append("switchport mode access")
    #command_array.append("switchport access vlan " + x[4].strip())
    #command_array.append("do write")
    file = open('D:/HE/common-config-snmp.txt', 'r')
    for i in file:
        command_array.append(i.strip())
    return(command_array) # add the new commands on return value

#print(commandset(0))
#for i in commandset(0):
#    print(i)



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
            "username" : "mannaiuser",
            "password" : "M@nn@iP@ssw0rd",
            "secret" : "cisco123",
        }
        print(x[1])
#        print(command)
#        print(commandset(count1))
        counter = 0
        while True:
            counter = counter + 1
            print("ssh attempt number  " + str(counter) )
            try:
                net_connect = ConnectHandler(**cisco)
                net_connect.enable()
                break
            except:
                print("cannot connect")
        output = net_connect.send_config_set(commandset(count1))
        file1.writelines("configuring  on : " + x[1] + "-" + x[0])
        print("commiting on : " + x[1] + "-" + x[0])
        print(output)
        file1.writelines(output)
        file1.writelines("\n")
    else:
        output = net_connect.send_config_set(commandset(count1))
        file1.writelines(output)
        #print("configuring the port : " + x[2])
        file1.writelines("\n")
file1.close()
file.close()


