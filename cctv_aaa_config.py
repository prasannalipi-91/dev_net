from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoAuthenticationException
from datetime import date



aaa_log = open('D:/MMC-CCTV/external-ise_pending-log.txt','w')

credentials = [{'user': 'mannaiadmin', 'password' : 'M@nn@iP@ssw0rd'}]


def commandset():
    command_array = []
    file = open('D:/MMC-CCTV/ise-common-config.txt', 'r')
    for i in file:
        command_array.append(i.strip())
    return(command_array) # add the new commands on return value



with open('D:/MMC-CCTV/external-ise-input2.csv', 'r') as file:
    lines = file.readlines()

for i in lines[:-1]:
    x = i.split(",")
    for auth_data in credentials:
        cisco = {
            "device_type": "cisco_ios",
            "host": x[0].strip(),
            "username": auth_data['user'],
            "password": auth_data['password'],
            "secret": "cisco123"
        }
        try:
            net_connect = ConnectHandler(**cisco)
            net_connect.enable()
            command = "write"
            output = net_connect.send_command(command)
            #print("configuring aaa on  :" + x[0])
            print(x[0])
            print(output)
            #aaa_log.writelines(x[0] + "\n" + output + "\n")
            break
        except NetMikoAuthenticationException:
            print("authentication_failed to: " + x[0] + "trying_again")
            continue
        except Exception as e:
            print(f"Unable to connect to the device: " + x[0])
            break


aaa_log.close()