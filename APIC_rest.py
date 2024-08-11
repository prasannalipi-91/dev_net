import requests

# Define APIC credentials
username = 'your_username'
password = 'your_password'
apic_url = 'https://172.16.243.11/api/aaaLogin.json'

# Construct authentication request payload
auth_payload = {
    "aaaUser": {
        "attributes": {
            "name": admin,
            "pwd": MMCP@ssw0rd
        }
    }
}

# Send authentication request
response = requests.post(apic_url, json=auth_payload, verify=False)  # Note: Setting verify to False ignores SSL certificate verification (not recommended in production)

# Check if authentication was successful
if response.status_code == 200:
    # Get token from response
    token = response.cookies['APIC-Cookie']
    print("Authentication successful. Token:", token)
else:
    print("Authentication failed. Status code:", response.status_code)