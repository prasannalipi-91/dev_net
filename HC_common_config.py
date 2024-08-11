from netmiko import ConnectHandler


file = open('D:/MMC-CCTV/B02-03-04to09-ext/hc_device_input.csv', 'r')
file2 = open('D:/MMC-HC/hc_common_standard_log.txt', 'w')


def common_config():
    command_array = []
    file1 = open('D:/MMC-HC/hc-idf-common-standard-config.txt', 'r')
    for i in file1:
        command_array.append(i.strip())
    return(command_array)


for i in file:
    x = i.split(",")
    cisco = {
        "device_type": "cisco_ios",
        "host": x[0].strip(),
        "username": "mannaiuser1",
        "password": "Cr!cket_2024",
        "secret": "cisco123",
    }
    try:
        net_connect = ConnectHandler(**cisco)
        net_connect.enable()
        print("configuring on : " + x[0] + "-" + x[1])
        output = net_connect.send_config_set(common_config())
        print(output)
        file2.writelines(x[0] + "\n")
        file2.writelines(output)

    except:
        print("cannot connect to the device : " + x[0] + "-" + x[1])