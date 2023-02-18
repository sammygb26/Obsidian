# The Application Layer and DNS
The physical, link and transport layers provide the infrastructure for applications to communicate. But the action of the internet takes place at the application layer.

### Some Application Layer Protocols
**Domain Name System (DNS)** - This protocol allows intuitive domain names to be resolved to IP addresses.
**Hypertext transfer protocol (HTTP)** - This protocol is use by web browsers
**SSL/TLS** - Allows secure encrypted browsing (HTTPS)
**IMAP/POP/SMTP** - These are protocols that make email possible
**File Transfer Protocol (FTP)** - Old protocol providing simple interface for uploading and downloading files.
**SOAP** - A recent protocol for exchanging structured data as part of the web services paradigm
**Telnet** - Early remote access protocol but like FTP it doesn't encrypt.
**SSH** - Recent more secure remove access protocol

### DNS
The **domain name system** is a fundamental application layer protocol that is essential to the functioning of the internet. It allows **domain names** such as $www.example.com$ to be resolved to IP addresses like $208.77.188.166$.

![[Pasted image 20230210111702.png]]

This is easier than remembering IP addresses. The **domains** have a hierarchy. For example **top-level domains (TLDs)** like com in the above example. Then $example.com$ is a subdomain of com. Then $www.example.com$ is a subdomain of $example.com$. These domain for a rooted tree where each node corresponds to a domain names and the children are subdomains. The root is the empty domain with TLD children.

##### Domain Name Registration
There are two types of TLD today

1. **Generic TLDs** such as .com, .net, .edu and .org
2. **Country-code TLDs** -like as .au, .de, .pt and so on. Their use is restricted to within their countries.

Domain names are registered and assigned by **domain-name registrars** which are organization accredited by ICANN (Internet Corporation for Assigned Names and Numbers). Domain names can then be reserved by contacting the registrars. There are even anonymous ones which can allow people to register and no be tracked. This can often be used by malicious actors.

because of the value of domain names there is a practice called **cybersquatting** where domain names are reserved and the not used for them to be sold on later at a higher price or just used to prevent other from using it.

##### DNS Organization
The **DNS** hierarchy is used to query different "name server" allowing the resolution of a domain name to an IP address. At the top there are **root name servers** such as .com, .it and so on. These store a **root zone database** of records indicating the authoritative name server for each TLD This database is maintained by ICANN. These name servers make up a hierarchy

![[Pasted image 20230210113040.png]]

### How DNS Queries Work
In general with **iterative resolution** we start by querying some root name server. It will point us to the correct TLD if it is not already. This will then point us to the subdomain name server. This continues until we have resolution.

![[Pasted image 20230210113313.png]]

##### DNS Packet Structure
DNS queries and replies are transmitted via a single UDP packet, with TCP being used as a substitute for requests and replies exceeding 512 bytes. This standard packets consists of 

- The header including a 16-bit **query identifier**, also called **transaction identified** which identified query responses
- The query part is a sequence of "questions" (usually just one), each consisting of the domain name queried and the type of record requested.

The answer part consists of 

- The NAME field of variable length containing full domain name.
- The 2-byte TYPE field indicating the type of DNS record. For example **A** for an address (will resolve a domain name to an IP address), **NS** records (providing information about name servers), **MX** servers providing information about mail resolution.
- The 2-byte CLASS field denotes the broad category the record applies to such as IN for internet domains
- The 4-byte TTL field saying how long this record will be valid in seconds
- The 2-byte RDLENGTH field indicating the length of the data segment
- The variable-length RDATA segments includes the actual record data. For example a 32-bit IP address

##### DNS Caching
To prevent too much traffic retrieved information will be cached for a set amount of time. Instead of querying the TLDs every time. The TTL specified how long the cached entry will last.

### DNS Attacks
DNS queries control what IP addresses we send information to.

##### Pharming and Phising
As an attacker if we control the cache then we can control what IP addresses uses visit. The attacker could thereby get the user to download **malware** in **pharming** attack or extract information with the user trusting them as in a **phishing** attack.

![[Pasted image 20230210115030.png]]

**Pharming** can also be done with MX records allowing mail to be redirected. We could also change update servers to be malicious and install malware on users computers automatically.

##### DNS Cache Poisoning
Here we trick a DNS server into caching false DNS records, any downstream client then gets this false record. One way to do this is 

