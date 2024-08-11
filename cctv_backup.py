from netmiko import ConnectHandler
from datetime import date
from netmiko.exceptions import NetMikoAuthenticationException

file = open('D:/MMC-CCTV/B02-03-04to09-ext/cctv_device_input.csv','r')
file1 = open('D:/MMC-CCTV/cctv_IDF_backups_' + str(date.today()) + '.txt', 'w')

credentials = [{'user': 'test_user', 'password' : 'P@ssw0rd123'},{'user': 'mmcadmin', 'password' : 'cisco123'}]

for i in file:
    for auth_data in credentials:
        try:
            x = i.split(",")
            cisco = {
                "device_type": "cisco_ios",
                "host": x[0],
                "username": auth_data['user'],
                "password": auth_data['password'],
                "secret": "cisco123"
            }
            print('\n')
            print(x[0])
            net_connect = ConnectHandler(**cisco)
            net_connect.enable()
            net_connect.conn_timeout = 1000
            hostname = "show running-config | i hostname"
            output = net_connect.send_command(hostname,read_timeout=1000)
            hostname = output.split(" ")
            hostname = hostname[1]
            print(f"{hostname : ^20}")
            file2 = open('D:/MMC-HC/cctv_idf_bkp_commands.txt', 'r')
            file1.writelines("##################################################" + "\n" + "#################" + hostname + "#####################" + "\n" + "##################################################" + "\n")
            print(f"Processing devices that don't match specific IPs. File2 content:")
            for j in file2:
                command = j
                print(f"Command from file2: {j.strip()}")
                output = net_connect.send_command(command,read_timeout=1000)
                file1.writelines(hostname + "#" + command)
                file1.writelines("\n")
                file1.writelines(output)
                file1.writelines("\n" + "\n")
            file1.writelines("------------------END-----------------------------" + "\n")
            file2.close()
        except NetMikoAuthenticationException:
            print("authentication_failed to: " + i + "trying_again")
            continue
        except Exception as e:
            print(f"Unable to connect to the device: " + x[0])
        finally:
            net_connect.disconnect()
file1.close()
file.close()
