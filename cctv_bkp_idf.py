from netmiko import ConnectHandler
from datetime import date

file = open('D:/MMC-CCTV/CCTV_NW_BKP_11012024/cctv_ips.csv','r')
file1 = open('D:/MMC-CCTV/CCTV_NW_BKP_11012024/CCTV_backup_IDF' + str(date.today()) + '.txt', 'w')


for i in file:
    cisco = {
        "device_type": "cisco_ios",
        "host": i,
        "username": "test_user",
        "password": "P@ssw0rd123",
        "secret": "cisco123"
    }
    net_connect = ConnectHandler(**cisco)
    file2 = open('D:/MMC-CCTV/IDF_commands.txt')
    file1.writelines("######## " + i + "#########")
    print("taking the backups on " + i)
    for j in file2:
        command = j
        output = net_connect.send_command(command, read_timeout=1000)
        file1.writelines("\n")
        file1.writelines(command)
        file1.writelines(output)
        file1.writelines("\n")