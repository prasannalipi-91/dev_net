import re


file = open('C:/Users/Lenovo123/Downloads/WhatsApp Chat - MOEHE Attendance/_chat.txt', 'r')
file1 = open('C:/Users/Lenovo123/Downloads/WhatsApp Chat - MOEHE Attendance/attendance.csv', 'w')

pattern = re.compile(r'~â€¯')
pattern1 = re.compile(r'\[(.*?)\]')
pattern2 = re.compile(r'\]\s*(.*?)\s*:')
pattern3 = re.compile(r'\[|\]|:|\s')

for i in file:
    newline = re.sub(pattern, '', i.strip())
    date_time = pattern1.match(i).group(0)
    date_time = re.sub(pattern3,"", date_time)
    name = pattern2.search(newline).group(0)
    name =re.sub(pattern3,"",name)
    print(date_time + "," + name)
    print(i)



'''
pattern = re.compile(r'(\s+)(?=(?:(?:[^"]*"){2})*[^"]*$)')

for i in file:
    newline = re.sub(pattern, '', i.strip())
    file1.writelines(newline + "\n")
file.close()
file1.close()

file = open('D:/Inventory-tool/hc_inventory_testing1.txt', 'r')

for i in file:
    newline = re.sub("\"", "",i)
    file2.writelines(newline)
file2.close()

file = open('D:/Inventory-tool/hc_inventory_testing2.txt', 'r')

for i in file:
    newline = re.sub(r'(DESCR|NAME|PID|VID|SN):', "",i)
    file3.writelines(newline)

file3.close()
'''