import re
import mysql.connector
import os


with open('D:/Inventory-tool/cctv_switch_status_modified.txt', 'r') as file:
    lines = file.readlines()

pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d)')

section_start = 0
section_size = 0
ip_address = []

new_lines = [element.rstrip() for element in lines]


for index, element in enumerate(new_lines):
    if pattern.match(element):
        ip_address.append(element)
        if section_size > 0:
            section_array = new_lines[section_start+1:index]
            section_string = ','.join(section_array)
            combined_lines = ip_address[-2] + "," + section_string
            file2 = open('D:/Inventory-tool/cctv_switch_status_output.txt', 'a')
            file2.writelines(combined_lines + "\n")
        section_start = index
        section_size = 0
    else:
        section_size = section_size + 1

if section_size > 0:
    section_array = new_lines[section_start+1:]
    section_string = ','.join(section_array)
    combined_lines = ip_address[-1] + "," + section_string
    file2 = open('D:/Inventory-tool/cctv_switch_status_output.txt', 'a')
    file2.writelines(combined_lines + "\n")

file2.close()


###########################################################
##############uploading the data to database###############
###########################################################

host = '192.168.56.101'
user = 'inventory'
password = 'Dialog@123'
database = 'INVENTORY_TEST'

try:
    # Establish a connection to the MySQL server
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connected to MySQL database")

        cursor = connection.cursor()
        cursor.execute('DROP TABLE IF EXISTS CCTV_SWITCH_STATUS_DATA')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS CCTV_SWITCH_STATUS_DATA (
                id INT AUTO_INCREMENT PRIMARY KEY,
                DEVICE_IP VARCHAR(255),
                DEVICE_NAME VARCHAR(255),
                REACHABILITY VARCHAR(255),
                VERSION VARCHAR(255),
                STACK_STATUS VARCHAR(255),
                NUM_LIVE_STACK_SW VARCHAR(255),
                NUM_CONF_STACK_SW VARCHAR(255),
                MODEL VARCHAR(255)
            )
        ''')

        with open('D:/Inventory-tool/cctv_switch_status_output.txt', 'r') as file:
            lines = file.readlines()
            for i in lines:
                row_array = i.strip().split(",")
                user_data = tuple(row_array)
                insert_query = 'INSERT INTO CCTV_SWITCH_STATUS_DATA (DEVICE_IP, DEVICE_NAME, REACHABILITY, VERSION, STACK_STATUS, NUM_LIVE_STACK_SW, NUM_CONF_STACK_SW, MODEL) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
                cursor.execute(insert_query, user_data)
            connection.commit()
            cursor.close()
            connection.close()
        file.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")

###########################################################
##############Removing unwanted files###############
###########################################################

os.remove('D:/Inventory-tool/cctv_switch_status_output.txt')

