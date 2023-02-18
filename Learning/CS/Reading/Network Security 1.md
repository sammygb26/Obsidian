The internet was devised as a robust networking system. Information is sent in **packets** made up of a **header** (source, destination, type) and **payload** (actual information sent).

### Network Topology
This is the connection structure within a network. Computers are **host nodes** and are sources and destinations of packets.*Routers* are **communication nodes** which information travels through. A small number of computer makes up a LAN (Local Area Network). The internet is also known as a WAN (wide area network). Routers in wide-area network on the internet are broken into chucks called **autonomous systems**. Each of these is controlled by an organization or entity.

![[Pasted image 20230209194557.png]]

### Internet Protocol Layers
These are the layers of protocols that make up a stack allowing high level tasks to be achieved by breaking up the task into small steps (lower packets). This is down all the way down to the physical metal.

1. **Physical layer** - How bits are sent from machine to machine on a physical medium
2. **Link-layer** - Ensures data is transferred between a par of network nodes. This uses MAC addresses which specify individual nodes.
3. **Network layer** - This is known as the internet layer and allows packets to move between hosts. Hosts are addressed using a label called an IP address. The protocol used is the **Internet Protocol** (IP).
4. **Transport layer** - This supports the communication between applications running on machines. For example **TCP** and **UDP** may be used to transfer data from one application to another.
5. **Application layer** - Here protocols exist to support the functioning of devices for example HTTP, HTTPS, SSH, DNS, and so on.

In the internet packets of higher layers and **encapsulated** whin packets of lowers layers. This allows the packets to be moved up and down the layers adding functionality to the network.

![[Pasted image 20230209195525.png]]

##### Using IP Suite
The IP suite was invented in a time when it didn't make sense for users of these networks to have malicious intent. These networks were so few and so expensive it wouldn't make sense to break any of it. Different layers have different functionality.

![[Pasted image 20230209195725.png]]

### Network Security Issues
To asses security we will comes back to C.I.A.

**Confidentiality** - There is no mechanisms in the base IP/TCP model to ensure information is kept secret. The only thing stopping someone from knowing something is if the packet passe through their fingers.

**Integrity** - There is no checking of the data to ensure it is free from tampering hence IP/TCP has no integrity.

**Availability** - The internet was designed to tolerate failures of hosts and routers. The data load is not taken in to account allow DoS attacks.

We can also look to the A.A.A model

**Assurance** - Permissions and polices don't exist by default and any packet can go anywhere.

**Authenticity** - There is no verification or proof of usership in any of the layers. The only specification is the IP address which is public and can be changed.

**Anonymity** - By default the network is anonymous as there is no concept of identity while this is good for human rights it can allow malicious entities to evade being traced.

![[Pasted image 20230209200600.png]]

# Link Layer
This is the layer **ethernet** runs on and ensures frames move from computer to computer.

In old networks all computers are sent frames, they will the keep or discard the frames based on if the MAC address matches. These can either be in a linear layout or a ring layout. But all machines are connected to the same line. Data could not be sent by multiple machines at the same time as both would light up the physical layer. This is called a **collision**.

##### Dealing With Collisions
This is when two devices send messages on a wire at once. Once this is detected each can wait a random amount of time to hopefully not cause another collision. This is designed so eventually every machine can send their packets.

##### Hubs and Switches
Hubs simple repeat frames from one port to all their other ports. These were common in old networks. Switches on the other hand look at the MAC address to see where it should go. They keep a table of MAC addresses - ports. This means when a frame comes in they can decide if they need to forward it to a port. They will only do so if said port has received traffic from said MAC address recently. This recently is ensued by **TTL** in the table.

### Media Access Control (MAC) Addresses
Network interfaces are typically identified by a hardware-specific identified known as its MAC address. These are 48-bit identified assigned to network interfaces by manufacturers. Typically the first 24-bits identify the organization (set by the IEEE) who made the device and the next 24 are device specific. MAC addresses can also be changed locally to ensure conflicts don't occur. These can Infact be easily changed on the command line in many cases (ifconfig).

![[Pasted image 20230209202221.png]]

### ARP Spoofing
ARP is the **address Resolution Protocol** and it is a link-layer protocol that allows IP addresses to be resolved to MAC addresses. There is a man-in-the-middle attack here called *ARP spoofing*.

##### How ARP works
If a machine wants to send a packet to a destination machine on a LAN. The source machine knows the destination IP address. This is for the network layer. But the link layer doesn't use IP addresses. We need to know the MAC address of the destination node.

