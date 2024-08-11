import subprocess
from netmiko import ConnectHandler
from datetime import date
from netmiko.exceptions import NetMikoAuthenticationException

## Creating the MGMT IP ARRAY

ip_array = []
reachable_array = []

for i in range(255):
    ip_array.append("172.20.242." + str(i+1))

#####################
##Checking for the Reachable IPs with PING LIST

for ip in ip_array:
    command = ['ping', ip]
    try:
        output = subprocess.check_output(command, universal_newlines=True)
        reachable_array.append(ip)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Ping command failed with error: {e}")

###################
#Checking the SSH login to get the username

credentials = [{'user' : "mannaiuser1", 'password' : 'Cr!cket_2024' }, {'user' : 'mmcadmin', 'password' : 'cisco123'}]

for i in reachable_ip_list:
    for auth_data in credentials:
        try:
            cisco = {
                "device_type": "cisco_ios",
                "host": i,
                "username": auth_data['user'],
                "password": auth_data['password'],
                "secret": "cisco123"
            }
            net_connect = ConnectHandler(**cisco)
            net_connect.enable()
            hostname = "show running-config | i hostname"
            output = net_connect.send_command(hostname,read_timeout=1000)
            hostname = output.split(" ")
            hostname = hostname[1]
            print(i + " " + hostname)
        except NetMikoAuthenticationException:
            print("authentication_failed to: " + i + "trying_again")
            continue
        except Exception as e:
            print(f"Unable to connect to the device: " + i )
