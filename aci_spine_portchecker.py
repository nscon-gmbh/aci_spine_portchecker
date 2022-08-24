# import modules
import requests
import json
import os


def get_token(baseurl,user,passw):

    # build url
    url = baseurl + '/api/aaaLogin.json'

    # define payload
    payload = {
        "aaaUser": {
            "attributes": {
                "name": user,
                "pwd": passw
            }
        }
    }

    # define header
    headers = {
        "Content-Type" : "application/json"
    }

    try:
        # send request and return response
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url,data=json.dumps(payload), headers=headers, verify=False).json()

        # parse token and return
        token = response['imdata'][0]['aaaLogin']['attributes']['token']
        return token
    except:
        print("Failed to get authorization token from: " + baseurl)



def get_devices(baseurl,token):

    # build url
    url = baseurl + '/api/node/class/fabricNode.json'

    # define header
    headers = {
        "Cookie" : f"APIC-Cookie={token}"
    }

    try:
        # send request and return response
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url, headers=headers, verify=False)
        return response
    except:
        print("Failed to get devices from " + baseurl)



def get_interface_status(baseurl,token):

    # build url
    url = baseurl + '/api/node/class/l1PhysIf.json'

    # define header
    headers = {
        "Cookie" : f"APIC-Cookie={token}"
    }

    # send request
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, headers=headers, verify=False)
    return response



def main():
    # define variables from args
    host = os.environ.get("ACI_URL") or input('\nEnter ACI url: ')
    user = os.environ.get("ACI_USER") or input('\nEnter ACI username: ')
    passw = os.environ.get("ACI_PASS") or input('\nEnter ACI password: ')

    # define dictionarys for checks
    device_dict = {}

    # get token
    token = get_token(host,user,passw)

    # get devices
    response = get_devices(host,token).json()
    devices = response['imdata']

    # parse devices
    for device in devices:

        # define variables
        name = device['fabricNode']['attributes']['name']
        dn = device['fabricNode']['attributes']['dn']
        role = device['fabricNode']['attributes']['role']

        # push to device dictionary
        if role == "spine":
            device_dict.update({dn : name})

    # get interface status
    response = get_interface_status(host,token).json()
    interfaces = response['imdata']

    # print host and types
    print("\nHost: " + host)
    print("\nDevice  |  Interface  |  Status")

    # parse interface status
    for interface in interfaces:

        # define variables
        interface_id = interface['l1PhysIf']['attributes']['id']
        status = interface['l1PhysIf']['attributes']['adminSt']
        dn = interface['l1PhysIf']['attributes']['dn']

        # manipulate dn for device name check
        check_dn = "/".join(dn.split("/")[:3])

        # get device name from dictionary
        if check_dn in device_dict:
            name = device_dict.get(check_dn)

            # print device name, interface and status if interface is not up
            if status != "down":
                print(name + "  |  " + interface_id + "  |  " + status)

if __name__ == "__main__":
    main()
