from netmiko import ConnectHandler
import re
import os


file = open('D:/HE/he_device_input.csv','r')
file1 = open('D:/HE/he_omnicell_vlan_ports.txt','w')

for i in file:
    x = i.split(",")
    cisco = {
        "device_type" : "cisco_ios",
        "host" : x[0],
        "username" : "mannaiuser",
        "password" : "M@nn@iP@ssw0rd",
        "secret" : "cisco123",
    }
    counter = 0
    while True:
        counter = counter + 1
        #print("ssh attempt number  " + str(counter) + " to " + x[0] )
        try:
            net_connect = ConnectHandler(**cisco)
            net_connect.enable()
            command = "show vlan brief | s 2998"
            output = net_connect.send_command(command)
            output_str = str(output)
            section = output_str.split("    ")
            interface_array = section[-1].split(", ")
            if interface_array[0] != '':
                for i in interface_array:
                    command = "show runn inter " + i  + " | in descrip"
                    command1 = "show mac address-table interface " + i
                    output1 = net_connect.send_command(command)
                    output2 = net_connect.send_command(command1)
                    output2 = str(output2)
                    print(x[0].strip() + ",2998," + x[1].strip() + "," + i + "," + output1)
                    #file1.writelines(x[0] + "\n")
                    #file1.writelines(output + "\n")
            else:
                print("no ports")
            break
        except:
            #print("cannot connect")
            a =0

file1.close()
file.close()

'''

file = open('D:/HE/he_omnicell_vlan_ports.txt', 'r')
file1 = open('D:/HE/he_omnicell_edited.txt', 'w')


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



with open('D:/HE/he_omnicell_vlan_ports.txt','r') as file:
    lines = file.readlines()

pattern = re.compile(r'^[0-9\.]+')

start_index = 0
section_size = 0
ip_address = []
count = 0



for index, element in enumerate(lines):
    if pattern.match(element):
        count = count + 1
        ip_address.append(pattern.match(element).group(0))
        print(ip)
        if section_size > 0:
            section_array = lines[start_index:index]
            for i in range(0, len(section_array)):
                print(section_array[i])
                #section_array[i] = ip_address[-2] + "," + section_array[i]
                #section_array[i] = re.sub(r'\s{4,}',",",section_array[i])
                #write_line = section_array[i] #.rstrip(",") + "\n"
                #file1 = open('D:/HE/intermediate.txt', 'a')
                #file1.writelines(write_line)
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
        print(section_array[i])
        #section_array[i] = ip_address[-1] + "," + section_array[i]
        #section_array[i] = re.sub(r'\s{4,}', ",", section_array[i])
        #write_line = section_array[i] #.rstrip(",") + "\n"
        #file1 = open('D:/HE/intermediate.txt', 'a')
        #file1.writelines(write_line)

file1.close()


### Again removing the empty lines
file = open('D:/HE/port_status_file.csv', 'r')
file1 = open('D:/HE/port_status_file1.csv', 'w')


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
os.remove('D:/HE/port_status_file.csv')
os.remove('D:/HE/he_port_status_edited.txt')
'''