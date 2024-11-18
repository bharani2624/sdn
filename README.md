---

## **Installation**

### **1. Install Mininet**
```bash
sudo apt update && sudo apt upgrade -y

sudo apt install mininet -y

sudo apt install wireshark -y

sudo dpkg-reconfigure wireshark-common

sudo usermod -aG wireshark $USER

sudo python3 simple_topology.py

wireshark &

h1 ping h2

sudo mn -c
### **3**
```bash
sudo apt update

sudo apt install python3 python3-pip

sudo pip3 install ryu

sudo apt install mininet

sudo apt install openvswitch-switch

ryu-manager /home/abd/ryu_apps/simple_switch.py

sudo mn --controller=remote --switch=ovsk,protocols=OpenFlow13 --topo=single,3

mininet> nodes

mininet> pingall


```