1. Rapidly transmit DNS queries to some target server
2. Rapidly send spoofed responses to that server
3. If the ISP server accept the forged requests we now control an entry in the ISP

For this to work we need to beat the true names servers response time. This could be accomplished by starting transmission early or being closer to the target.  We also need to find the 16-bit query ID. This can be broken by brute force as there are only $2^{16}$ numbers or if the order is predictable in some way. Random return ports can also be used to makes this even harder.

![[Pasted image 20230210115714.png]]

##### DNS Cache Poisoning and the Birthday Paradox
The key insight is we are more likely to guess the identifier correctly if there are many identified and many responses. An attacker issuing fake responses will guess transaction ID equal to one of $n$ different 16-bit real IDs with a probability $n/2^{16}$ and so would fail with a probability $1-n/2^{16}$. But this happens $n$ times hence there is a  $$(1-n/2^{16})^n$$probability none of them will match. As $n$ rises this quickly falls to 0 and with $n=213$ there is a 50% chance that one of her random response will match a real request.

![[Pasted image 20230210122351.png]]

##### Subdomain DNS Cache Poisoning
A problem with the above request is these is only a small window to get it right as the server will not request again once it has secured a correct entry as the TTL will be set. To get around this we can request many subdomains of our target that don't exist. Many requests will be sent out for this and so there are many opportunities to poison the cache.

The trick is this should include a **glue record** that will eventually change the domain of the subdomain requested.

![[Pasted image 20230210122906.png]]

This attack can also be targeted against a victim client. This type of attack is hard to prevent as it relies on flaws in the implementation of the DNS service.

- Relying on a 16-bit number
- Having the response for a non-existent subdomain being a nonexistent response

##### Preventative Measure
**LDNS** - are DNS name servers configured to only allow responses from within their network. This means they cannot be poisoned from without. But they can still be attacked form within.
**SPR** - source port randomization can also be used to add another ~16-bits to the code. It is still possible to attacked these servers just harder.


### DNSSEC
Since preventative measures don't remove attacks DNSSEC is a secure protocol based on DNS. But this isn't widely used. **Signatures** are sent alongside records to prove their authenticity. All that remains is to get the correct public keys to users.

![[Pasted image 20230210123914.png]]

If each name server can verify its subdomain name server we can create a **chain of trust** leading back the the client. This ensures each step along the way is verified.

## Firewalls
**Firewalls** are used to keep systems safe from the internet at large. A firewall applies a set of rules to allow or reject traffic called **firewall policies**. These can be used to protect or to censor.

![[Pasted image 20230210124423.png]]

### Firewall Policies
Policies can give three possible outcomes to packets

1. **Accepted** permitted through the firewall
2. **Dropped** nit allowed through with no indication of failure (silence)
3. **Rejected** not allowed through accompanied by an attempt to inform the source.

##### Blacklists and Whitelists
This is the simplest way to allow or block traffic. With a **blacklist** we allow everything by default then have special rules applied to packets that will allow them to pass. With a **whitelist** it is the opposite with packets dropped by default. Blacklists are easier for users by default but less secure.

### Stateless and Stateful Firewalls
There are two kinds of firewalls **stateless** and **stateful**.

##### Stateless Firewalls
There is no data stored by this firewall. Every packets that passes it is treated in a vacuum and a set of rules is simply applied to decide whether or not to reject it. These allow some traffic managements by lick the flexibility required a choice between limiting functionality or security.

For example for this type of firewall to allow TCP connections it must allow all outgoing SYN packages from our computer to start the handshake. Then it must allow incoming SYN-ACK requests

![[Pasted image 20230210125334.png]]

We can block just incoming SYN packets preventing a TCP connection form being established.

![[Pasted image 20230210125447.png]]

This prevents probing attacks on the network.

##### Stateful Firewalls
Stateless firewall can't tell if a packet is in response to another or is unprompted and possibly malicious. Using tables of sequence numbers stateful firewalls can keep track of different confections.

![[Pasted image 20230210130855.png]]

We can easily keep track of TCP connections here however UDP packets don't perform a handshake and therefore may ore may not be part of a session. Generally a UDP session is instead initiated with a initialization packet which keeps the session open for a set amount of time.

##### Application Layer Firewalls
These allow monitoring of the contents of packets. For example they could allow packet payload to be inspected. This can allow for example DNS blocking on specific name server that for example contain the name games in the domain name. These may require **deep packet inspection** but this can be expensive and slow.

