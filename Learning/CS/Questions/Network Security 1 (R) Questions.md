What are the two kinds of nodes in a computer network? #flashcard #CS #NetworkSecurityR1
	There are **host nodes** (can take a receive packets) and there are **communication nodes** (switches, routers etc which facilitate packet transmission).

---
What is the difference between a WAN and a LAN? #flashcard #CS #NetworkSecurityR1 
	A WAN (wide area network) is a collection on LANs (Local Area Network) connected by routers. LANs operate at a local level with Switches and Hubs etc.

---
What are the different categories of network security issues? #flashcard #CS #NetworkSecurityR1 
	We have **confidentiality**(keeping data private), **integrity** (making sure data is unchanged), **availability** (making sure services are available constantly), **assurance** (no way to control data flow), **authenticity** (no concept of user identity), **anonymity** (no way to tie actions to users).

---
What is ethernet? #flashcard #CS #NetworkSecurityR1 
	This is a low level internet protocol in the link layer. It moves frames between devices which are addressed via their MAC addresses.

---
What are ethernet collisions and how are they delt with? #flashcard #CS #NetworkSecurityR1 
	An ethernet collision is when two packets are sent at the same time over the same channel. This leads to both being lost / corrupted. When a collision is detected all machines wait a random amount of time and then send a packet again.

---
What are hubs and switches? #flashcard #CS #NetworkSecurityR1 
	Hubs just repeat incoming frames to all ports while switches keep a table of which ports contain which MAC is that way they can just send the frame to the port it is required on. These records can expire or be overwritten by incoming frames (all of which contain a source address). Without a entry in the table for a destination MAC the frame is broadcast.

---
What are the downsides of hubs? #flashcard #CS #NetworkSecurityR1 
	They send **more traffic** as they always broadcast causing more **collisions** and making the network **slower**. There is also a **privacy** issue as all packets can be opened by every machine.

---
How many hex digits are in a MAC? #flashcard #CS #NetworkSecurityR1 
	There are 6 pairs so 12 character in total when in hex for 48bits. Typically the first 3 pairs are for an organization and the next 3 for the device.

---
Why can MAC addresses not be used as identifiers for devices? #flashcard #CS #NetworkSecurityR1 
	Since the MAC address can be changed by the user.

---
What are the contents of an ethernet packet? #flashcard #CS #NetworkSecurityR1 
	We have a **preamble** (7 bytes), **start of frame delimiter** (1 byte), then the **destination MAC** (6 bytes) and **source MAC** (6 bytes), **ether-type** (2 bytes), then the **payload** (46-1500 bytes), **Checksum** (4 bytes) and an **interframe gap** (12 bytes).

---
What are the solutions to ARP poisoning attacks? #flashcard #CS #NetworkSecurityR1 
	We can have a **static arp table** (but this can still be rewritten if an adversary breaks in) or we can **check for multiple occurrences of the same MAC** to multiple IPs.

---
What algorithm is employed by hosts to deliver IP packets? #flashcard #CS #NetworkSecurityR1 
	A host checks the IP to see if the packet is in the LAN. If it is then the packets is delivered via the MAC address for that IP address (possibly given by ARP). If not it needs to travel outside our LAN so we send it to the gateway (router).

---
What algorithm is employed by routers to deliver IP packets? #flashcard #CS #NetworkSecurityR1 
	Routers either **Drop** a packets if it expires, **Deliver** if the destination is a machine in the LAN of the router or **forward** to another router.

---
When a router forwards a packets what determines the protocol is uses to find the next router? #flashcard #CS #NetworkSecurityR1 
	If the packet is within the same AS then open shortest path is used to be most efficient. Otherwise Border Gate Protocol is used.

---
What are autonomous systems? #flashcard #CS #NetworkSecurityR1 
	Autonomous systems are groupings of IP addresses that were given to large organizations and ISPs. They define a range of IP addresses.

---
What allows IP spoofing? #flashcard #CS #NetworkSecurityR1 
	IP spoofing is facilitated by there being no checking on IP source address validity in the IP protocol. Any machine can rewrite this can impersonate another machine, although they wont receive a response.

---
How can border routers be used to defend against IP spoofing? #flashcard #CS #NetworkSecurityR1 
	If a packet from outside the subnet has a source IP address from within it is likely spoofed and so can be safely dropped.

---
What happens in packets sniffing (fixes)? #flashcard #CS #NetworkSecurityR1 
	In packet sniffing an adversary will keep traffic not addressed to them to break confidentiality within the network. **Encryption** is the best way around this although switches can also help.

---
What addressing addition does the transport layer make? #flashcard #CS #NetworkSecurityR1 
	The transport layer adds **ports** (16 bit) which allow one machine to have many addresses. This makes is possible for different application to receive different packets. (**but the ports are independent for different protocols**)

---
