import json

device_info = {
    "NetworkDevice": {
        "name": "DeviceName",
        "description": "DeviceDescription",
        "authenticationSettings": {
            "radiusSharedSecret": "YourRadiusSecret",
            "enableKeyWrap": True
        },
        "NetworkDeviceIPList": ["DeviceIPAddress"],
        "NetworkDeviceGroups": [{"name": "DeviceGroup"}]
    }
}

with open("output.json", "w") as json_file:
    json.dump(device_info, json_file, indent=4)

