What is ARP? #flashcard #CS #NetworkSecurity
	ARP (Address Resolution Protocol) describes a datalink protocol that allows machines on a network to resolve IP addresses to MAC addresses.

---
How does ARP work? #flashcard #CS #NetworkSecurity 
	ARP allows machines to ask **who has (IP address A)**. Then machines can respond with **(IP address A) is at (MAC address)**. These messages are broadcast so all machines can hear them.

---
What is ARP cache poisoning? #flashcard #CS #NetworkSecurity 
	Also called ARP Spoofing. Since the ARP machines are stateless, meaning  they treat every message incoming the same. A machine can say it has some IP address and it will overwrite the ARP cache. This can be used to insert a machine in-between two other machines on a network. You simply say to each you have the other's IP address.

---
How do LANs come together to form the internet? #flashcard #CS #NetworkSecurity 
	LANs (Local Area Networks) can communicate within themselves using switches, hubs and bridges. If an IP is not found the package will go to the **default route** or **gateway**. This leads to the router which connects LANs together forming the internet.

---
What security problems come from IP? #flashcard #CS #NetworkSecurity 
	IP sends unencrypted transmission, there is no source authentication, no integrity checking and no bandwidth constraints.

---
What issues comes from IP no encrypting messages? #flashcard #CS #NetworkSecurity 
	This means any system the messages are forwarded to can read the messages if care isn't taken to encrypt the payload.

---
What problems does the lack of source authentication in IP lead to? #flashcard #CS #NetworkSecurity 
	The lack of source authentication means that messages can be spoofed and you can lie about what IP address you are on. But to get messages back you still need to end some message.

---
What problems can come from the lack of integrity checking in IP? #flashcard #CS #NetworkSecurity 
	This means entire packets, header and payload can be modified enabling forgeries and man-in-the-middle attacks.

---
What problems does the lack of bandwidth restriction lead to with IP? #flashcard #CS #NetworkSecurity 
	This means some machines can spam out traffic and **broadcast** addresses can exacerbate this. This can lead do DoS attacks.

---
What is UDP (what layer)? #flashcard #CS #NetworkSecurity 
	**User Datagram Protocol** is a stateless unreliable datagram protocol build on IP. It send messages from some machine to another and but doesn't verify transmission. This is fine for applications which don't mind about lost data. This is part of the **transport layer**.

---
What is TCP? #flashcard #CS #NetworkSecurity 
	**Transmission Control Protocol** is a transport layer protocol for reliable transferring data. Each packet send has an ACK packet send pack to ACKnowledge that a packet has been received. Packets are send multiple times. TCP is stateful and keeps track of messages received and acknowledged.

---
What are ports within computers and what do they allow? #flashcard #CS #NetworkSecurity 
	To allow applications to speak to one another they lie on different ports. When an IP packet arrived on the computer the transport layer protocol within will contain a port which will allow the packet to be forwarded to a specific program.

---
What are the steps in the TCP handshake? #flashcard #CS #NetworkSecurity 
	1) A TCP TYN packet with Seq=x (some random number) is sent to the server
	2) The server sends back TCP SYN-ACK packet with Seq=y (some random number) and Ack = x+1.
	3) The client sends back a TCP-ACK packet with Seq=x+1 and Y=y+1.

---
What is the aim of a Syn Flooding attack? #flashcard #CS #NetworkSecurity 
	Here an adversary sends thousands of Syn packets to a server without responding to them. This creates thousands of entries in the server's TCP table. This causes a DoS on the server as it cannot reply to legitimate responses.

---
What are the upsides and downsides of the TCP flooding attack? #flashcard #CS #NetworkSecurity 
	One downside it the **adversary's IP** must be used and it is only effective against small targets.

---
What is an upgrade to a basic TCP syn flood attack? #flashcard #CS #NetworkSecurityR1 
	The we can forge our IP addresses this way all the SYN-ACKs will be send to random addresses, this hides us and reduces out bandwidth usage.

---
What is the smurfing attack? #flashcard #CS #NetworkSecurityR1 
	In smurfing ICMP ping is used on the broadcast address with the source set to our victim.

---
