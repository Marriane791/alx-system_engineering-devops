# WebStack  Debbuging.
## Networking Basics
A protocol is a set rules for communication between two or more computers in a network which recieve, format and transfer data, considering the devices are nmade up of different infrastructures, designs and standards. These processes break processes into functions across every level of the network. Most computing protocols add a header at the beginning of each protocol to store more information about the **sender reciver** and the **message** . In order for protocols to work, they must be coded within the application or software or implemented within a hardware.
**Ip address** is a unique identifier used to identify a computer in a network. There are two standards of IP adresses *IPV4* (uses 32 binary bits to create unique adresses in the network. It is expressed by four numbers separated by dots ~ 216.27.61.137) and *IPV6* (uses 128 binary bits to create a unique adress in the network. Uses base 16 numbers  separated by semicollons. ~ 2001:cdba:0000:0000:0000:0000:3257:9652. All zeros are often omitted to save on space leaving a collon separator to mark te gap as shown ~ 2001:cdba::3257:9652). Note that an IP adress can be static or dynamic. Dynamic adresses are common. They are assigned by the DynamicHostConfigurationProtocol(DHCP). It issues the IP adress on a leasing sysytem. Once the lease expires the computer will request for a new lease. **IPV4** adresses range from 0.0.0.0 to 255.255.255.255 . However, there are some adresses reserved for spesific purposes only. They include :
* 0.0.0.0 - reserved for a default network just being connected to a TCP/IP network.
* 255.255.255.255 - reserved for messages that should go to all te computers in the network.
* 127.0.0.1 - loop back adress. A way for your computer to identify itself in a network weather or not i has an assigned IP.
* 169.254.0.1 to 169.254.255.254 - Automatic private IPs. They are assigned automatically when a computer is unsuccessful in       finding an adress from the DHCP server.  

**TCP/IP** includes a suite of communication protocols, used to connect network devices on an intranet or an extranet. It functions as an abstraction layer between the application and routing and switching fabric. It defines how data  is defined, broken down into packets, addressed, transmitted, routed and recieved, reassembled in the right order in the required destination. Common TCP/IP protocols include HTTP and FTP. The transport layer remains statefull until all the packets in a message are recieved and reassembled at the destination. TCP/IP has the following layers:
* Application Layer - HTTP, FTP, SMTP
* Transport Layer - which maintains an end to end communication.
* Network Layer - deals with the packets
* Physical Layer - combined with the datalink layer and only operates on a link.

**A port** number forms part of the adress information. They are associated with the TCP/IP and might be described as an adress to the IP adress. It allows different applications on the same computer to share recources.


