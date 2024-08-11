import re
import os
#############First Step 1 : collecting the inventory################

from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoAuthenticationException
from datetime import date

attempt = 1
retries = 5

inventory_collect = open('D:/Inventory-tool/hc_device_inventory.txt','w')

#credentials = [{'user': 'mannaiuser', 'password' : 'M@nna@iP@ssw0rd'},{'user': 'mmcadmin', 'password' : 'MMCP@ssw0rd'}]

with open('D:/MMC-CCTV/B02-03-04to09-ext/mmc_he_device_input.csv', 'r') as file:
    lines = file.readlines()

for i in lines[:-1]:
    x = i.split(",")
    attempt = 1
    while attempt < retries:
        attempt = attempt + 1
        for auth_data in credentials:
            cisco = {
                "device_type": "cisco_ios",
                "host": x[0].strip(),
                "username": auth_data['user'],
                "password": auth_data['password'],
                "secret": "MMCP@ssw0rd"
            }
            try:
                net_connect = ConnectHandler(**cisco)
                net_connect.enable()
                command = "show inventory"
                output = net_connect.send_command(command, read_timeout=1000)
                print("collecting inventory from :" + x[0])
                #inventory_collect.writelines(x[0] + "\n" + output + "\n")
                print(output)
                attempt = retries + 1
                break
            except NetMikoAuthenticationException:
                print("authentication_failed to: " + x[0] + "trying_again")
                attempt += 1
                continue
            except Exception as e:
                print(f"Retrying to connect to the device: " + x[0])
                attempt += 1
                break

'''
inventory_collect.close()

#############END OF First Stpe COLLECTING INVENTORY#############


############ Second Step 2: Openning the files generated by data collection############
############And removing the empty lines and write the file in to a new file###########


file = open('D:/Inventory-tool/cctv_device_inventory.txt', 'r')
file1 = open('D:/Inventory-tool/cctv_device_inventory_without_spaces.txt', 'w')


# Removing the empty lines
emptyline_pattern = re.compile(r'^\s*$')

for i in file:
    empty_line_found = False
    if emptyline_pattern.match(i):
        empty_line_found = True
    else:
        file1.writelines(i)
file1.close()
file.close()

############ End of the Second Step ############

############ Third Step 3: Openning the files generated by second step ################
############ Adding the IP address, infront of each line ##############################

with open('D:/Inventory-tool/cctv_device_inventory_without_spaces.txt', 'r') as file:
    lines = file.readlines()

pattern = re.compile(r'^[0-9\.]+') # matching the IP addresses

# Iterate through sections
section_start = 0
section_size = 0
ip_address = []
for index, element in enumerate(lines):
    if pattern.match(element):
        ip_address.append(pattern.match(element).group(0)) # maintaining the previous value of the IP address
        if section_size > 0:
            section_array = lines[section_start:index]
            for i in range(0, len(section_array), 2):
                section_array[i] = ip_address[-2] + "," + section_array[i]
                file2 = open('D:/Inventory-tool/cctv_inventory_with_combined_lines.txt', 'a')
                combinedlines = section_array[i].strip() + "," + section_array[i + 1].strip() + "\n"
                file2.writelines(combinedlines)
        section_start = index+1
        section_size = 0
    else:
        section_size = section_size + 1

file2.close()

##########checking is there any left over section greater than 0 ##############

if section_size > 0:
    section_array = lines[section_start:]
    for i in range(0, len(section_array), 2):
        section_array[i] = ip_address[-1] + "," + section_array[i]
        file2 = open('D:/Inventory-tool/cctv_inventory_with_combined_lines.txt', 'a')
        combined_lines = section_array[i].strip() + "," + section_array[i + 1].strip() + "\n"
        file2.writelines(combined_lines)
    file2.close()

############ End of Third step 3 ###########



############# Step 4 :  ##############################

'''






