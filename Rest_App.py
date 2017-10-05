''' 
Name : Ankur Sheth

'''
#import the required libraries like requests,json and urllib
import requests
import urllib
import json

#all the REST calls will use the url for controller so create a variable for controller ip
controller_url = 'http://10.0.2.15:8080/'

#get device url (REST api)
devices_url = controller_url + 'wm/device/'
#get flows url (REST api)
flows_url = controller_url + 'wm/core/switch/all/port/json'

#call the REST api for getting the device stats 
response_devices = requests.get(devices_url)
#call the REST api for getting the flow stats
response_flows = requests.get(flows_url)

#Use the json method for the response object to return (devices) request body in json
response_devices_json = response_devices.json()
# Use the json method for the response object to return (flows) request body in json
response_flows_json = response_flows.json()

#set the parent of the device response object as the top-level response object
devices = response_devices_json["devices"]
#set the parent of the flow response object as the top-level response object
flows = response_flows_json["00:00:00:00:00:00:00:01"]

print
print("=" * 40)
print('Device information')
print("=" * 40)
#FOR EACH DEVICE, PRINT DEVICE PORT, MAC ADDRESS AND IPV4 ADDRESS
#print(json.dumps(response_devices_json, indent = 4, separators = (',',':')))
print("Port " + "   " + "Mac Address     " + "     IPV4 Address  ")

for device in devices:
    a = device['attachmentPoint'][0]['port']
    b = device['mac'][0]
    c = device['ipv4'][0]
    print(a + "       " + b + "    " + c + "           ")

print
print("=" * 80)
print('Flow Statistics')
print("=" * 80)

#FOR EACH FLOW, PRINT DEVICE PORT, RECEIVED BYTES, TRANSMITTED BYTES AND DURATION IN SECS
#print(json.dumps(response_flows_json, indent = 4, separators = (',',':')))
print("Port                " + "Recieved Bytes      " + "Transmitted Bytes        " + "      Duration(sec)")

for flow in flows['port_reply']:
    for reply in flow['port']:
        x = reply['port_number']
        y = reply['receive_bytes']
        z = reply['transmit_bytes']
        t = reply['duration_sec']
        print(" " + x + "                    " + y + "                     " + z + "                    " + t)
