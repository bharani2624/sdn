from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.topo import Topo
from mininet.log import setLogLevel

class SimpleTopology(Topo):
    def build(self):
        # Add a switch
        switch = self.addSwitch('s1')

        # Add two hosts
        host1 = self.addHost('h1', ip='10.0.0.1/24')
        host2 = self.addHost('h2', ip='10.0.0.2/24')

        # Connect hosts to the switch
        self.addLink(host1, switch)
        self.addLink(host2, switch)

def run():
    # Set log level
    setLogLevel('info')

    # Create network with Remote Controller
    topo = SimpleTopology()
    net = Mininet(topo=topo, controller=RemoteController)

    # Add controller
    net.addController('c0', ip='127.0.0.1', port=6633)

    # Start the network
    net.start()
    print("Network started. Use `pingall` or Wireshark for testing.")

    # Open CLI for interaction
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    run()
