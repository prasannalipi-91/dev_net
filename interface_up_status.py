from netmiko import ConnectHandler

file = open('D:/MMC-CCTV/B02-03-04to09-ext/hc_device_input.csv','r')
file1 = open('D:/MMC-CCTV/B02-03-04to09-ext/hc_port_status.txt','w')

for i in file:
    x = i.split(",")
    cisco = {
        "device_type": "cisco_ios",
        "host": x[0],
        "username": "mannaiuser1",
        "password": "Cr!cket_2024",
        "secret" : "cisco123"
    }
    try:
        print("checking interface status on  : " + x[0])
        net_connect = ConnectHandler(**cisco)
        net_connect.enable()
        command = "show interface description"
        output = net_connect.send_command(command)
        file1.writelines(i + "\n")
        file1.writelines(output + "\n")
    except:
        print(f"Unable to connect to the device: " + x[0])

