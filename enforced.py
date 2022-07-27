#!/usr/local/bin/python3
from loginApic import loginApic
from pprint import pprint
import requests
import json
import urllib3
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

apic_ip = "10.138.159.34"
apic_username = "admin"
apic_password = "C1sc0123"


# Retrieve base_url and cookies
base_url, cookies = loginApic(apic_ip, apic_username, apic_password)

# Build up 
vrf1_url = base_url + 'node/mo/uni/tn-kai/ctx-vrf1.json'

# Payload to create vzany provider
enforced = json.dumps({
    "fvCtx": {"attributes": {"dn": "uni/tn-kai/ctx-vrf1", "pcEnfPref": "enforced"}, "children": []}
})

enforcedCreator = requests.post(
    vrf1_url, cookies=cookies, data=enforced, verify=False)
print('VRF enforced')

