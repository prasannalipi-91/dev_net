import re
import os
import pandas as pd
from datetime import date

'''
##########Login to Each Device and Collecting the  INVENTORY Details##############
########## For the Moment I have commented this, we can remove the comment when th actual process start

inventory_collect = open('D:/QR_IAAS/QR_Inventory automation/sw_inventory_input.txt','w')

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
        inventory_collect.writelines(x[0] + "," + x[1].strip() + "\n" + output + "\n")
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

file = open('D:/QR_IAAS/QR_Inventory automation/sw_inventory_input.txt','r')
file1 = open('D:/QR_IAAS/QR_Inventory automation/sw_inventory_output.txt','w')

today = date.today()


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


with open('D:/QR_IAAS/QR_Inventory automation/sw_inventory_output.txt', 'r') as file:
    lines = file.readlines()

pattern = re.compile(r'^[0-9\.]+[\,\_A-Za-z\-0-9]+') # matching the IP addresses

#####Test Field#####

#for index, element in enumerate(lines):
#    if pattern.match(element):
#        ip_add = pattern.match(element).group(0)
#        print(ip_add)


####################


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
                file2 = open('D:/QR_IAAS/QR_Inventory automation/sw_inventory_output1.txt', 'a')
                combinedlines = section_array[i].strip() + "," + section_array[i + 1].strip() + "\n"
                file2.writelines(combinedlines)
        section_start = index+1
        section_size = 0
    else:
        section_size = section_size + 1


if section_size > 0:
    section_array = lines[section_start:]
    for i in range(0, len(section_array), 2):
        section_array[i] = ip_address[-1] + "," + section_array[i]
        file2 = open('D:/QR_IAAS/QR_Inventory automation/sw_inventory_output1.txt', 'a')
        combined_lines = section_array[i].strip() + "," + section_array[i + 1].strip() + "\n"
        file2.writelines(combined_lines)

file2.close()

file = open('D:/QR_IAAS/QR_Inventory automation/sw_inventory_output1.txt','r')
file1 = open('D:/QR_IAAS/QR_Inventory automation/sw_inventory_output2.txt','w')
file2 = open('D:/QR_IAAS/QR_Inventory automation/sw_inventory_output3.txt','w')
file3 = open('D:/QR_IAAS/QR_Inventory automation/sw_inventory_final.csv','w')


pattern = re.compile(r'(\s+)(?=(?:(?:[^"]*"){2})*[^"]*$)')
pattern1 = re.compile(r'\[(\d{4}-\d{2}-\d{2}, \d{2}:\d{2}:\d{2})] (.*?): (.*)')

for i in file:
    newline = re.sub(pattern, '', i.strip())
    file1.writelines(newline + "\n")
file.close()
file1.close()

file = open('D:/QR_IAAS/QR_Inventory automation/sw_inventory_output2.txt','r')

for i in file:
    newline = re.sub("\"", "",i)
    file2.writelines(newline)
file2.close()

file = open('D:/QR_IAAS/QR_Inventory automation/sw_inventory_output3.txt','r')

for i in file:
    newline = re.sub(r'(DESCR|NAME|PID|VID|SN):', "",i)
    file3.writelines(newline)

file3.close()

previous_ip = "0"

recog_pattern = re.compile(r'^(Chassis)|^(power Supply 1)|^(power Supply 2)')

file4 = open('D:/QR_IAAS/QR_Inventory automation/final_file.csv', 'w')
file4.writelines("IP Address, Hostname, Chassis PID, Chassis SN, PSU1 PID, PSU1 SN, PSU2 PID, PSU2 SN")

with open('D:/QR_IAAS/QR_Inventory automation/sw_inventory_final.csv','r') as file:
    lines = file.readlines()
    #file4 = open('D:/Inventory automation/final_file.csv', 'r')
    for i in lines:
        j = i.split(",")
        if j[0] == previous_ip:
            previous_ip = j[0]
            if recog_pattern.match(j[2]):
                file4.writelines("," + j[4].strip() + "," + j[6].strip())
                #print(j[3].strip() + "," + j[5].strip() + ",", end='')
        else:
            file4.writelines("\n")
            previous_ip = j[0]
            if recog_pattern.match(j[2]):
                file4.writelines(j[0].strip() + "," + j[1].strip() + "," + j[4].strip() + "," + j[6].strip())
                #print(j[0].strip() + "," + j[3].strip() + "," + j[5].strip() + ",", end='')

os.remove('D:/QR_IAAS/QR_Inventory automation/sw_inventory_output.txt')
os.remove('D:/QR_IAAS/QR_Inventory automation/sw_inventory_output1.txt')
os.remove('D:/QR_IAAS/QR_Inventory automation/sw_inventory_output2.txt')
os.remove('D:/QR_IAAS/QR_Inventory automation/sw_inventory_output3.txt')
os.remove('D:/QR_IAAS/QR_Inventory automation/sw_inventory_final.csv')

file4.close()


df = pd.read_csv('D:/QR_IAAS/QR_Inventory automation/final_file.csv')
df1 = pd.read_csv('D:/QR_IAAS/QR_Inventory automation/inventory_final1.csv')

with pd.ExcelWriter('D:/QR_IAAS/QR_Inventory automation/QR_IAAS_QDC5_SW_INVENTORY_MASTER_FILE_' + str(today) + '.xlsx') as writer:
    df.to_excel(writer, sheet_name='ACTIVE_NODE_INVENTORY', index=False)
    df1.to_excel(writer, sheet_name='SFP_INVENTORY', index=False)

os.remove('D:/QR_IAAS/QR_Inventory automation/final_file.csv')

