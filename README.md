# Route2Nsx

## Overview
This script is only suitable for injecting static routes into a single T1 Router in NSX-T.<br>
The script reads the relationship between Node IP and Pod Subnet in the K8s cluster, Generate a static route in Json format, and update the API to the specified T1 Router.<br>

`This script is purely a personal hobby, it needs to be used with caution in other environments.`
<img src="img/index.png"> 
