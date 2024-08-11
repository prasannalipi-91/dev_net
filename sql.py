import mysql.connector

# Replace these values with your actual database credentials
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
        cursor.execute('DROP TABLE IF EXISTS HC_INVENTORY_DATA')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS HC_INVENTORY_DATA (
                id INT AUTO_INCREMENT PRIMARY KEY,
                DEVICE_IP VARCHAR(255),
                NAME VARCHAR(255),
                DESCR VARCHAR(255),
                PID VARCHAR(255),
                VID VARCHAR(255),
                SN VARCHAR(255)
            )
        ''')

        with open('D:/Inventory-tool/hc_inventory_testing3.txt', 'r') as file:
            lines = file.readlines()
            for i in lines:
                row_array = i.strip().split(",")
                user_data = tuple(row_array)
                insert_query = 'INSERT INTO HC_INVENTORY_DATA (DEVICE_IP, NAME, DESCR, PID, VID, SN) VALUES (%s, %s, %s, %s, %s, %s)'
                cursor.execute(insert_query, user_data)
            connection.commit()
            cursor.close()
            connection.close()
        file.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")