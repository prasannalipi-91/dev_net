import requests
import urllib3
from requests.auth import HTTPBasicAuth

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'http://172.18.38.202/ers/config/networkdevice/'

auth = HTTPBasicAuth('admin', 'Cr!cket_2024')
headers = {'Accept' : 'application/json','Content-Type': 'application/json', 'Ers-Media-Type' : ''}

## Inorder to get the all details (handling the pagination of REST response) will use the below function

def get_all_data(url):
    all_devicess = []
    while url:
        try:
            response = requests.get(url, auth=auth, headers=headers, verify=False)
            response.raise_for_status()
            data = response.json()
            devices = data['SearchResult']['resources']
            for i in range(len(devices)):
                sub_data = devices[i]
                all_devicess.append(sub_data['id'])
            # Check if there's a next page URL in the response (this key depends on API's pagination structure)
            if 'nextPage' in data['SearchResult']:
                url = data['SearchResult'].get('nextPage', None)['href']
            else:
                url = None
        except requests.exceptions.SSLError as err:
            print(f'SSL error occurred: {err}')
            break
        except requests.exceptions.RequestException as err:
            print(f'An error occurred: {err}')
            break
    return all_devicess

all_devicess = get_all_data(url)

url = 'http://172.18.38.202/ers/config/networkdevice/'

for index,value in enumerate(all_devicess):
    new_url = url + all_devicess[index]
    try:
        response = requests.get(new_url, auth=auth, headers=headers, verify=False)
        new_data = response.json()
        new_dict = new_data['NetworkDevice']
        #print(new_data)
        print(new_dict["NetworkDeviceIPList"][0]["ipaddress"])
    except requests.exceptions.SSLError as err:
        print(f'SSL error occurred: {err}')
    except requests.exceptions.RequestException as err:
        print(f'An error occurred: {err}')




