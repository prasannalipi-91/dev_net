from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoAuthenticationException
from datetime import date



mac_log = open('D:/MMC-CCTV/B02-03-04to09-ext/log_check.txt','w')

credentials = [{'user': 'mannaiadmin', 'password' : 'M@nn@iP@ssw0rd'}]


def commandset():
    command_array = []
    file = open('D:/MMC-CCTV/B02-03-04to09-ext/authentication_sessions_pre_log.txt', 'r')
    for i in file:
        command_array.append(i.strip())
    return(command_array) # add the new commands on return value



with open('D:/MMC-CCTV/B02-03-04to09-ext/cctv_device_input.csv', 'r') as file:
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
            command = "show authentication sessions"
            output = net_connect.send_command(command)
            mac_log.writelines(x[0] + "\n" + output + "\n")
            print("collecting authentication logs on " + x[0])
            break
        except NetMikoAuthenticationException:
            print("authentication_failed to: " + x[0] + "trying_again")
            continue
        except Exception as e:
            print(f"Unable to connect to the device: " + x[0])
            break


mac_log.close()