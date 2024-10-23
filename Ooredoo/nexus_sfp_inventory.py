import re
import os
from netmiko import ConnectHandler

'''
##########Login to Each Device and Collecting the  SFP Details##############
########## For the Moment I have commented this, we can remove the comment when th actual process start

inventory_collect = open('D:/QR_IAAS/QR_Inventory automation/inventory_input.txt','w')

with open('D:/QR_IAAS/QR_Inventory automation/nexus_device_input_list.csv', 'r') as file:
    lines = file.readlines()

for i in lines[:-1]:
    x = i.split(",")
    cisco = {
        "device_type": "cisco_nexus",
        "host": x[0].strip(),
        "username": "username", # Update the Proper username, password and secret.
        "password": "password",
        "secret": "secret"
    }
    try:
        net_connect = ConnectHandler(**cisco)
        net_connect.enable()
        command = "show inventory" ## replace with the proper command
        output = net_connect.send_command(command, read_timeout=1000)
        print("collecting inventory from :" + x[0])
        inventory_collect.writelines(x[0] + "#" + x[1].strip() + "\n" + output + "\n")
        #break
        #except NetMikoAuthenticationException:
        #    print("authentication_failed to: " + x[0] + "trying_again")
        #    continue
    except Exception as e:
        print(f"Unable to connect to the device: " + x[0])
        #    break


inventory_collect.close()

#########################END OF THE DATA COLLECTION############################

'''

file = open('D:/QR_IAAS/QR_Inventory automation/inventory_input.txt','r')
file1 = open('D:/QR_IAAS/QR_Inventory automation/inventory_output.txt','w')
#file2 = open('D:/Inventory automation/inventory_output1.txt','w')
file3 = open('D:/QR_IAAS/QR_Inventory automation/inventory_final.txt','a')
file4 = open('D:/QR_IAAS/QR_Inventory automation/inventory_final1.csv','w')

start_pattern = re.compile(r'^\s*(SFP Detail)')
end_pattern = re.compile(r'^\s*(Note:)')
empty_line_pattern = re.compile(r'^\s*$')
Inside_text =  False


## filtering the required patterns

filter_pattern = re.compile(r'^[0-9\.]+|^(Ethernet)|^\s*(transceiver is)|^\s*(serial number is)|^\s*(cisco product id is)')

for i in file:
    if filter_pattern.match(i):
        file1.writelines(i)

file1.close()


with open('D:/QR_IAAS/QR_Inventory automation/inventory_output.txt','r') as file:
    lines = file.readlines()


    section_start = 0
    section_size = 0
    section_array = []
    matched_count = 0

    pattern = re.compile(r'^[0-9\.]+(#)[A-Z0-9\-]+')
    interface_Pattern = re.compile(r'^(Eth)')

    for index, value in enumerate(lines):
        if pattern.match(value):
            matched_count = matched_count + 1
            if section_size > 0:
                section_array = lines[section_start:index]
                section_array = [ip_address] + section_array
                for i in range(0, len(section_array)):
                    section_array[i] = re.sub(r'#', ",", section_array[i])
                    section_array[i] = re.sub(r'\s{4,}', "", section_array[i])
                    section_array[i] = re.sub(r'(transceiver is )', "", section_array[i])
                    section_array[i] = re.sub(r'(serial number is )', "", section_array[i])
                    section_array[i] = re.sub(r'(cisco product id is )', "", section_array[i])
                for i in range(0, len(section_array)):
                    file3 = open('D:/QR_IAAS/QR_Inventory automation/inventory_final.txt', 'a')
                    write_line = section_array[i].strip() + ","
                    file3.writelines(write_line)
                file3 = open('D:/QR_IAAS/QR_Inventory automation/inventory_final.txt', 'a')
                file3.writelines("\n")
            ip_address = pattern.match(value).group(0)
            section_start = index + 1
            section_size = 0
        if interface_Pattern.match(value):
            if section_size > 0:
                section_array = lines[section_start:index]
                section_array = [ip_address] + section_array
                for i in range(0, len(section_array)):
                    section_array[i] = re.sub(r'#', ",", section_array[i])
                    section_array[i] = re.sub(r'\s{4,}', "", section_array[i])
                    section_array[i] = re.sub(r'(transceiver is )', "", section_array[i])
                    section_array[i] = re.sub(r'(serial number is )', "", section_array[i])
                    section_array[i] = re.sub(r'(cisco product id is )', "", section_array[i])
                for i in range(0, len(section_array)):
                    file3 = open('D:/QR_IAAS/QR_Inventory automation/inventory_final.txt','a')
                    write_line = section_array[i].strip() + ","

                    file3.writelines(write_line)
                file3 = open('D:/QR_IAAS/QR_Inventory automation/inventory_final.txt', 'a')
                file3.writelines("\n")
                #print(section_array)
                section_start = index
            section_size = section_size + 1

if section_size > 0:
    section_array = lines[section_start:index+1]
    section_array = [ip_address] + section_array
    for i in range(0, len(section_array)):
        section_array[i] = re.sub(r'#',",", section_array[i])
        section_array[i] = re.sub(r'\s{4,}', "", section_array[i])
        section_array[i] = re.sub(r'(transceiver is )', "", section_array[i])
        section_array[i] = re.sub(r'(serial number is )', "", section_array[i])
        section_array[i] = re.sub(r'(cisco product id is )', "", section_array[i])
    for i in range(0, len(section_array)):
        file3 = open('D:/QR_IAAS/QR_Inventory automation/inventory_final.txt', 'a')
        write_line = section_array[i].strip() + ","
        file3.writelines(write_line)
    file3 = open('D:/QR_IAAS/QR_Inventory automation/inventory_final.txt', 'a')
    file3.writelines("\n")

os.remove('D:/QR_IAAS/QR_Inventory automation/inventory_output.txt')

file4.writelines("Device_IP,Hostname,Interface,Serial_Number,Part_ID" + "\n")

with open('D:/QR_IAAS/QR_Inventory automation/inventory_final.txt') as file:
    lines = file.readlines()
    for i in lines:
        line_items = i.split(",")
        if line_items[3] == "not present":
            no_sfp = True
        else:
            line_items.pop(3)
            del line_items[-1]
            list(map(str,line_items))
            join_line = ",".join(line_items)
            file4.writelines(join_line + "\n")
file4.close()
file3.close()

os.remove('D:/QR_IAAS/QR_Inventory automation/inventory_final.txt')

