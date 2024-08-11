import re

from netmiko import ConnectHandler

file = open('D:/MMC-CCTV/B02-03-04to09-ext/hc_device_input.csv','r')
file1 = open('D:/Inventory-tool/hc_switch_status.txt','w')

for i in file:
    j = i.split(",")
    cisco = {
        "device_type": "cisco_ios",
        "host": j[0],
        "username": "mannaiuser1",
        "password": "Cr!cket_2024",
        "secret" : "cisco123"
    }
    try:
        net_connect = ConnectHandler(**cisco)
        net_connect.enable()
        command = "show version | i Cisco IOS XE Software"
        output = net_connect.send_command(command)
        file1.writelines(j[0] + "\n" + j[1].strip() + "\n")
        file1.writelines("Reachable \n")
        version_pattern = re.compile(r'\b(\d+\.\d+\.\d+[a-z]?)\b')
        match = version_pattern.search(output)
        version = match.group(0)
        print(version)
        file1.writelines(version + "\n")
        command2 = "show version | i Model Number"
        output = net_connect.send_command(command2)
        model = re.sub("Model Number                       : ", "", output)
        model_array = model.splitlines()
        length = len(model_array)
        if len(model_array) > 1:
            file1.writelines("Stack" + "\n")
            file1.writelines(str(length) + "\n")
            command3 = "show running-config | include provision "
            net_connect.enable()
            output = net_connect.send_command(command3)
            conf_stack = output.splitlines()
            conf_sw = len(conf_stack)
            file1.writelines(str(conf_sw) + "\n")
        else:
            file1.writelines("Not a Stack" + "\n")
            file1.writelines("N/A" + "\n")
            file1.writelines("N/A" + "\n")
        file1.writelines(model_array[0] + "\n")
    except:
        file1.writelines(j[0] + "\n" + j[1].strip() + "\n")
        file1.writelines("Not Reachable \nNA\nNA\nNA\nNA\nNA\n")

        print(f"Unable to connect to the device: " + i)

file1.close()

file1 = open('D:/Inventory-tool/hc_switch_status.txt','r')
file2 = open('D:/Inventory-tool/hc_switch_status_modified.txt','w')

emptyline_pattern = re.compile(r'^\s*$')

for i in file1:
    empty_line_found = False
    if emptyline_pattern.match(i):
        empty_line_found = True
    else:
        file2.writelines(i)
file1.close()
file2.close()





