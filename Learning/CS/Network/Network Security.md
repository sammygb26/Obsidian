(ARP, IP, TCP, UDP) - These are protocols uses at the lower levels of the internet stack. Computers have two addresses IP addresses and MAC addresses. MAC addresses are given to physical devices while IP are given by administrators. We need to map the IP addresses to MAC addresses to allow communication.

- IP addresses are used by higher level protocols.
- MAC addresses are used by lower level protocols.

In the beginning there were tones of protocols. Devices from one manufacturer couldn't talk to other manufacturer's devices. In the end they decided to standardize the protocols. In the end they decided a set of protocols the devices should respond to.

### Address Resolution Protocol (ARP)
This connects the network layer to the datalink layer. It maps IP addresses to MAC addresses. It is based on broadcasting local messages and local addresses. Devices broadcast their MAC addresses and their IPs. No **confidentiality** (anyone can read), **integrity** (information changes are not checked) or **authentication** (source of the message isn't checked) comes with ARP. 

- ARP is defined as part of RFC 826.

##### ARP Messages
ARP **broadcasts** requests of type 

- *who has (IP address C)* - this sends out to all computers a request. A computer can then respond saying they have that address. *Machine with (IP address C) is at (MAC address)*. Many requests have to happen to get all IP MAC mappings. The **requesting machine** caches the response. The network administrator configures IP addresses then the MAC comes from the manufacturer

.
- *tell (IP address)*

The Linux, Window and OSC command "arp -a" displays the ARP table. We can use "arp -a -d" to flush the ARP cache and start again. ARP caches entries are stored for a configurable amount of time (as MAC - IP mapping may change).

##### ARP Cache Poisoning (aka ARP Spoofing)
The ARP table is updated whenever an ARP response is received. Requests are not tracked so IP and MAC addresses can be rewritten without asking. We just listen to any information (not checking it). The ARP announcements are not authenticated so machines always trust each other. This way a rouge machine can spoof (pretend to be) any machine it wants to.

##### ARP Normal Operation
Take a scenario with two computers Alice and Bob. Both machines say (name)'s IP is at MAC addresses. They both respond can get a mapping for MAC addresses.

##### ARP Failure
A machine Eve can interest itself saying it is Bob to Alice it is Alice to Bob. This machine now sits in between the two computers. This happens as both computers trust the ARP commands Even has sent. The wrong information has been put in the caches. You many not often have to do this.

ARP is still used as new techniques are build on top of this system.

- Almost all ARP implementations are stateless so you can send a response whenever
- An ARP cache is updated every time that it receives an ARP reply.
- Can "poison" ARP cache with **gratuitous ARP replies**
- Using static entries solves the problem only for small static networks.

### From LAN to Internet
The internet just connects multiple LANs together. IP addresses and MAC addresses are used within a LAN. But how can we connect networks. We use a **router** or gateway (gateway to the internet). It is also called the **default route** then the gateway will solve where this IP labeled address is going. The router decides whether the messages does to a device on the network or out to the internet. **Routers** keep routing tables each network says to the neighboring networks where a message should be sent. If it arrives at the owner of the IP address the router sends the message down.

##### Edinburgh's IP Space
Edinburgh is part of the autonomous system (AS786) of Jisc for Joint Information Systems Committee, operate Janet.
- Class $B$ network $129.215.0.0$ 

School of Informatics has 40 or so sub-networks, class C (/24) with 254 addresses or slightly larger. This is the number of public addresses they have on the internet.

##### IP Vulnerabilities
Similar to ARP there are many missing security features.
- *IP sends unencrypted transmission* - There is also no source authentication. This makes sense as the labeling needs to be unencrypted to allow header to be read.  
- *No source authentication* -So a sender can spoof source addresses making it difficult to trace packets back to attackers.
- *No integrity checking* - entire packet, header and payload can be modified, enabling **content forgeries, redirections** and **mal actor-in-the-middle attacks**.
- *No bandwidth constraints* - Large number of packets can be injected into network to launch a **denial-of-service attack**. Broad cast addresses also provide additional leverage.

All these attacks can be performed by some device on the network.


### User Datagram Protocol
ARP gets messages to the right machine on a LAN. IP gets messages to the correct network. UDP is a **stateless**, **unreliable** datagram protocol build on top of IP, i.e. it is at the **transport layer**. UDP does not provide delivery guarantees or acknowledgements, which makes it efficient. Can however distinguish data from **multiple concurrent applications** on a single host. This is done with different ports.

The **transport layer** allows packages to be moved form one **application to another**.

A lack of reliability implies applications using UDP must be ready to accept a fair amount of corrupted and lost data. This means most applications build on UDP will suffer if they require reliability. VoIP, steaming video, and streaming audio all use UDP. Many errors are fine as our brains can understand still. To get **reliability** we need to have replies to know when a message it acknowledged. So for streaming video its better to just get a quick response.

### Transmission Control Protocol
Transport layer protocol for **reliable** data transfer, in-order delivery of messages and ability to distinguish multiple applications on the same host.

- HTTP and SSH are built on top of TCP

TCP is **stateful** it keeps track of connection state in memory. TCP packages a data stream into segments transported by IP.

##### Ports
TCP (& UDP) support concurrent applications on the same serves. Prots are 16 bit numbers identifying where data is directed.

The TCP header includes both a source and destination port. Ports 0 through 1023 are reserved for use by know protocols (i.e. HTTPS uses 443)

The rest of the port are reserved for many packets.

##### TCP Format
![[Pasted image 20230128094921.png]]

### TCP Data Transfer
To initiate a TCP connection a three way handshake s performed with **initial sequence number**. A connecting machine sends out a **Syn** with some special number $x$. Then it is responded to with a **Syn-Ack** which give another special number $y$ aswell as returning $x+1$ to prove it received the first message. Finally the initial computer sends back an **Ack** with $y+1$.

![[Pasted image 20230128100115.png]]

Each TCP header includes a 16 bit checksum of the data and part of the header , including the source and destination. **Ack** packages or their lack are used to track packer loss, network congestion and flow control.

### Syn Flooding
Here attackers use their own IP to flood a server. Some malicious computer sends many **Syn** packages to a victim computer without acknowledging and **Acks**, so the target continues to try get an acknowledgement. This computer then runs out of pace to handle the packages.

A problem with this is the **attacker** must use their own IP which could be traced. The attack also must yield a higher bandwidth then the attacking computer. Hence this is **effective against a small target**, like a home server but isn't effective against a large target like a company.

##### Spoofing: forged TCP packets
Set the source of the TCP packet to another IP. Advantages: harder to trace
But we still have to use some address on our network due to **ingress filtering** where packets trying to get our of a LAN not labeled in that LAN are dropped.. Then also **Acks** are sent to a second computer so the attacker needs less bandwidth.

### Smurfing (direct broadcast)
This use ICMP (Internet Control Message Protocol) **ping** uses this. We ping on the broadcast address, all machines will respond to this address. So we write the source address as the *victim*. Then we ping everyone on the network and get a multiplied response.

This is also called a **reflection attack**. Many LAN which are vulnerable to this attack are listed.

[[Network Security Questions]]

