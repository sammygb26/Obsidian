What is Tor? #flashcard #CS #Tor
	Tor is a low latency overlay network protocol that aims to anonymize network traffic to local adversaries.

---
What is the guard in Tor routing? #flashcard #CS #Tor 
	The **guard** is defined with respect to a user. It is the Tor relay they always connect to first.

---
How does Tor routing work? #flashcard #CS #Tor 
	In Tor routing we pass traffic through three nodes, the guard, a hidden node and the exit. A secure connection is established with the first node. Then through that node to the second then finally through that node to the final. No node knows where the traffic came from and where its is going to at the same time.

---
What is onion encryption in the Tor browser? #flashcard #CS #Tor 
	A packets is sent with layers of encryption, each node can only remove a single layer from the encryption and hence the data beneath is safe from the knowledge of any destination and source.

---
What is crypto tagging? #flashcard #CS #Tor 
	Here changes to the top layer of encryption has corresponding changes on the lower layers. This can be used to end messages and not have then corrupted when decrypted. Hence it is used to tag encrypted messages the message is revealed when the packet is decrypted.

---
What is the End-to-End correlation attack? #flashcard #CS #Tor 
	Here if an adversary control the entrance and exit nodes in a Tor circuit t can crypto tag incoming traffic and read tags on outgoing traffic this can then be used to match a user to a website as one node can match the traffic patter to another.

---
How can selective dos be used to compromise Tor? #flashcard #CS #Tor 
	Tor allows circuits to be cut due to network failures if our **guard** is an adversary it can cut the network over and over again until the exit node it also an adversary. We can then perform and End-to-End correlation attack.

---
What is a website fingerprinting attack? #flashcard #CS #Tor 
	Here we monitor the sequence and size of packets coming into a machine while accessing a website and try to guess the website from the combination of this data.

---
How is website fingerprinting performed? #flashcard #CS #Tor 
	We first collect lots of data and then train a classifier to recognize the website based on the traffic (as features).

---
What are three problems in website fingerprinting? #flashcard #CS #Tor 
	The main problems are **decreased accuracy at scale**, **base rate neglect** and **close world assumption**.

---
What is the decreasing accuracy scale problem with website fingerprinting? #flashcard #CS #Tor 
	The problem is ML techniques to guess websites from traffic work well for small numbers of classes but as this is scaled to the size of the internet the accuracy falls severally and can no longer be trusted.

---
What is the base rate problem with website fingerprinting? #flashcard #CS #Tor 
	The problem is for websites which we care about (and may be rarely visited) the number of false positives will be much larger and so it is much hard to concentrate on TPs.

---
What is the closed world problem with website fingerprinting? #flashcard #CS #Tor 
	The closed world problem with website fingerprinting is that we train on a set of websites but the true set of websites it always changing and ML solutions don't work well for any data they haven't trained on. So as the internet changes these techniques become much harder to apply.

---
What are the four main ways to resist censorship? #flashcard #CS #Tor 
	We ensure there **is no single point of failure**. We ensure **collateral damager** if we are caught. We **try not to look suspicious**. Then we attempt to **be untraceable**.

---
How does no single point of failure help overcome censorship? #flashcard #CS #Tor 
	The idea is censors will implement blocking of websites and resources. If there are many resources and websites it will be harder for them to block them all.

---
How does the idea of collateral damage help overcome censorship? #flashcard #CS #Tor 
	The idea is we mix our censor traffic in with normal traffic the censor want to allow. We they cannot distinguish our traffic form the other traffic then they cannot block us without blocking it. They must accept the collateral of this other traffic. If they don't we have overcome the censorship.

---
How does not looking suspicious overcome censorship? #flashcard #CS #Tor 
	If our traffic looks normal it cannot be detected within normal traffic. Therefore it would be impossible to block it.

---
What are the two ways to no look suspicious to get around censorship? #flashcard #CS #Tor 
	There is **emulation** where we make our websites work the same way of allowed ones to blend in and **tunneling** where we use legitimate websites to pass information through as part of accepted traffic.

---
What is the aim of censorship? #flashcard #CS #Tor 
	Censorship aims to control the access and publication of certain information.

---
How can being untraceable overcome censorship? #flashcard #CS #Tor 
	By being untraceable a censor has nothing to block as they don't know what they are looking for.

---
How can Tor allow untraceable servers? #flashcard #CS #Tor 
	These were called **hidden services**. The idea is the hidden server is never revealed. Instead intro points are requested and saved in the HSDir. A browser can tell this intro point to meet at a Rendezvous point and it will send its traffic to that point setting up a circuit with it. Both can then send traffic to the rendezvous without revealing their IP.

---
