docker run --name route2nsx \
-e NSXMANAGER_IP=192.168.31.245 \
-e T1ROUTER_ID=K8C3-T1 \
-e NSX_USER=admin \
-e NSX_PASSWD="VMware1\!VMware1\!" \
-v ~/.kube/config:/root/.kube/config \
rock981119/route2nsx:unity.v1