This resolution is done via a **broadcast** message that asks about the owner of the IP address and their MAC address.

![[Pasted image 20230209202617.png]]

Then the owner can respond with transmitted to the MAC address of the packet sent to the queried machine.

![[Pasted image 20230209202635.png]]

At this point the original computer will update its ARP table with this MAC address. This is a simple protocol and machines will update their table even if they didn't ask for an address.

##### ARP Cache Poisoning
Here an attacker can basically rewrite a connection between $A$ and $B$. Such that $A$ things $B$ is at $E$ and $B$ things $A$ is at $E$. The machine $E$ can simply say this in ARP packets. This way all traffic between $A$ and $B$ passes through $E$ and can be inspected.

![[Pasted image 20230209203053.png]]

A way around this is **static ARP tables** where admins manually rewrite the tables. However if someone can achieve admin access they can likewise install a man in the middle.

# The Network Layer
Here we attempt to move packets between two networks on a **best effort basis**.

### IP
The *Internet Protocol* is the network-level protocol which performs a best effort to route a data packet from a source node to a destination node in the internet. These IP addresses are either 32-bit numbers for IPv4 or 128-bit for IPv6.

##### Routing IP Packets
This relies on a simple algorithm performed by a host. 

1. **If the packet is addressed to a machine on the same LAN as the host** - then the packet is transmitter directly on LAN using the ARP protocol to determine the MAC address of the machine.
2. **If the packet is addressed to a machine not in the LAN** - then the packet is transmitted to specially determined machine on the LAN called a **gateway**. This handles the next step of routing.

Each machine typically knows if a IP address belongs to its network so will know for each packet if should go to the gateway or not. **Gateways** and other intermediates node that handle the routing of packets on the internet are called **routers**. They connect two or more LANs. They contain **routing tables** to demine the next router a packet needs to be sent to.

![[Pasted image 20230209204308.png]]

Misconfiguration in routing tables can cause packets to travel forever aimlessly and so to prevent this each one has a TTL which counts own for each hop it makes.

##### AIs and Subnets
The internet is divided into autonomous systems, so routing tables have to be able to direct traffic to node clusters not individual destinations. Networks are partitioned on logical grouping known as **subnets**. To know what is in an outside a subnet a **subnet mask** is used.

![[Pasted image 20230209204733.png]]

We know an IP is in our subnet if it the network part matches.

Subnets masks give a range of IP addresses and these are given our based on the sizes of organizations. **Class A** networks are the largest have only at least an 8-bit subnet mask. Then **Class B** network have a least a 16-bit subnet mask. Finally **Class C** networks have usually 24-bit subnet masks and so will have 256 unique addresses.

### Internet Control Message Protocol
This is the **ICMP**, it is a network-layer protocol that is used by hosts to perform a number of basic testing and error notification tasks. For example diagnostics, determining if a host is alive and finding path followed by a packet. Some of the types of messages include:

1. **Echo request** - Asks destination to reply
2. **Echo response** - response to the above
3. **Time exceeded** - error notification that a packet has expired, TTL is 0.
4. **Destination unreachable** - error notification that a packet couldn't be delivered.

##### Ping
**Ping** is a unitality that uses ICMP to verify whether or not a particular host is receiving packets. Ping sends an ICMP echo request and gets the response.

##### Traceroute
This uses ICMP messages to determine the path a packet takes to reach another host, either on a LAN or the internet. The TTL is use to get to host progressively further along the path until a host is found.

![[Pasted image 20230209205620.png]]

### IP Spoofing
The source address is never checked in any way by default. In fact most OSs allow the source address to be rewritten. When this is done it is called **IP spoofing**.

![[Pasted image 20230209205911.png]]

##### How IP Spoofing is Used in Other Attacks
Any response to the message packet will go not to the attacker but to the owner of the IP address used to spoof. Hence these attacks only work if the attacker doesn't need the response or has another way of getting it.

##### Dealing with IP Spoofing
One way to deal with this is by configuring **border routers** so that packets with source addresses inside them coming in are dropped or sources outside from inside going out are dropped. This is as these packets are likely forged.

IP traceback techniques can also be used to reverse this.

# The Transport Layer
This extends the functionality of IP addresses by viewing machines as having multiple ports Applications can live on these ports and receive notifications when packets arrive addressed to them. These ports are 16-bot source and destination numbers in the transport layer headers. Two common ones are **TCP** and **UDP**.

### Transmission Control Protocol
This is a critical protocol for the internet and it ensures information it transmitted in full without loss. A program can interface with TCP specifying an IP address and port then TCP will ensure the data is transmitted over IP from machine to the other. The data will then be handed off to the other machine.

