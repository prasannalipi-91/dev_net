from netmiko import ConnectHandler
import re
import os

file = open('D:/MMC-CCTV/B02-03-04to09-ext/hc_device_input.csv','r')
file1 = open('D:/MMC-CCTV/B02-03-04to09-ext/hc_commit.txt','w')

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
        #command = "show i"
        command1 = "write"
        #command2 = "show running-config |  in ip address 172"
        #command3 = "do write"
        output = net_connect.send_command(command1)
        #output1 = net_connect.send_command(command2)
        #test = output.split(" ")
        #test2 = output1.split(" ")
        #print(test[1] + "," + test2[3])
        #print(test2[3])
        print("commiting on " + j[0])
        print(output)
        file1.writelines(j[0] + "\n")
        file1.writelines(output + "\n")
        #if "No sessions currently exist" in output:
        #    print("no auth sessions in " + j[0])
        #print("cheking on " + j[0])
    except:
        print(f"Unable to connect to the device: " + j[0])

file1.close()

'''
file = open('D:/EWS_PORT.txt', 'r')
file1 = open('D:/EWS_interface_check_edited.txt', 'w')


# Removing the empty and headings in the lines
empty_or_header_line_pattern = re.compile(r'^\s*$|^.*Interface\s*Status\s*Protocol.*$')

for i in file:
    empty_or_header_line_found = False
    if empty_or_header_line_pattern.match(i):
        empty_or_header_line_found = True
    else:
        file1.writelines(i)
file1.close()
file.close()

#################

with open('D:/EWS_interface_check_edited.txt','r') as file:
    lines = file.readlines()

pattern = re.compile(r'^[0-9\.]+')

start_index = 0
section_size = 0
ip_address = []
count = 0

##Adding Headers to Csv ###
file1 = open('D:/EWS_interface_check_edited.csv', 'a')
file1.writelines("DEVICE_IP,Interface,Status,Protocol,Description\n")
file1.close()

for index, element in enumerate(lines):
    if pattern.match(element):
        count = count + 1
        ip_address.append(pattern.match(element).group(0))
        if section_size > 0:
            section_array = lines[start_index:index]
            for i in range(0, len(section_array)):
                section_array[i] = ip_address[-2] + "," + section_array[i]
                section_array[i] = re.sub(r'\s{4,}',",",section_array[i])
                write_line = section_array[i].rstrip(",") + "\n"
                file1 = open('D:/EWS_interface_check_edited.csv', 'a')
                file1.writelines(write_line)
               # section_array[i] = section_array[i].replace(" ","")
                #file1 = open('D:/MMC-CCTV/B02-03-04to09-ext/port_status_file.csv','a')
            #for i, element in enumerate(section_array):
             #   file1.writelines(element)
        start_index = index+1
        section_size = 0
    else:
        section_size = section_size + 1

if section_size > 0:
    section_array = lines[start_index:]
    for i in range(0, len(section_array)):
        section_array[i] = ip_address[-1] + "," + section_array[i]
        section_array[i] = re.sub(r'\s{4,}', ",", section_array[i])
        write_line = section_array[i].rstrip(",") + "\n"
        file1 = open('D:/EWS_interface_check_edited.csv', 'a')
        file1.writelines(write_line)

file1.close()
### Again removing the empty lines
file = open('D:/EWS_interface_check_edited.csv', 'r')
file1 = open('D:/EWS_interface_check_edited2.csv', 'w')


# Removing the empty and headings in the lines
empty_line_pattern = re.compile(r'^\s*$')

for i in file:
    empty_line_found = False
    if empty_line_pattern.match(i):
        empty_line_foun = True
    else:
        file1.writelines(i)
file1.close()
file.close()

### Removing unwanted files###
os.remove('D:/EWS_interface_check_edited.csv')
os.remove('D:/EWS_interface_check_edited.txt')

'''


