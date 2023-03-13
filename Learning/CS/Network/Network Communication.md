Communication on modern networks is characterized by the following principles. **Packet switching**, **stack of layers**, **encapsulation**. These things are fundamental is allowing modern communication networks to function.

### Packet Switching
Data we want to send is split into **packets**. Each packet is transported **independently** through the network. Each is handled on a **best efforts** basis by each path. Each packet may follow a different route from the other packets. Packets may also be dropped by an intermediate device and never delivered.

Packets may take different paths and may also be **lost** along the way.

### Stacks of Layers
Network communication models use a **stack** of **layers**. Higher layers use services of lower layers. The bottommost layer is the physical layer. A way this can be thought of is a number of layers of letters. The outer layer is used to deliver the package without caring about the inner package. Each network device implements several layers. A communication channel between two devices is established for each layer. The bottom layer is the **actual channel** while the higher layers are **virtual channels**.

The beauty of this system is higher layers don't worry about the implementation of the network. For example on the internet we may only need an IP address instead of dealing with MAC addresses over many machines or working at the packet or physical layers. The layers need to use the same communicating for example the same address. Here is a simplified **internet stack**:

![[Pasted image 20230121120412.png]]

The blue columns are the stacks for the different devices (OS appears a lot as it performs many operations).  The data flows down to the physical layer the data then goes up the next layer to decide where to go. Then it goes back down to physical once it knows its next move and so on until we reach the destination.

Different **protocols** operate at different layers. So HTPPS is used between the Browser and the Server while TLS is used for a security layer. Then the OS uses TCP and so on down the layers through IP and ARP. Each of the **layers** (application, security, reliability, internet routing, LAN routing) performs a different operation and doesn't have to worry about the other layers.

##### OSI Model
The above version is a simplification. In reality the OSI Reference model is used or **Open System Interconnect**. This is a network model consisting of seven layers. It was created in 1983 and is promoted by the International Standard Organization (ISO).

![[Pasted image 20230121121003.png]]

In reality TCP and IP is used. The above layers can be mapped to this version.

![[Pasted image 20230121121046.png]]

### Encapsulation
This helps a packet traverse the different layers. **Control Information** is contained in the **header** and **footer**. In between is the **Payload**. A protocol $P$ uses the services of another protocol $Q$ through **encapsulation**.

![[Pasted image 20230121121233.png]]

This is like using another envelope. The higher layer message is placed in a lower level packer (possibly being broken up). The **payload** in $Q$ is the packet at the layer $P$. So $q$ contains $p$. The control information of $q$ is derived from that of $p$ ensuring $p$ is routed correctly.

##### Internet Packet Encapsulation
![[Pasted image 20230121121512.png]]

So at the **application layer** we want to send some packet. The **transport layer** adds its own header on to get the data derived from the application packet. Then this is passed to the **network layer** with a new IP header derived from the TCP header. This then goes to the **link layer** with a *frame header added*. Then the frame travels on the physical layer between devices over WiFi or wires.

![[Pasted image 20230121121727.png]]

### Network Interfaces
Network interfaces are devices that connect a computer to a network, for example **ethernet card**, **WiFi adapter**, **DSL modem**. A computer can have multiple network interfaces. Packets are transmitted between network interfaces. Most local area networks, (including Ethernet and WiFi) broadcast frames.

Most network interfaces come with a predefined MAC address. A MAC address is a 48-bit number usually represented in hex. The first three octets of any MAC address are IEEE-assigned organizationally unique identifiers.

![[Pasted image 20230121122157.png]]

So you can with the MAC addresses tell what company made a device. The next three octets can be assigned by the organizations as they please with only the constraint threat the addresses are unique.

### Switch
A switch performs routing in a local area network. It operates at the link layer and has multiple interfaces, each connected to a computer / segment. Each switch learns the MAC addresses of each computer connected to it. It then forwards frames only to the destination computer. This is different from a hub which broadcasts frames

![[Pasted image 20230121122530.png]]

