import re
file = open('D:/Inventory-tool/hc_inventory_with_combined_lines.txt', 'r')
file1 = open('D:/Inventory-tool/hc_inventory_testing1.txt', 'w')
file2 = open('D:/Inventory-tool/hc_inventory_testing2.txt', 'w')
file3 = open('D:/Inventory-tool/hc_inventory_testing3.txt', 'w')

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


