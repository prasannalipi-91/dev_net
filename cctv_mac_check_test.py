import re
import os


#################

with open('D:/MMC-CCTV/mac-post-check.txt', 'r') as file:
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
        if section_size > 0:
            section_array = lines[start_index:index]
            for i in range(0, len(section_array)):
                section_array[i] = ip_address[-2] + "," + section_array[i]
                section_array[i] = re.sub(r'\s{4,}',",",section_array[i])
                write_line = section_array[i].rstrip(",") + "\n"
                file1 = file1 = open('D:/MMC-CCTV/mac-check-post-log.txt', 'a')
                file1.writelines(write_line)
                print(write_line)
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
        file1 = open('D:/MMC-CCTV/mac-check-post-log.txt', 'a')
        file1.writelines(write_line)

file1.close()