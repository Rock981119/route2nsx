from kubernetes import client, config
import json
import requests
import urllib3
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def addroute2nsx(url,payload):
    session = requests.session()
    session.verify = False
    session = session.patch(url, headers=headers, data=json.dumps(payload), auth=(nsxmanager_user,nsxmanager_passwd), verify = False)
    return session

'''K8s Part'''
try:
    config.load_incluster_config()
except config.ConfigException:
    try:
        config.load_kube_config()
    except config.ConfigException:
        raise Exception("Could not configure kubernetes python client")

v1 = client.CoreV1Api()
get_node_info = v1.list_node(watch=False)
# for i in get_node_info.items:
#     print(i.status.addresses[0].address)
#     print(i.spec.pod_cidr)

'''Call NSX API '''
nsxmanager_ip = os.getenv("NSXMANAGER_IP", "192.168.31.245")
t1router_id = os.getenv("T1ROUTER_ID", "K8C3-T1")
nsxmanager_user = os.getenv("NSX_USER", "admin")
nsxmanager_passwd = os.getenv("NSX_PASSWD", "VMware1!VMware1!")
pod_subnet = " "
node_ip = " "
route_id = " "
url = "https://{nsxmanager_ip}/policy/api/v1/infra/tier-1s/{t1router_id}/static-routes/{route_id}"

headers = {
  'Content-type': 'application/json'
}


x = 1
for i in get_node_info.items:
    route_id_index = "route2-"
    pod_subnet = i.spec.pod_cidr
    node_ip = i.status.addresses[0].address
    node_name = i.status.addresses[1].address
    route_id = route_id_index + node_name
    url = "https://{nsxmanager_ip}/policy/api/v1/infra/tier-1s/{t1router_id}/static-routes/{route_id}".format_map(vars())
    payload = {
        "network": pod_subnet,
        "next_hops": [
            {
            "ip_address": node_ip,
            "admin_distance": 1
            }
        ]
    }
    result = addroute2nsx(url,payload)
    print(result)
    