Why is encryption not a solution to anonymity?  #flashcard #CS #AnonymousCommunication
	We cannot simple encrypt everything as this leaves the header encrypted which are needed to route traffic the correct destination.

---
How can network traffic be used to break internet users privacy?  #flashcard #CS #AnonymousCommunication 
	Our traffic can reveal our identity as in general our traffic is unique to us. It hold our interests, habits and much more.

---
What is the definition of anonymity?  #flashcard #CS #AnonymousCommunication 
	The definition is the use of a service or resource without disclosing the user identity. Where identity is something that can be tied back to the users physical form.

---
What is the dinning cryptographers protocol?  #flashcard #CS #AnonymousCommunication 
	This gives a way to transmit information anonymously to a group of people without revealing who gave out the information.

---
How does dinning cryptographers work?  #flashcard #CS #AnonymousCommunication 
	1. We start with **secure channels** between each diner that doesn't reveal who want to give out information.
	2. Every pair of users generate a random bit (0,1) between them. This leaves every user with n-1 bits. With each random bit present in two users knowledge.
	3. All users who don't want to say anything XOR all the random bits they have and transmit the resulting value.
	4. The user wanting to transmit can flip a bit if they want to transmit 0 and not flip a bit if not.
	5. All transmitted values can be XORed revealing a 0 or a 1 in accordance with e transmitting users wish.

---
Why does dinning cryptographers work?  #flashcard #CS #AnonymousCommunication 
	The key things is we technically end with a massive XOR at the end with all random values repeated twice. This means they all cancel out giving 0. If someone choses to flip the bit they transmit this will flip the result. But no one has all the random bits so they can't figure out who flipped the bit.

---
What are some problems with dining cryptographers?  #flashcard #CS #AnonymousCommunication
	It is vulnerable to DoS attacks as it relies on every user not sending out random bits. It also relies on secure channels which can be hard to manage.

---
What is the idea with crowds?  #flashcard #CS #AnonymousCommunication 
	In crowds we have a collection of users and we hope to gain anonymity by routing traffic between them randomly before exiting to a server.

---
How do crowds work?  #flashcard #CS #AnonymousCommunication 
	We have $m$ users where $c$ of them are corrupted. To send out a message we randomly send it to some user. Each forwarder either sends it to a new forwarder with a probability $1-p_f$ or sends it to the target server with a probability $p_f$. Each forwarder rewrites the source address so the packet is hidden.

---
What can be used to break crowd based anonymity?  #flashcard #CS #AnonymousCommunication 
	In crowd based anonymity isn't secure it an adversary can see the whole network state. In these cases the timing a packet enters and leaves a forwarder can be tracked to allow the packets movement to be revealed.

---
How does a Chaum's mix work?  #flashcard #CS #AnonymousCommunication 
	With a Chaum's mix we add a new mix node to a network which anonymous traffic is forwarded to. The mix node takes in a number of packets, jumbles up the order, pads them (so they are the same size) and then releases them after some time. The packets going in have their next destination encrypted so only the mix can known it.

---
What are the different security features of Chaum's mixes?  #flashcard #CS #AnonymousCommunication 
	We have **buffering** (to break timing based deanonymization), **padding** (to break packet size based deanonymization), **encryption** of messages (to ensure destination cannot be revealed by catching a packet), **dummy packets** (to stop n-1 attacks) and **header rewriting** to removed packet tracing.

---
What are n-1 attacks?  #flashcard #CS #AnonymousCommunication 
	These are attacks on mixes where the mix is filled up with traffic from a bad actor. If only one packet is in the mix not form this actor then it can be spotted as the destination of the others is known.

---
What is an anonymity set?  #flashcard #CS #AnonymousCommunication 
	This is a way to measure anonymity we measure it by the number of users the action is split between (the set of user). With 4 users and complete anonymity between there is a 1/4 change we are guessed.

---
What are the three kinds of mixes?  #flashcard #CS #AnonymousCommunication 
	**Threshold mixes** store packets until the number reaches a threshold at which point all packets are sent out, **pooled mixes** packets are send out on a clock if a certain pool number is reached and **timing mixes** packets are send out on a clock even if 1 pack is present (breaking anonymity).

---
What is the problem with sender anonymity?  #flashcard #CS #AnonymousCommunication 
	With sender anonymity the user cannot receive packets back and must send their IP or send a return address. 

---
What is the key idea with return addresses and mixers?  #flashcard #CS #AnonymousCommunication 
	The key idea is we can send packets with not our return IP but the IP of a mix with out IP encrypted for that mix. This way only the mixes connected to us know our IPs.

---
What is the idea behind a mix cascade?  #flashcard #CS #AnonymousCommunication 
	The issue is a malicious mix could break our anonymity. But mixes can be chained by encapsulating traffic for mix inside the body for another. This way we only require one good mix to achieve anonymity.

---
