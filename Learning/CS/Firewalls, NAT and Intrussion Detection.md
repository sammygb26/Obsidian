These are methods for observing, managing and controlling network information flows.

## Firewalls
A **firewall** is a security measure designed to prevent *unauthorized electron access* to a network computer system. The firewall prevents things getting through.

![[Pasted image 20230128214544.png]]

Here is an example

![[Pasted image 20230128214638.png]]

The **firewall** only does anything if it is chokepoint for information coming in. The firewall applies a set of rules called **firewall policies**. Based on the rules it allows or denies every traffic. For example we might have a **Blocklist** (allowed-by default). The other way is an **Allow list** (deny-by-default). Allow-list has better security but is harder to use. An example of the rules are

![[Pasted image 20230128214959.png]]

Firewall syntax changes between firewalls and can be more or less complex.

##### Firewall Types
**Packet filters (stateless)** - If a packet matches the packets filter's set of rules the pack will be dropped or accepted.

**Stateful filters** - this maintains records of all connection passing through it and can determine if a packet is either the start of a new connection, a part of an existing connection or is an invalid packet. So this can keep track of who initiated a connection.

**Application layer** - This works like a **proxy** it understands certain applications and protocols. So it may inspect the traffic and block depending on the contents.

##### Stateless Firewalls
This has no state and doesn't maintain any context. It treat each packet attempting to travel through it in isolation without considering packets that it has processed previously.

![[Pasted image 20230128215536.png]]

This allows SYN to establish TCP and SYN-ACK to maintain in bound connections. But a random SYN-ACK will not be dropped. These are **cheap** and **fast** but may have to be very restrictive to prevent attacks.

##### Stateful Firewalls
**Stateful firewalls** can tell when packets are part of legitimate sessions originating with a trusted network. These maintain tables containing information on each active connection, including IP addresses, ports, and sequence numbers of packets. Using these tables, stateful firewalls can allow only inbound TCP packets that are in response to a connection initiated form within the internal network.

![[Pasted image 20230128220214.png]]

### Port Scan
Here an attacker is looking for applications listening on ports. A single IP address is contacting many ports to see if any respond.  This would look like

![[Pasted image 20230128220550.png]]

A custom firewall ruleset could take care of this

![[Pasted image 20230128220355.png]]

### Application layer firewall / proxy
This simulates the (proper) effect of an application. Effectively a **protective interceptor** that screens information at an application layer. This allows an administrator to block certain application requests. For example we can block web traffic constraining certain words (aka censorship), or remove macros from Microsoft Word files in email. Or prevent anything that looks like a credit card number leaving a database. This can also scan for malware in downloaded files.

The problem with this is the expense. We need to simulate an entire desktop on a router (or there abouts).

##### Personal Firewalls
This runs on a workstation that it protects i.e. specific software. It provides basic protection especially for home and mobile devices. Any rootkit type software can disable the firewall.

##### Pros and Cons
**They do** prevent straightforward attacks and information leakages
**They can be circumvented**, and may have unintended consequences. Increasing their effectiveness increases their operational cost substantially (overhead/configuration).
**Bottom-line**: you have to have one but do not count on it for much.

## Network Address Translation (NAT)
We have a certain IP address within our LAN. This is a private network and in fact it will be dropped from routing if it were to be used on the internet. Our IP on the internet will be different to this address. So how does it change?

##### IPv4 and address space exhaustion
Version 4 of the internet protocol has less than 4.3 billion IPv4 available addresses. So there are not enough for every device on the planet. NAT is used to solve this. Internal IP different than external IP, border router maps between its own IP and the internals ones.

Alternatively we could switch to IPv6.

![[Pasted image 20230128222246.png]]

The IPs only have to be unique externally. We can look up these addressee son the routers (internal vs external).

![[Pasted image 20230128223503.png]]

The trick is to use the ports as identifiers for the machines. We have to set our router to forward certain ports to certain machines.

Certain devices may poke holes in your NAT. But this can allow adversaries in.

## Intrusion Detection Systems (IDS)
**Firewalls** are preventative, IDS detects a potential incident in progress. At some point you have to let some traffic into and our of your network. Most security incidents are caused by users accidently letting people in or insider threats. These don't prevent attack they allow you to address an attack.

![[Pasted image 20230128224008.png]]

##### Rule-Based Intrusion Detection
Here we can write signature for attacks. We have an alarm if anyone does some kind of bahaviour we flag then we will be notified. This is good if we have a **signature** we are looking for. This has high accuracy and low false positive. It however cannot deal with new attacks.

##### Statistical Intrusion Detection
Here we build a statistical model of acceptable "normal" bahaviour. Then we flag anything that deviated form this normal. We may have more false positives as our normal may not capture everything. But this can detect new kinds of attacks. So false negatives go down but false positives go up.

##### Base-Rate Fallacy
If we have some accuracy rating. This will create far more false positives if normal traffic is fare more likely. This can drown our or true signal. This is similar to testing accuracy for disease. 

So if regular data is far more likely there will be a sea of false positives. In some cases IDSs detect the attack but their alarms aren't investigates due to how often they go off. Not all can be investigated.

[[Firewalls, NAT and IDS questions]]