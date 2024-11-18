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