##### Combining Switches
Switches can be arranged into a **tree**. each forwards frames for the MAC addresses of the machines in the segment (subtrees) connected to it. Frames to unknown MAC addresses are broadcast. Frames to MAC addresses in the same segment as the sender are ignored. A this point we have a **Local Area Network (LAN)**.

Once we connect many of these we get the internet.

![[Pasted image 20230121122736.png]]

These segments are interconnected with **gateways** which manage IP routing information instead of just link layer information.

### Internet Protocol (IP) Functions
IP allows you to connect to other networks together. There are two functions.

**Addressing** - means the IP layer needs to know where data should go in order to deliver data properly.

**Routing** - means IP needs to communicate with other networks and possible networks it isn't connected to. Hence it need to send the layers correctly.

![[Pasted image 20230121123047.png]]

**Fragmentation** and reassembly of packets can happen as different layer and networks may send different packet sizes. This is allowed under IP.

##### IP Addresses and Packets
There are two kinds of IP addresses IPv4 32-bit addresses and IPv6 128-bit addresses. Address subdivided into **network**, **subnet** and **host**. This is a way of organizing a network into manageable parts. So take $$128.148.32.110$$$128.148$ may be the **network address**, **32** may be the **subnet address** and $110$ may be the **host address**. There is also a broadcast address ending in $255$ to the subnetwork indexed by the rest of the address. There are also private networks which aren't routed outside of LAN. So $10.0.0.0$ address $172.16$ address space and the $192.168$ address space.

An IP header includes
- Source address
- Destination address
- Packet length (up to 64KB)
- Time to live (up to 255) - this means how many hops or routers this packet should go through
- IP protocol version
- Fragmentation Information (how to reassemble)
- Transport layer protocol information (e.g. TCP)

### IP Routing
A **router** bridges two or more networks. It operates at the **network layer**, it contains a table telling it where it should forward packets to. Forwarding decisions are base solely on the destination address. The **routing table** maps ranges of addresses to LANs or other gateway routers. Each router broadcasts what it's connected to and how far away it is form other networks. Other networks then rely on this information.

![[Pasted image 20230121124030.png]]

So Each gateway sends this IP packet to the router closes to server $B$ or with the shortest path to $B$.

### Exploring Internet Routes
The paths change very frequently with devices going up and down and traffic changing all the time. To explore these networks ICMP can be used. A simple messages is encapsulated in single IP packets, considered a network layer protocol.

Tools base don ICMP include:
**Ping**: sends a series of echo requests messages and provides statistics on roundtrip times and packet loss
**Traceroute**: send series of ICMP packets with increasing TLL value to discover routes.

![[Pasted image 20230121124315.png]]

The returned packet has the IP address of the router reached and so can be used to map out a packets path. Although this can change while we compute it.

![[Pasted image 20230121124849.png]]

So here we can see 8 different intermediaries are hit before we get to fakebook.

**Caida** -This services maps out the internet. They just produce many graphs between networks around the world.

### Failures 
In a real world example **Syria** turned off the internet.

![[Pasted image 20230121125203.png]]

The story was that terrorists caused the attack. But this didn't stack up with other investigations. This explination didn't carry a lot of weight as there are four cables which are hard to get to and they would all need to be gut to cut of Syria.

Later is was found by Snowden that this attack was performed by the NSA.

### Network Attacks
Usually in **standard flow** information travels from source to destination. A DoS or (Denial of Service) attack happens when this connection is blocked. The infrastructure if blocked. Then in **wiretapping** also known as (sniffing) the information is copied at the source. In **passive wiretapping** the adversary is introduced into the path to the destination. In **tampering (active)** the information traveling from the source is changed. Then in **creation (spoofing)**  some information is synthesized to look like it came form the source.

![[Pasted image 20230121125934.png]]

### Wireshark
This is a packet sniffer and protocol analyzer. It capture and displays network packets for analysis. It supports plugins and so it very versatile and useful. It usually requires administrator privileges because of the security risks associated with the program. When it runs in promiscuous mode it capture's all traffic across the network.

[[Network Communication Questions]]