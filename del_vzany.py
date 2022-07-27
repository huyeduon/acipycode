#!/usr/local/bin/python3
import requests
import json
import urllib3
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from loginApic import loginApic

apic_ip = "10.138.159.34"
apic_username = "admin"
apic_password = "C1sc0123"

# Retrieve base_url and cookies
base_url, cookies = loginApic(apic_ip, apic_username, apic_password)

# Build up vzany_url
vzany_url = base_url + 'node/mo/uni/tn-demo/ctx-vrf1/any.json'

# Payload to delete vzany provider
provVzany = json.dumps({
    "vzRsAnyToProv": {
        "attributes": {
            "tnVzBrCPName": "default",
            "status": "deleted"
        }
    }
})

# Payload to delete vzany consumer
consVzany = json.dumps({
    "vzRsAnyToCons": {
        "attributes": {
            "tnVzBrCPName": "default",
            "status": "deleted"
        }
    }
})

provVzanyDeleter = requests.post(
    vzany_url, cookies=cookies, data=provVzany, verify=False)
print('vzany contract provider side was removed')
time.sleep(1)

consVzanyDeleter = requests.post(
    vzany_url, cookies=cookies, data=consVzany, verify=False)
print('vzany contract consumer side was removed')
