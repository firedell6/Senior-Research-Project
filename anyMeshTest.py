#TODO
#Integrate into TCP/IP Messaging Application

#Testing of mesh network connection
import time

from mesh.links import UDPLink
from mesh.programs import Printer
from mesh.filters import UniqueFilter
from mesh.node import Node


links = [UDPLink('en0', 2010), UDPLink('en1', 2010), UDPLink('eth0', 2010), UDPLink('eth1', 2010)]  # add your network interface here if it isn't one of these (find the name using ifconfig)
node = Node(links, 'me', Filters=(UniqueFilter,), Program=Printer)
[link.start() for link in links]
node.start()


if __name__ == "__main__":
    print("Run lan-chat.py on another computer on the LAN")

    try:
        while True:
            print("------------------------------")
            message = input("[me]  OUT:".ljust(49))
            node.send(bytes(message, 'UTF-8'))
            time.sleep(0.3)

    #Error handling for mesh network
    except (EOFError, KeyboardInterrupt):
        node.stop()
        [link.stop() for link in links]