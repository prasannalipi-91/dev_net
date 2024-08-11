import mysql.connector

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
    cursor = connection.cursor()

    if connection.is_connected():
        print("connected to db")
        query = f"SELECT * FROM CCTV_INVENTORY_DATA;"
        cursor.execute(query)
        rows = cursor.fetchall()
        array = []
        for elements in rows:
            result_dict = { "DEVICE" : elements[1],
                           "NAME" : elements[2],
                           "DESCR" : elements[3],
                           "PID" : elements[4],
                           "VID" : elements[5],
                           "SN" : elements[6]
                           }
            array.append(result_dict)
        return resut_array

except mysql.connector.Error as err:
    print(f"Error: {err}")