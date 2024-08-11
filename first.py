from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def reading_nodes():
    result_array = []
    with open("D:/Inventory-tool/hc_nodes.csv", "r") as file:
        for line in file:
            value = line.strip()
            result_dict = {
                "id" : value
            }
            result_array.append(result_dict)
    return result_array

def reading_file_to_dict():
    resut_array = []
    with open("D:/Inventory-tool/cctv_inventory_testing3.txt","r") as file:
        for line in file:
            value = line.split(",")
            result_dict = { "DEVICE" : value[0],
                           "NAME" : value[1],
                           "DESCR" : value[2],
                           "PID" : value[3],
                           "VID" : value[4],
                           "SN" : value[5]
                           }
            resut_array.append(result_dict)
    return resut_array



def reading_sql_table_to_dict():
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
            query = f"SELECT * FROM HC_INVENTORY_DATA;"
            cursor.execute(query)
            rows = cursor.fetchall()
            array = []
            for elements in rows:
                result_dict = {"DEVICE": elements[1],
                               "NAME": elements[2],
                               "DESCR": elements[3],
                               "PID": elements[4],
                               "VID": elements[5],
                               "SN": elements[6]
                               }
                array.append(result_dict)
            return array

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def reading_sql_table_to_dict_hc():
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
            query = f"SELECT * FROM HC_SWITCH_STATUS_DATA;"
            cursor.execute(query)
            rows = cursor.fetchall()
            array = []
            for elements in rows:
                result_dict = {"DEVICE_IP": elements[1],
                               "DEVICE_NAME" : elements[2],
                               "REACHABILITY": elements[3],
                               "VERSION": elements[4],
                               "STACK_STATUS": elements[5],
                               "NUM_LIVE_STACK_SW": elements[6],
                               "NUM_CONF_STACK_SW": elements[7],
                               "MODEL": elements[8]
                               }
                array.append(result_dict)
            return array

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def reading_sql_table_to_dict_cctv():
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
            query = f"SELECT * FROM CCTV_SWITCH_STATUS_DATA;"
            cursor.execute(query)
            rows = cursor.fetchall()
            array = []
            for elements in rows:
                result_dict = {"DEVICE_IP": elements[1],
                               "DEVICE_NAME" : elements[2],
                               "REACHABILITY": elements[3],
                               "VERSION": elements[4],
                               "STACK_STATUS": elements[5],
                               "NUM_LIVE_STACK_SW": elements[6],
                               "NUM_CONF_STACK_SW": elements[7],
                               "MODEL": elements[8]
                               }
                array.append(result_dict)
            return array

    except mysql.connector.Error as err:
        print(f"Error: {err}")



@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        result_array_of_dict = reading_sql_table_to_dict()
        return jsonify(result_array_of_dict)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/topo', methods=['GET'])
def get_topo():
    result_array_of_nodes = reading_nodes()
    return jsonify(result_array_of_nodes)


@app.route('/api/hc_switch_status', methods=['GET'])
def get_sw_status():
    try:
        result_array_of_dict = reading_sql_table_to_dict_hc()
        return jsonify(result_array_of_dict)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/cctv_switch_status', methods=['GET'])
def get_cctv_sw_status():
    try:
        result_array_of_dict = reading_sql_table_to_dict_cctv()
        return jsonify(result_array_of_dict)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
