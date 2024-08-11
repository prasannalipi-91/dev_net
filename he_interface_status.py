from netmiko import ConnectHandler

file = open('D:/HE/he_device_input1.csv','r')
file1 = open('D:/HE/he_omnicell_re_arrange.txt','w')

for i in file:
    x = i.split(",")
    cisco = {
        "device_type" : "cisco_ios",
        "host" : x[0],
        "username" : "mannaiuser",
        "password" : "M@nn@iP@ssw0rd",
        "secret" : "cisco123",
    }
    counter = 0
    while True:
        counter = counter + 1
        print("ssh attempt number  " + str(counter) + " to " + x[0] )
        try:
            net_connect = ConnectHandler(**cisco)
            net_connect.enable()
            command = "show int des"
            output = net_connect.send_command(command)
            file1.writelines(x[0] + "\n")
            file1.writelines(output + "\n")
            break
        except:
            print("cannot connect")

file1.close()
file.close()

