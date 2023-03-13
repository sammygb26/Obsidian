What are SSL and TLS? #flashcard #CS #SSL-TLS
	These are protocols that hope to ensure secure confidential transmission from point to point. These also ensure **integrity**: the data isn't changed as it moves.

---
What can SSL and TLS not hide about packets?  #flashcard #CS #SSL-TLS 
	SSL and TLS cannot hid where the data is going and who between as this information is in the headers so cannot be encrypted.

---
What is the authentication problem when it comes to packets?  #flashcard #CS #SSL-TLS 
	The problem is IP or TCP and UDP don't have inbuilt system to prove packets come from specific entities. Any computer can send any packet even if it looks like a different computer.

---
How does TLS and SSL get around the authentication problem?  #flashcard #CS #SSL-TLS 
	SSL and TLS get around the authentication problem by using a certificate authority to to provide authenticity to public key signatures.

---
What does SSL stand for and what is it?  #flashcard #CS #SSL-TLS 
	**Secure Sockets Layer** is a protocol developed by Netscape (and later Mozilla) which provides confidential and integral packets transfer.

---
What does TLS stand for and what is it?  #flashcard #CS #SSL-TLS 
	**Transport Layer Security** is a protcol developed to replace SSL. Similarly it provides confidential and integral packet transfer.

---
What was the hope with the TLS machine assisted proof (what went wrong)?  #flashcard #CS #SSL-TLS 
	The hope was that a logical proof could be made that TLS was secure and this would stop future problems arising. The issue is simplifications needed to be made to make the proof and these actually hid issues.

---
What is the threat model that motivates SSL and TLS? #flashcard #CS #SSL-TLS 
	In the threat model for TLS and SSL we assume an adversary can redirect traffic to its own server, passively read data and actively tamper with packets.

---
What is the security goal with TLS and SSL? #flashcard #CS #SSL-TLS 
	We assume as long as the client is honest and the adversary doesn't know the server's private key they shouldn't be able to Inject forged data (**integrity**) or distinguish the data stream form random bytes. **confidentiality**.

---
What are the goal of TLS and SSL?  #flashcard #CS #SSL-TLS 
	These hope to provide end-to-end confidentiality, end-to-end integrity. They require server authentication and have optional client authentication.

---
What is a public key certificate?  #flashcard #CS #SSL-TLS 
	A public key certificate is used to prove some public key belongs to some entity. A certificate authority will cryptographically sign a document specifying that a given domain has given them a given public certificate. This ensures the correct public key is used that only the true owner of the domain can decrypt.

---
What is the chain of trust with certificates?  #flashcard #CS #SSL-TLS 
	Certificates get verified by certificate authorities but they also have their public keys verified by certificates. This creates a chain of trust the goes back to root certificate authorities which usually run the web browser.

---
When is certificate revocation required?  #flashcard #CS #SSL-TLS 
	Certificate revocation is required when a certificates private key is compromised or the entity controlling the private key is show to be a mal actor.

---
What is one way to perform certificate revocation?  #flashcard #CS #SSL-TLS 
	One way is to have a list of revoked certificates posted and signed by the CA. Users periodically check this list to ensure they aren't using bad certificates.

---
How are setup and transmission different in TLS?  #flashcard #CS #SSL-TLS 
	In the setup phase of TLS public key cryptography is used to establish a private key. This is then used for data transmission. In the setup phase **confidentiality** is given by public key encryption. **Integrity** is given by public key signatures. **Authentication** is given by a public key certificate. In the transmission phase both ides have established a secret key and so symmetric encryption provides **confidentiality** while *MACs* provide **integrity**. Authentication isn't required as it is implied by the secret keys from the previous step.

---
What are the 5 broad steps to TLS?  #flashcard #CS #SSL-TLS 
	1) Proposed crypto, 2) Select crypto, 3) Certificate, 4) Key exchange 5) Data transfer.

---
How is basic RSA key exchange performed?  #flashcard #CS #SSL-TLS 
	In basic RSA key exchange a client can generate a random number. It can then encrypt this message with a server's public key. The encrypted message is sent to the sever which can then decrypt it. Both then have the secret random number.

---
What is forward secrecy?  #flashcard #CS #SSL-TLS 
 A scheme is forward secret if the key being compromised doesn't compromise messages sent in the past.

---
How is forward secrecy achieved?  #flashcard #CS #SSL-TLS 
	Forward secrecy can be achieved by getting rid of long lived private keys. As without these nothing can be recovered.

---
Why can long lived RSA private key snot provide forward secrecy?  #flashcard #CS #SSL-TLS 
	An attached can record all messages sent between a client and a server. In the future once the keys have been broken all messages including private key exchange can be recovered.

---
What are the steps to Diffie Hellman key exchange?  #flashcard #CS #SSL-TLS 
	This is a way to establish a shared random key. Two parties both independently generate random numbers $x$ and $y$. Then each also knows $g$ a generator of $Z_p$ for a known $p$. Then $A$ sends $g^x$ to $B$ and $B$ sends $g^y$ to $A$. Each can then raise it to their random number which in both cases will give $g^{xy}$. This hasn't been send in the open and is computationally hard to reverse.

---
What is a problem with a basic implementation of DH key exchange?  #flashcard #CS #SSL-TLS 
	Basic DH key exchange has no authentication. This means a MITM attach can be performed when an attacker generates a private key for both parties and decrypts messages in between them.

---
What is a possible attack on signed DH key exchange in TLS?  #flashcard #CS #SSL-TLS 
	One possible attach is to perform a MITM attack and down grade the proposed crypto schemes send by the client to only include broken versions. When the key exchange is performed the attacker can break it at every step revealing the secret key.

---
In signed DH what changes?  #flashcard #CS #SSL-TLS 
	Here at the end the server can sign and send a hash of the XOR of the exchanged messages. This ensures the server received both and there is no MITM giving two keys between the client and server.

---
