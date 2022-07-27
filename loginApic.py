from pprint import pprint
import requests
import json
import urllib3
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def loginApic(apic_ip, apic_username, apic_password):
    credentials = {
        'aaaUser':
        {'attributes':
            {'name': apic_username, 'pwd': apic_password}
         }
    }
    base_url = 'https://%s/api/' % apic_ip
    login_url = base_url + 'aaaLogin.json'
    json_credentials = json.dumps(credentials)
    post_response = requests.post(
        login_url, data=json_credentials, verify=False)
    post_response_json = json.loads(post_response.text)
    login_attributes = post_response_json['imdata'][0]['aaaLogin']['attributes']
    cookies = {}
    cookies['APIC-Cookie'] = login_attributes['token']

    return base_url, cookies
