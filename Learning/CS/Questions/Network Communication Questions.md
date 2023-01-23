What is packet switching? #flashcard #CS #NetworkCommunication
	Data we want to set is split into packets. Each packet is transported independently and handled on a *best effort* basis. Where some packets wont reach the destination.

---
How are stacks of layers important to computer networking? #flashcard #CS #NetworkCommunication 
	Different layers of communication are built on one another. Each layer connects different components and packages travel down the layers to the physical layer (**actual channel**) to move. The other layers are **virtual channels**.

---
In the Open System Interconnect model what are the different layers? #flashcard #CS #NetworkCommunication 
	We have the **Application**, **Presentation**, **Session**, **Transport**, **Network**, **Datalink** and **Physical** layers.

---
What is encapsulation in computer networking? #flashcard #CS #NetworkCommunication 
	This means the data from higher layers in the network stack are send as the payload in lower network layers. As the packet or frame moves up the stack the layers a peeled off to decide what is to be done.

---
What are the four layers of internet packet encapsulation? #flashcard #CS #NetworkCommunication 
	We have the **Application Packer** (application layer) enclosed withing a **TCP or UDP** packet at the (transport layer), this is then enclosed within an **IP PACKET** (network layer) and finally put inside a **Frame** (link layer).

---
What are network interfaces? #flashcard #CS #NetworkCommunication 
	These are components of computers allowing them to interact with the network. For example **ethernet cards**, **WiFi adapters** or **DSL modems**.

---
What is a MAC address? #flashcard #CS #NetworkCommunication 
	A MAC address is a unique identifier given to network interfaces. They contain a section giving the manufacturer of the device and the rest is given by the manufacturer to uniquely identify the device.

---
What is a switch and a hub? #flashcard #CS #NetworkCommunication 
	These are devices on LANs. A switch keeps a table of how to reach different MAC addresses and so transfers frames along wires to the next device. A hub doesn't care who sees some packet and anything it received it broadcasts to all connected devices. These devices combine computers together to give a LAN.

---
What are the function of the Internet Protocol? #flashcard #CS #NetworkCommunication 
	IP is used for **addressing** (knowing where data needs to go) and **routing** (communication with other networks) and forwarding data to the correct network.

---
What is fragmentation in networking? #flashcard #CS #NetworkCommunication 
	This means a package from a higher layer can be broken into many packets in lower layers then reassembled at the other end.

---
What is IP routing? #flashcard #CS #NetworkCommunication 
	Here when a IP address cannot be resolved in a LAN it is sent to a router. The router decides which network it is connect to would be closest to the network this packet is destined for. This continues until the correct LAN is found. At this point the packet can find the correct machine within the LAN.

---
How can routs be explored? #flashcard #CS #NetworkCommunication 
	pig and traceroute can be used to find the IP addresses of machines on the way to some host. This may move between many network in many countries.

---
How does traceroute work? #flashcard #CS #NetworkCommunication 
	traceroute uses the TTL (time to live) value to trace out longer and longer sections of a route. Each time a echo request is sent pack giving the next IP. This continues until the destination is reached.

---
What are the 5 main network attacks? #flashcard #CS #NetworkCommunication 
	1. **Block (DoS)** - denial of service, connection to destination is blocked.
	2. **Wiretapping (sniffing)** - data is duplicated and send to attacker
	3. **Wiretapping (passive)** - attacker sends the traffic through them capturing it
	4. **Tampering (active)** - data from source is changed along the way by the attacker
	5. **Creation (spoofing)** - data is fabricated and send to the destination

---
