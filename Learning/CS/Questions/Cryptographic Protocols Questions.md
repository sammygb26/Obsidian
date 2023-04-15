What kind of attacker capabilities to cryptographic protocols attempt to defend against? #flashcard #CS #CryptographicProtocols
	Cryptographic protocols attempt to defend against attackers who can, *record messages*, *insert new messages*, *redirect messages*, *reorder messages* and inject new messages. Basically they control the network.

---
Why is it important to ensure we give hypothetical attackers powerful capabilities when it comes to designing cryptographic protocols? #flashcard #CS #CryptographicProtocols 
	We need to rely on cryptographic protocols and we will assume they always protect our data. So we want any attacker even ones who completely control the network to be incapable of breaking our security. This ensures our messages are as secure as we expect them to be and so we can rely on them. These are also realistic capabilities when it comes to MITMs or governments.

---
What are the capabilities of a MITM? #flashcard #CS #CryptographicProtocols 
	A MITM basically controls the network between the two entities. They can forge request, repeat request, alter messages and inject their own messages. All while reading all packets.

---
What is wrong with just encrypting and sending messages with MACs to create cryptographic protocols? #flashcard #CS #CryptographicProtocols 
	Even with these measures in place the network can still suffer replay attacks where the attacker sends multiple messages at once.

---
