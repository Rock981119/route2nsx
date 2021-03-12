# Route2Nsx

## Overview
This script is only suitable for injecting static routes into a single T1 Router in NSX-T.<br>
The script reads the relationship between Node IP and Pod Subnet in the K8s cluster, Generate a static route in Json format, and update the API to the specified T1 Router.<br>
`This script is purely a personal hobby, it needs to be used with caution in other environments.`

<img src="img/index.png"> 

## Usage
You can run the script as a Docker or as a Pod in the K8s cluster.<br>
Specify T1 Router ID(Name), NSX-T Username & Password by passing environment variables.<br>
To use Docker, you need to mount a permissioned Kubeconfig.<br>

* Docker Run:
```
docker run --name route2nsx \
-e NSXMANAGER_IP=192.168.31.245 \
-e T1ROUTER_ID=K8C3-T1 \
-e NSX_USER=admin \
-e NSX_PASSWD="VMware1\!VMware1\!" \
-v ~/.kube/config:/root/.kube/config \
rock981119/route2nsx:unity.v1
```
