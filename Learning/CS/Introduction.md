Cybersecurity Ventures' estimate that the cybercrime damage costs are predicted to hit $6 trillion annually by 2021, up from $3 trillion in 2015. This predicts and increase of $1 trillion from 2017 to 2021. GCHQ characterized cybersecurity as being as serious as terrorism.

At the same time less than half of businesses in the US, UK an Germany are prepared to deal with cyber-attacks according to Hiscox' Cyber Readiness Report. Cybersecurity Ventures' predicted that there will be 3.5 million unfilled cyber-security jobs globally by 2021.

### What is computer security
Computer security is the protection of computer systems against adversarial environments. The systems need to **allow intended use** and **prevent unintended use**.

A security policy $\phi$ is given by a combination of our **computer system** and our **attacker model** (this includes motives -> personal motivation, financial motivation, political motivation).

### In this class
We will try to understand why computer systems are insecure and how to build secure systems.

Topics:
	- Access control and authentication
	- Cryptography
	- Communications security
	- Network security
	- Usable security
	- Web security
	- OS security
	- Software security

![[Pasted image 20230119101752.png]]

### Logistics
- 3 lectures per week (Mondays, Thursdays and Fridays) @ 1000 - 1050
- 8 tutorials/labs: week 3 - week 10

3 Coursework's:
	- CW1 - formative - Friday 10 February at 12:00
	- CW2 - 12.5% total - Friday 10 March at 12:00
	- CW3 - 12.5% total - Friday 31 March at 12:00

1 final exam - May 2021 75% total

### Landscape
The security landscape is quite large and so there isn't time to go into all of them. We will be following CyBOK (made by UK universities).

![[Pasted image 20230120205950.png]]

### Definitions
We need to decide what we mean by the words we use, **authentic** or **safe** for example. There are many ways to describe these words. We will often use more **Formal** rather than common language definitions for these fords. These are:

- Based on definitions
- Properties of the system, the data, usage and abilities of the participants
- Wide-spread agreement (in some areas; still evolving)

So we will have to replace words we use with these words.

We also need to consider are place in this and whose these words are applying to. Here are some users we could see:

