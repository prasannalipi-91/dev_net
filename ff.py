file = open('D:/MMC-HC/test1.txt','r')
import paramiko

j = ''

ip_address = "172.20.242.16"
username = "mmcadmin"
password = "cisco123"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

count = 0
for i in file:
    count = count + 1
    x = i.split(',')
    if x[0] != j:
        if x[0] != j and count != 1:
            client.close()
        j = x[0]
        command = "show interface description | i " + x[1]
        client.connect(x[0], username=username, password=password, timeout=20)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        print(x[0])
        print(command)
        print(output)
    else:
        command = "show interface description | i " + x[1]
        client.connect(x[0], username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        print(command)
        print(output)

