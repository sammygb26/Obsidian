What are firewalls? #flashcard #CS #FirewallsNATIDS
	Firewalls act as a chokepoint to a network. Then can inspect all traffic going in and block any unwanted or unwarranted traffic.

---
How do the most basic firewalls work? #flashcard #CS #FirewallsNATIDS 
	The most basic firewalls consist of simple rules applied to each incoming packet. This decides if the packed is blocked or kept. For example we may block all incoming  SYN requests.

---
What are the three types of firewalls? #flashcard #CS #FirewallsNATIDS 
	There are **packet filters (stateless)**, **stateful filters** and **application layer** firewalls.

---
What happens in a packet filter firewalls? #flashcard #CS #FirewallsNATIDS 
	A packet filter firewall is stateless. So each packet is inspected individually. Then a sequence of rules are applied. If any rule matches the packet then the rules action (drop, forward) is performed. There is also a default which can be drop or forward.

---
What happens in a stateful firewall? #flashcard #CS #FirewallsNATIDS 
	In a stateful firewall information about packet sessions are kept. Packets can then be filtered out if they don't fit in with a session. This can say stop a spoofed SYN-ACK coming in from an attacked if the correct one has already come in.

---
What are the benefits and drawbacks of packet filters vs stateful filters in firewalls? #flashcard #CS #FirewallsNATIDS 
	As compared to stateful filters, packet filter is cheap and fast. The problem is it is hard to get it configured correctly as there is little fine grained control so many attacks cannot be blocked.

---
What happens in a port scan? #flashcard #CS #FirewallsNATIDS 
	The point of a port scan is to identify what ports are open to packets on a machine. The ports that are may respond. As an adversary we can then act accordingly. But this will look like a lot of traffic coming from one IP address going to many different ports.

---
What happens in an application layer firewall / proxy? #flashcard #CS #FirewallsNATIDS 
	Here our firewall inspects application layer packet information. It can then use this to block traffic form certain websites or scan incoming files for malware.

---
What is a problem with application layer firewalls? #flashcard #CS #FirewallsNATIDS 
	The problem with application layer firewalls is that they are very expensive to run and take up a lot of system resources.

---
What are personal firewalls? #flashcard #CS #FirewallsNATIDS 
	Nowadays small networks have firewalls to protect themselves. These usually provide basic protection to home devices but firewalls can be taken down by a rootkit.

---
What are the pros and cons of firewalls? #flashcard #CS #FirewallsNATIDS 
	They do prevent straightforward attacks and information leaks. But they can be circumvented and may have unintended consequences. They may also take a lot of time to configure and operate. They may give a false sense of security.

---
What is NAT? #flashcard #CS #FirewallsNATIDS 
	NAT is network address translation. The problem is there isn't enough IPv4 addresses for all devices. So combat this inside a LAN local addresses are used. The router then translates them to its own public IP address and splits up the network between its own ports.

---
What problems can NAT lead to? #flashcard #CS #FirewallsNATIDS 
	By reassigning ports many devices allow clear paths through the firewall. This can allow port scanners to fine devices like IOT cameras and hack them.

---
What is an IDS? #flashcard #CS #FirewallsNATIDS 
	An IDS is an intrusion detection system. It detects attackers once they are already in the network.

---
What are the possible alarm outcomes for and IDS? #flashcard #CS #FirewallsNATIDS 
	True positive, False positive, False negative and true negative.

---
What are the two kinds of intrusion detection systems? #flashcard #CS #FirewallsNATIDS 
	The two kinds of intrusion detection systems are rule based and statistical.

---
How do rule based IDSs work what are the drawbacks and benefits? #flashcard #CS #FirewallsNATIDS 
	A rule based IDS defines rule that identify the signature of some kind of attack. This can have a low false positive rate but it requires we know an attacks signature before it happens (we must have seen it before).

---
How do statistical IDSs work (pros and cons)? #flashcard #CS #FirewallsNATIDS 
	A statistical IDS build a statistical model of "normal traffic ". It then sounds an alarm if the activity on the machine differs form this norm. This can detect never before seen attacks but also has a higher false positive rate.

---
What is the base-rate fallacy and how does this relate to IDSs? #flashcard #CS #FirewallsNATIDS 
	Here since the amount of normal traffic is so much higher than adversarial traffic even a good accuracy will swamp the number of false positive with false negatives. This leads blue teams to not investigate alarms invalidating the whole system.

---
