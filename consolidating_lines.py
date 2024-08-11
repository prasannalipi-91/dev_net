import re

pattern = re.compile(r'^[0-9\.]+')

with open('D:/MMC-CCTV/B02-03-04to09-ext/mac_log.txt', 'r') as file:
    lines = file.readlines()

section_start = 0
section_size = 0
section_array = []
ip_address = []

for index,value in enumerate(lines):
    if pattern.match(value):
        ip_address.append(pattern.match(value).group(0))
        if section_size > 0:
            section_array = lines[section_start:index]
            section_start = index
            section_size = 0
            #file = open("D:/MMC-CCTV/B02-03-04to09-ext/mac_log_modified.txt", "a")
            for i in section_array[1:]:
                consolidated_lines = print(ip_address[-2].strip() + "," + i.strip())
                print(consolidated_lines)
            #consolidated_lines = ",".join([element.strip() for element in section_array])
            #added_ip_lines = ip_address[0].strip() + "," + consolidated_lines
            #print(section_array[1:])
        else:
            section_size = section_size + 1
    else:
        section_size = section_size + 1



