from netmiko import ConnectHandler


cisco = {
"device_type": "cisco_ios",
"host": "172.20.242.10",
"username": "mmcadmin",
"password": "cisco123",
"secret" : "cisco123"
}
try:
    print("172.20.242.14\n")
    net_connect = ConnectHandler(**cisco)
    command = "show version | i Cisco IOS Software"
    output = net_connect.send_command(command)
    print(output)
    command1 = "show version | i Model Number"
    output = net_connect.send_command(command1)
    print(output)
except:
    print(f"Unable to connect to the device: ")


from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoAuthenticationException

inventory_collect = open('D:/Inventory-tool/hc_device_satus.txt','w')

credentials = [{'user': 'test_user', 'password' : 'P@ssw0rd123'},{'user': 'mmcadmin', 'password' : 'cisco123'}]

with open('D:/Inventory-tool/hc_devices.csv', 'r') as file:
    lines = file.readlines()

for i in lines[:-1]:
    for auth_data in credentials:
        cisco = {
            "device_type": "cisco_ios",
            "host": i.strip(),
            "username": auth_data['user'],
            "password": auth_data['password'],
            "secret": "cisco123"
        }
        try:
            print()
            net_connect = ConnectHandler(**cisco)
            net_connect.enable()
            command = "show version | i Cisco IOS Software"
            output = net_connect.send_command(command)
            print("collecting inventory from :" + i)
            inventory_collect.writelines(i + "\n" + output + "\n")
            break
        except NetMikoAuthenticationException:
            print("authentication_failed to: " + i + "trying_again")
            continue
        except Exception as e:
            print(f"Unable to connect to the device: " + i)
            break


inventory_collect.close()