- Ordinary citizen (wants ease of use)
- Whistle blower (want to escape the system and be anonymous)
- Corporate worker (maybe have special security, cares about working software)
- Dissident activist (care's about anonymity but also making a movement happen, communication, so countries may block internet usage to stop this)
- Secret agent (still want to be anonymous and will authenticate themselves)

The idea is there are many different factions using systems and we cannot respect them all.

### What is Security
The main properties are:
	- Confidentiality
		- Information only access to **authorized** entities
	- Integrity
		- The data is **untampered** and **uncorrupted** (still useful), this doesn't mater for data coming in always as we may not be responsible for verifying some data
	- Availability
		- Both the data and the system that provides **access** to it are there **when you need** them

All this is rooted in military meaning hence the usage of **data**. To get **confidentiality** we need to verify the *authorized entities* hence we need **authenticity**.

### Failure of Security: Apple Security Cert Validation Bug
This bug occurs in the code that is used to check the validity of the server's signature on a key used in a SLL/TLS connection. This allow a "man-in-the-middle" this causes the user to accept a counterfeit key that was chosen by the attacker.

![[Pasted image 20230120211402.png]]

The second goto fail means the true check isn't taken and so we never check the true key.

### Failure of Security: Meltdown/Spectre
Speculative execution speeds up CPUs we execute code that may not be executed. We do this with different cores then throw away the results we don't need. The problem is we may have **protected memory** which may contain passwords and the like. When the memory is accessed some memory is **cached** on the CPU. In **speculative execution** the checks on access are not taken then access is checked later. The problem is the cache isn't cleared when the program backs up after the access is checked. So specially crafted ops can cause timing based information leaks. So we can leak what is in the cache by testing how long the computations took.

The problem here isn't the fault of the designer they never expected this. Another problem is these issues are baked into the silicon.

### Trust
Generally, we trust when we have:
	- Assurance
		- The **means to know** the system is secure. So how we check ourselves the system is secure
	- Reliability/Resilience
		- To **operate intact** in the face of natural disaster and human-launched attacks. All systems will fail but we should know when the systems security fails.
	- Accountability
		- The **means to verify** the system was operating in a secure way. So this could be log files and so on.

There is a difference between **trustworthy** and **trusted**. Things we have to trust are **trusted**. But things are trusted when we are sure they wont betray us.

### Failure of Trust: CA Domain Control Validation
![[Pasted image 20230120212426.png]]

We want to communicate with some system. We then have certified keys the CA certifies that some website is truly the website and not an attacker faking some certificate. We trust the CA more as their whole purpose is **security** and so there are no conflicting interests.

Now the CA needs to validate the the website owns the domain. This is done through **domain control validation**. The CA asks for some file to be posted and then if it is done the website must be controlled by the person wanting a certificate.

The problem is not only the owner of a website could put a key in the domain.

##### BGP Certificate Authority Attacks
The internet is a bunch of different **networks** who have to communicate with each other. BGP allows packets to be routed outside of networks. The **source** doesn't know where the packet is going, so this acts as a pathfinding protocol. In BGP all networks get to say how far they are away from some other network. Giving the cost to reach the network form them. They can even claim ownership of the network. It is assumed that anything said is true.

Say Google owns 12.0.0.0 but an adversary could say they own 12.1.0.0 (more specific). BGP prefers this more specific route. So we would capture Googles traffic. They now own this path through the network. They could then switch in a file for example and show some fake file to a CA. Then their certificate is issues and validated, they still capture the traffic to the network and so can read all encrypted messages

![[Pasted image 20230120213432.png]]

### Failure of Trust: Operational Security of Digital Certs
Symantec has track record of fumbling certificate issuance, once even wrongly issuing one for google.com. Being a certified in the browser is a big deal as this gives a lot of briskness. So Google chrome, among other browsers removes Symantec as a root CA. 

Trustico (Symantec reseller) emails 23,000 private keys for certes they issued, this invalidating them (**how di they get them**?). All of them we revoked within 24 hours. They didn't know how they got them! But they had the private keys so the fact they had them invalidates the security.

##### Convenient Insecurity
**Trustico** used to generate private and public keys. These keys may have been saved and so not destroyed.

![[Pasted image 20230120214155.png]]

But there is a conflict of interset that lead to this convenience.

### Privacy
This concerns **individuals** and their **expectations** on how their data, bahaviour, and interactions are recorded, utilized, and spread.

A useful definition: "Information self-determination"
	- A **person** gets to **control** information about **themselves**
		- Controls can include:
			- **Who** gets to **see** it
			- **Who** gets to **use** it
			- **What** they can **use** it for
			- **Who** they can **give** it to

### Failure of Privacy: Vancouver Coastal Health
Here a Hospital paging system broadcast unencrypted medical data via pages. Anyone with some knowledge and time can intercept the data. Data includes, age, diagnosis, room number, among other details.

### Failure of Privacy: New York Taxi Database
Database released for research containing lots of information. The license plates and and taxi number of pseudonymized using MD5 hash. The hashes were then released. It should be hard to do this as there are many different hashes. But here are only few (relatively) taxi numbers, hence this makes it easy to reverse.

![[Pasted image 20230120214835.png]]

## Prevention

Was the problem lack of education? (phishing)
Could some processes have helped? (removing links or CA certification)
Were the problems obvious?
	- People are always a problem
	- Hard to get people to coordinate to secure systems (BGP)
Were the right stakeholders involved?
	- Paging system didn't involve the patients only the doctors/nurses.

### Who are the adversaries
All system are vulnerable to all manner of threats. But there can be many different threats that may take on a system.

Adversary types:
	- Nature (not working just happening but should be secured against)
	- script kiddies (just taking scripts and passing them on, no technical understanding, reusing others attacks)
	- crackers/ hackers (people who develop hacks to break systems, could be many different motivations)
	- organized crime (profit in attacks and moving goods)
	- governments (geological aims with massive resources, targeting industry, infrastructure and ip)
	- terrorists (interested in specific goals for a group, target points)

they key point is they don't all aim for the same thing. this leads to many different needs in terms of security. who we care about the most depends on our system.

### threat modelling
here we take the adversary and try to look at what they will do. 

we have to look at what they are allowed to do? or, what can they be prevented from doing?
	- the adversary need not be malicious, maybe a good honest but curios person
	- the difference is a malicious adversary will subvert and break rules
	- the honest one will just take what they are given

what do we want to prevent the adversary from doing?
	- what is the adversary's aim, or when do they win?

the set of threats we want to protect against given this (set of) adversaries?
	- when do we win? (secured against failures)
	- when do the adversary's win? (conditions met we don't want)

