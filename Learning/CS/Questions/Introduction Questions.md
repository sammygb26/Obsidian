What is the aim of computer security? #flashcard #CS #IntroductionToCS
	The aim in computer security is to ensure intended use have access to systems while preventing unintended use.

---
How are definitions different in this course? #flashcard #CS #IntroductionToCS 
	Definitions are used to redefine and solidify words' meaning. We use definition to be definite in our meaning throughout the course.

---
What are some different stakeholders in computer security and what do they want? #flashcard #CS #IntroductionToCS 
	- Ordinary citizen (wants ease of use)
	- Whistle blower (want to escape the system and be anonymous)
	- Corporate worker (maybe have special security, cares about working software)
	- Dissident activist (care's about anonymity but also making a movement happen, communication, so countries may block internet usage to stop this)
	- Secret agent (still want to be anonymous and will authenticate themselves)

---
What are the main properties of security / a secure system and what do they mean? #flashcard #CS #IntroductionToCS 
	The main properties are **confidentiality** (information stored can only be accesed by those with right), **integrity** (systems are free from tampering or forgery) and **availability** (system can be accessed when you need it).

---
What is required to have trust? #flashcard #CS #IntroductionToCS 
	We need **assurance** (knowing the system is secure given in some way), **reliability/resilience** (system operates intact if the security is compromised we know when it is) and **accountability** (we have the means to ensure the system is working in a secure way e.g. auditing).

---
What is an example of a trusted authority when it comes to certificates? #flashcard #CS #IntroductionToCS 
	Certificate authorities are trusted entities that validate certificates used to sign public keys for secure data transfer.

---
How can CA Domain Control Validation fail? #flashcard #CS #IntroductionToCS 
	A CA may want to use CA domain control validation to prove that some entity requesting a certificate owns the domain it is requesting domains for. But this can fail as a response "proving" (spoofing) ownership of a domain could come in. This could be done with a BGP attack.

---
What is a fasted path BGP attack? #flashcard #CS #IntroductionToCS 
	BGP is a algorithm to send packages to the correct router. However it relies on every router reporting how long it will take through them to reach some LAN. You van spoof these requests and get packages forwarded to you and basically act as a man-in-the-middle.

---
What is an example of privacy failure with taxis? #flashcard #CS #IntroductionToCS 
	Here taxi data was anonymized by MD5 hashing the taxi numbers. However even through there were many possible hashes there were comparatively less  taxi numbers allowing then to be cracked. This de-anonymized the drivers.

---
How can attacks be prevented overall? #flashcard #CS #IntroductionToCS 
	We can **educate** (for example with phishing), **fix** some problem is there is a failure in procedure. 

---
What are some common adversaries? #flashcard #CS #IntroductionToCS 
	**Nature** (bad things happen, e.g. floods), **Scrip kiddies** (people without technical knowledge who use pre-made hacks), **Crackers/Hackers** (people dong out of interest), **Organized Crime** (profit driven), **government** (massive resources with geopolitical intentions) and **terrorists** (trying to send a message).

---
What is done in threat modeling? #flashcard #CS #IntroductionToCS 
	In threat modeling we look at a system form the point of view of an attacker and try to see what systems they might attack and how / what they might aim to do with a system. You have to consider **what can / are they willing to do**, **what do we want to prevent them from doing**, **what we want to protect vs what the adversary wants**.

---
What are assets? #flashcard #CS #IntroductionToCS 
	Assets are things we want to protect like hardware, software and information.

---
What are vulnerabilities? #flashcard #CS #IntroductionToCS 
	These are **weaknesses** in the system that can be **exploited**.

---
What are threats? #flashcard #CS #IntroductionToCS 
	These are possible outcomes of an attack we don't want to happen.

---
What are the six major categories of threats? #flashcard #CS #IntroductionToCS 
	* Interception
			* Information is diverted and read
		* Interruption
			* Usage it cut
		* Modification
			* Data is changed giving them control
		* Fabrication
			* Completely fake information
		* Repudiation
			* Can't deny some information
		* Epistemic
			* Once I control what you know / think I can attack your system.
			* So if you think all roads are blocked I can force you to take a route (internet routing)

---
What is an attack? #flashcard #CS #IntroductionToCS 
	An action that exploits a **vulnerability** to carry out a **threat**.

---
What are controls? #flashcard #CS #IntroductionToCS 
	Controls are things we could do to mitigate or remove a vulnerability.

---
What are some good security principles? #flashcard #CS #IntroductionToCS 
	- **Economy of mechanism**: system should be easy to understand, verify, maintain and fix.
	- **Fail-safe defaults**: conservative permissions and functionality (system should be as secure as possible by default)
	- **Complete mediation**: every time you access you should check. For example sudo doesn't check every time for a password.
	- **Open design**: no security by obscurity (limit secret information to small amount, then the public can verify system). But security by obscurity (opposite) is often used.
	- **Separation of privilege**: cooperation required to act, so there is no single point of failure
	- **Least privilege**: programs and users on bare minimum of access
	- **Least common mechanism**: minimize shared means of access to resources
	- **Psychological acceptability**: well designed UI that are intuitive making it easy to be secure
	- **Work factor**: comparable effort for the value of the resource
	- **Compromise recording**: recoding failures and breaches

---
What are 5 common defence methods? #flashcard #CS #IntroductionToCS 
	- **prevent** - just find ways to secure the system
	- **Deter** - make sure consequences are known and adversaries are less likely to want to attack
	- **Deflect** - try to show another target who is attacked instead of you (honey pots)
	- **Detect** - should know when an attack is happening
	- **Recover** - all attacks cannot be prevented need to get back on your feet afterwards.

---
What trade-offs come with security, privacy and trustworthiness? #flashcard #CS #IntroductionToCS 
	A system will be **more expensive** and **less-performant** with a focus on security. These are taken are reasons not to follow proper security.

---
What are the most common defence tools? #flashcard #CS #IntroductionToCS 
	We use **cryptography** (this protects data making it unreadable to anyone without the right key), **software controls** (passwords, sandboxes, virus scanners, versioning, software firewalls), **hardware controls** (fingerprint readers, smart tokens, firewalls, intrusion detection), **physical controls** (locks, guards, off-site backups) and **policies and procedures** (non-technical but educational also password rules).

---
