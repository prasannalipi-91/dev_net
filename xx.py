file1 = open('D:/MMC-HC/test.csv','r')
file2 = open('D:/MMC-HC/bkp_log.txt', 'w')

import paramiko

username = "test_user"
password = "P@ssw0rd123"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for j in file1:
    x = j.split(',')
    print("########" + x[0] + "#############")
    print(x[0])
    file = open('D:/MMC-HC/bkp_commands.txt', 'r')
    file2.writelines("########" + x[0] + "#############")
    for i in file:
        client.connect(x[0],username=username,password=password)
        command = i
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        file2.writelines(command)
        file2.writelines(output)
#        print(command)
#        print(output)
    client.close()
