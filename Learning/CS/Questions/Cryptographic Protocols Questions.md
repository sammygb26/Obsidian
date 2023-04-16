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
What properties must a cryptographic protocol have? #flashcard #CS #CryptographicProtocols 
	**Confidentiality** (information isn't revealed to unauthorized peoples) **Integrity** (information isn't altered by unauthenticated peoples) **Authenticity** (ability to know the identity of a communicator) **Anonymity** (identify of the author is kept private) **Unlinkability** (service destination to the same author is hidden) **Non-repudiation** (author cannot say some action is faked).

---
What are cryptographic protocols? #flashcard #CS #CryptographicProtocols 
	These are distributed program that rely on **cryptographic primitives** to establish secure communications.

---
What is an example given of a logical attack on an encryption scheme? #flashcard #CS #CryptographicProtocols 
	The idea is a scheme that exploits commutativity. This way a key can be added to an encrypted message then the key below decrypted so the received can decrypt the message on their own. The problem is there is no way to stop an attacker form faking their own key into the mix

---
How can we reduce the attack surface on public keys? #flashcard #CS #CryptographicProtocols 
	We can do this by limiting the number of things we use one for. E.g. only use for encrypting or signing. We can also only use them to send session keys instead of bulk encrypting.

---
Why is it important to reduce the attack surface? #flashcard #CS #CryptographicProtocols 
	We want to reduce the attack surface to ensure attackers have as little of our public keys to work with as possible.

---
Why are session keys used? #flashcard #CS #CryptographicProtocols 
	Long term keys should be used sparingly. This way instead session keys are used which are forgotten and so forward secrecy is achieved.

---
How does Needham-Schroeder Public Key? #flashcard #CS #CryptographicProtocols 
	Here we want to send over two nonces to provide private key encryption. This is all done under public key encryption. The basic idea is $A$ sends a nonce and their name to $B$. $B$ then decrypts this and sends the nonce and their own nonce back to $A$ proving they hold $B$'s private key. $A$ decrypts this and sends their name and $B$'s nonce to $B$ proving they are $A$.

---
What is the problem with Needham-Schroeder Public key scheme? #flashcard #CS #CryptographicProtocols 
	The issue is $B$ never specifies their identity in an authenticated way and so never authenticates to $A$. This way $E$ can sit in the middle and since the nonces are used as future private keys and are decrypted and send back for authentication this decryption can be exploited allowing $B$ to remove the encryption $B$ puts on its nonce when sending it to $A$.

---
How is forward secrecy different from regular secrecy? #flashcard #CS #CryptographicProtocols 
	The difference is even if protocols are secure to cryptographic breaking keys may still be leaked in the future. To avoid this session keys should be used. This way the messages are secure if a fuller way.

---
How does the station to station protcol work? #flashcard #CS #CryptographicProtocols 
	In the station to station protocol we with to create a encrypted channel (shared secret key) between two authenticated peoples.
	1. So we have $g,p,g^x$ sent to $B$. 
	2. $B$ can then generate their own $g^y$ and sent that along with a certificate for their PK and encrypt a a signed message of the two private key parts $g^x$ and $g^y$ signed with their public key and encrypted with the private key $g^{x,y}$. 
	3. Form this $A$ can get the same private key and authenticate $B$ from their signature. 
	4. $A$ then does the same to $B$ authenticating that they sent the original message (since they know $x$) and so can encrypt their signature with the private key.

---
How is the old SSL/TLS handshake performed? #flashcard #CS #CryptographicProtocols 
	A party wishing to set up a channel request one. In response the server gives their certificate. This is then used to send a private key over. Both parties now have a private key they can use to send messages.

---
What was the problem with the old SSL/TLS when it came to reconnection? #flashcard #CS #CryptographicProtocols 
	The issue was full authentication wasn't performed during reauthentication and so attackers could DOS a session and then reconnect themselves between.

---