##### Congestion Control
TCP keeps track of what packets are sent and how long transmissions are taking. This allows it to limit the number of packets it needs to send to achieve good data quality. Acknowledgements are send of previously sent packages allowing TCP to track how much data has been successfully sent.

##### TCP Packet Format
This includes the source and destination ports along with a sequence number specifying the part of the data this is and a acknowledgement number to be send back to prove the packet has been received. A checksum is also included to allow detection of corruption.

![[Pasted image 20230209211712.png]]

##### TCP Connections
TCP uses a three-way handshake to establish a reliable confection stream between two parties. First the client sends a pack to the destination with the SYN flag. This includes a random **sequence number**. In response the server replies with a packet marked with both SYN and ACK (for acknowledgment), this is a SYN-ACK packet. This includes an acknowledgment number which is set to one more than the received sequence number and a new random sequence number. Finally the client sends an ACK message with the acknowledgement number set to the server's sequence number plus 1.

![[Pasted image 20230209212057.png]]

Common application layer protocols live at specific ports for example SSH uses 22 and HTTP uses 80. **Sockets** are used in programming which allow programmers to treat internet connections as files.

### User Datagram Protocol
UDP doesn't protect against packet loss or corruption like TCP. This make sit faster however. Parties simple send messages known as **datagrams**. No handshake is needed for UDP. A *checksum* is included for individual packets. Anything else is left to the applications running on UDP.

![[Pasted image 20230209212648.png]]

UDP packet is far simpler.

### Network Address Translation
There aren't enough IP addresses for all the devices we have nowadays. Instead **network address translation** is used. This allows machines on a LAN to share IP addresses. Private devices are on the $192.168$ and $172.16$ subnets. A NAT router represents the gateway between private IP and public IP addresses.

![[Pasted image 20230209234700.png]]

In NAT a lookup table is maintained that contains entries of the form 

![[Pasted image 20230209234742.png]]

Hence as long as the correct porn is known for the private IP address more machines can be accessed. The source IP address and port of outbound packets is changed while the destination IP and port is changed for inbound packets. Checksums may also be updated to reflect changes to the IP addresses. 

### TCP Session Hijacking
This is a security flaw in TCP that allows a hacker to hijack or alter a TCP connection from another user.

##### TCP Sequence Prediction
This is also known as **session spoofing**. Instead of stealing a session we create a new one. usually TCP connections are initiated by a three-way handshake. Here we attempt to guess the initial sequence numbers sent by the server at the start of a TCP session. This allow us to create a spoofed session. Early on TCP sequence numbers weren't randomized making this trivial. 

##### Blind Injection
In **session spoofing** only one-way communication is permitted since the server s never gives the attacker's IP address they can never get a response. When we don't get a response like this it is a **blind injection**.

##### ACK Storms
Blind injection can cause client and server to become out of sync. To resync a flood of ACK messages is send until one is lost. This is called an **ack storm**.

##### Complete Session Hijacking
If an attacker is on the same network segment as the target server the entire TCP session can be hijacked as the SYN and ACK numbers can be seen in sniffed packets. With this the attacker can inject a packed with a with probable sequence number. This can also be used to create a man in the middle attack for example using ARP spoofing.

##### Countermeasures
Application layer encryption schemes can help with these attacks.

## Denial-of-Service Attacks
Each network has a finite service, when this is used up packets are dropped. Any attack designed to cause a machine to be unavailable is called a **Denial-of-Service (DoS)** attack. Attackers don't care for a response so IPs can be spoofed making it hard to block with a firewall via blacklisting IPs.

### ICMP Attacks
Two simple DoS attacks, ping food and smurf exploit ICMP

##### Ping Flood Attack
The ICMP ping utility sends an ICMP echo request to a host who responds with a reply. With a ping flood a strong machines can overpower a weaker machines by sending many of these pings.

##### Smurf Attack
This is a variation of the above technique that makes use of misconfigured networks which have a **broadcast** address allowed. If a user sends a packet to this address every IP in the network will receive the message. So we can broadcast  ping with a return address to our victim system and multiply our power many times.

![[Pasted image 20230210021719.png]]

This can be prevented by configuring the network to not allow broadcasting. Weak servers can also just ignore ping requests.

### SYN Flood Attacks
Here we send a large amount of SYN packets and in response the server will attempt to make contact with the spoofed IP addresses we are filling the messages with. The server keep the session open for a small amount of time. Hence these attacks can quickly overwhelm the storage of the server.