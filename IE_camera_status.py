import re
import os
file = open('D:/MMC-HC/BMS/07_12_2023_Acivity/activity_cctv_B01-B04_ext.txt', 'r')
file1 = open('D:/IE_remove_space.txt', 'w')

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


with open('D:/IE_remove_space.txt', 'r') as file:
    lines = file.readlines()

pattern = re.compile(r'^[0-9\.]+')

start_index = 0
section_size = 0
ip_address = []

for index, element in enumerate(lines):
    if pattern.match(element):
        ip_address.append(pattern.match(element).group(0))
        if section_size > 0:
            section_array = lines[start_index:index]
            for i in range(0, len(section_array)):
                section_array[i] = ip_address[0] + "," + section_array[i]
                section_array[i] = re.sub(r'\b50\b',"",section_array[i])
                section_array[i] = re.sub(r'\bDYNAMIC\b', ",", section_array[i])
                section_array[i] = section_array[i].replace(" ","")
            file2 = open('D:/IE_IDF_identification.csv', 'a')
            for i, element in enumerate(section_array):
                print(element)
            ip_address = ip_address[1:]
            start_index = index+1
            section_size = 0
        else:
            section_size = section_size + 1
            start_index = index + 1

    else:
        section_size = section_size + 1





