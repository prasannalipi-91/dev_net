import requests

####### Declearation of Common RNs ########

APIC_URL = ""  ### We can put our APIC URL
TENANT_NAME = "" ### We need to put the Tenant name, which all the EPGs belongs to

####### Reading from a file, and creating the service creation input array #####

file = open('D:/ACI_automation/aci_epg_bd_input.csv','r')

SERVICE_DATA = []

for i in file:
    j = i.split(",")
    SERVICE_DATA.append({
        'epg_name' : j[0].strip(),
        'bd_name' : j[1].strip(),
        'subnet' : j[2].strip(),
        'svi' : j[3].strip()
    })

############# EPG Creation Function ############

def create_epg(epg_name, bd_name):
    rest_message = f'{APIC_URL}/api/node/mo/uni/tn-{TENANT_NAME}/epg-{epg_name}.json'
    payload =
    requests.post(rest_message, json = payload, auth={})





    