## Intrusion Detection
An **intrusion detection system (IDS)**. IS a software or hardware system that is used to detect malicious activity on a network. The function is divided by IDS sensor which collect real-time data about the functioning of the network. These are sent to an IDS manager. If it detects something it will sound an alarm.

![[Pasted image 20230210155347.png]]

### Intrusions
The IDS is designed to detect a number if threats. These include
1. **Masquerader** - an attacker who is falsely using the identity and / or credentials of a legitimate user to gain access to a computer system or network.
2. **Misfeasor** - a legitimate user doing something they shouldn't do
3. **Clandestine user** - a user covering up their action by deleting audit files and/or logs.

There IDSs can also detect certain attacks like

1. **Port scans** - sending out packets to see if pots are open and what service is running on them
2. **DoS** network attack means to overwhelm legitimate access
3. **Malware attacks** - replicating malicious software attack like Trojan horses, worms, viruses etc
4. **ARP spoofing**: attempt to redirect IP traffic in a local-area network
5. **DNS cache poisoning** - a pharming attack directed at changing host's DNS cache to a set IP address.

##### Intrusion Detection Techniques
Traditional network IDSs (NetoworkIDSs) sit at the perimeter of a network and detect malicious bahaviour based on traffic patters. PIDSs are **protocol-based** and can be set up for specific protocols like a web server having a PIDS for HTTP. There are also **Host-based** HIDS which reside on a single system and monitor activity on that system only. Most IDSs work via deep packet inspection and heuristics.

**Statistical IDSs** - record some baseline activity and sound an alarm when there is a difference.

**Rule based IDSs** - apply rules and heuristics when analyzing packets to decide if the alarm should be sounded.

##### An IDS Attack
One way to evade detection is to launch a DoS on the IDS itself. If enough intrusion detection events are triggered the IDS cannot log the real activity.

### Intrusion Detection Events

![[Pasted image 20230210160920.png]]

While we want to avoid false negatives and false positives, false negatives actually lead to problems. However it can be an issue if there are too may false positives as it could lead to positives not being investigated. This is exacerbated by the **base-rate-falicy** where since there is so much more usual traffic than malicious attack even a small false positive rate will drown out any false negatives.

### Rule-Based IDSs
This uses rules to trigger alarms. If traffic matches a **signatures** then an alarm is triggered. This can also allow **policies** to be enforced. The signature are for clearly malicious activity and so the accuracy is higher leading to few false negatives. The problem is the signatures could be avoided by attacked by obfuscating their activity or creating a new attack pattern.

### Statistical Intrusion Detection Systems
Here instead of matching signatures a **baseline** is found. User activity is then compared to this baseline to asses whether it is suspicious or not. For example if a user attempts to log in 100 times with the wrong password as apposed to many once every now and again this could be taken as suspicious. Machine learning can also be used to determining a typical profile for each user and host. This representation automatically learns what to expect and so deviations.

![[Pasted image 20230210162004.png]]

This can lead to **false positives** as user activity may change much over time.

## Port Scanning
This allows you t find out what traffic is allowed through a firewall and so which pots on a target machines are accessibly. This is often done to asceses if a network is safe but may also be the first step in an attack.

![[Pasted image 20230210162255.png]]

Open ports are those which respond to packets and so are ready to respond to another computer. These open port represent **attack vectors** and so need to be kept secure.

##### TCP Scans
These are the most simple scans. They determine if TCP is open on the ports they check. 

In a **SYN Scan** a party sends low level TCP packets with the SYN flag. They listen for a SYN-ACK response and if they receive this then end a RST packet to terminate the connection.

##### Idle Scanning
This is a technique where we look for predictable sequence number in a victim. We send SYN-ACK messages and receive RST messages with a sequence number. If we can detect the sequences we can use SYN packets to test if a port is open by the fact it is incrementing the sequence number.

![[Pasted image 20230210163643.png]]

### UDP Scans
A different technique is required for UDP packets. This is a connectionless protocol so there are fewer cues from which to gather information. But if we send a UDP packet generally a ICMP destination unreachable is sent for a closed port and there will be no response for an active port. One way to get around this is to send UDP packets tailored for specific programs. For example DNS packets to 53

### Port Scan Security Concerns
Often the combination of ports open can give clues as to what service is running on a host. This is called **fingerprinting**. Generally complete port scans can be detected by IDSs. 