### terminology
- **assets**: things we want to protect, like:
	  - hardware
	  - software
	  - information

- **vulnerabilities**
	- **weaknesses** in the system that can be **exploited**
		- an example: public facing email server without spam protection

* **threats**
	* loss or damage to the system, its users, or operation
		* e.g. proprietary source code being stolen and sold
	* the six major categories of threats:
		* interception
			* information is diverted and read
		* interruption
			* usage it cut
		* modification
			* data is changed giving them control
		* fabrication
			* completely fake information
		* repudiation
			* can't deny some information
		* epistemic
			* once i control what you know / think i can attack your system.
			* so if you think all roads are blocked i can force you to take a route (internet routing)

* **attack**
	* an action that exploits a vulnerability to carry out a threat
		* e.g. hacking the company public facing email server to read emails to steal company trade-secrets

* **controls** (what we can do)
	* mitigating or removing a vulnerability
	* the control mitigates a vulnerability o prevent an attack and that defends against a threat
	* no system is perfect so this also comes to what we do when vulnerabilities are discovered

### security principles
* economy of mechanism: system should be easy to understand, verify, maintain and fix.
* fail-safe defaults: conservative permissions and functionality (system should be as secure as possible by default)
* complete mediation: every time you access you should check. for example sudo doesn't check every time for a password.
* open design: no security by obscurity (limit secret information to small amount, then the public can verify system). but security by obscurity (opposite) is often used.
* separation of privilege: cooperation required to act, so there is no single point of failure
* least privilege: programs and users on bare minimum of access
* least common mechanism: minimize shared means of access to resources
* psychological acceptability: well designed ui that are intuitive making it easy to be secure
* work factor: comparable effort for the value of the resource
* compromise recording: recoding failures and breaches

### common defence methods
there are 5 common defence patterns:
* **prevent** - just find ways to secure the system
* **Deter** - make sure consequences are known and adversaries are less likely to want to attack
* **Deflect** - try to show another target who is attacked instead of you (honey pots)
* **Detect** - should know when an attack is happening
* **Recover** - all attacks cannot be prevented need to get back on your feet afterwards.

Best practices to employ some form of all to get "**defence in depth**". Where there are many layers of defence

### Trade-Offs
* Can we have secure, privacy-friendly, and trustworthy (SecPrivTru) systems?
	* Privacy mean potentially hiding information; can the system be assured to be safe when does not know all the data?
* SecPrivTru vs. Cost
	* There is a cost to operating more secure systems
	* Are the assets worth the efforts?
	* Non-technical solutions? (insurance)
* SecPrivTru vs. Performance
	* There is an overhead to gain SecPrivTru properties
	* How much performance degradation can we tolerate?
	* What properties do we really need?

### How secure, private, trusted should it be?
There will always be a **weakest link**, the adversary will attack this. So there is no point making system stronger than some other system used which would also give access. We need to think like an attacker to look at how insecure we are.

We may also do a **cost-benefit Analysis** and decide what is it worth to add protection. But often stakeholders aren't represented like use privacy.

### Defence tools of the trade
We want to protect assets that can be hardware, software and data. There are many forms of control we might use:
	- **Cryptography** - this protects the data making it unreadable to anyone without the keys. Authenticating users with digital signatures. Can also authentical transaction with cryptographic protocols. We can also ensure integrity (with a signature) this proves our message is unchanged.
	- **Software controls** - passwords, sandboxes, virus scanners, source code versioning, software firewalls, privacy enhancing technologies
	- **Hardware controls** - fingerprint readers, smart tokens, firewalls, intrusion detection systems.
	- **Physical controls** - locks, guards, off-site backups, defence from nature
	- **Policies and procedures** - Non-technical means to protect against some types of attacks, disallow personal hotspots, or educate on phishing, password rules, security training.

[[CS/Questions/Introduction Questions]]
