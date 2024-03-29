What is the aim of digital signatures? #flashcard #CS #DigitalSignatures
	The aim with digital signatures is to provide a way to prove some entity made a given message. A signature is send along with the message that can be checked against that entity's public key to verify they signed the message.

---
How does a MAC work? #flashcard #CS #DigitalSignatures 
	A MAC is a **Message Authentication Code** this works by having using a symmetric encryption scheme to hash a message. The recipient can perform the same action at the other side to verify the message.

---
What are the downsides of backs? #flashcard #CS #DigitalSignatures 
	MACs are not publicly verifiable you must know the private key to verify them. There is also the problem that the private keys are always shared by nature (at least between two people) and therefore the signature doesn't really prove who authenticated it.

---
What is the existential unforgeability property? #flashcard #CS #DigitalSignatures 
	This means that an attacker with a collection of chosen cipher texts and signatures shoudn't be able to create a new signature for an arbitrary message.

---
How does RSA signing work? #flashcard #CS #DigitalSignatures 
	In RSA signing we simply encrypt some message with RSA then send the message and the cypher text (encrypted with the private key). To verify a signature we only need check the public key can decrypt the message. RSA works in a symmetric way that allows this.

---
What is the problem with textbook RSA signing? #flashcard #CS #DigitalSignatures
	With textbook RSA signing the signature for two messages multiplies together is the two signature multiplied together. This provides a road to **forging signatures**.

---
How can signatures be forges with textbook RSA signing?   #flashcard #CS #DigitalSignatures  
	The issue is for messages $m_1$ and $m_2$ we can get signatures $s_1$ and $s_2$. Where $s_1=m_1^d\mod n$ but then $s_1s_2=m_1^dm_2^d=(m_1m_2)^d$ is a valid signatures for $m_1m_2$! This makes RSA textbook signing mutable.

---
What is the solution to make textbook RSA signing secure? #flashcard #CS #DigitalSignatures 
	Instead of signing the message we sign a hash of the message. This means the relationship between two messages and two signatures is unintelligible as the hash between block any inference. This also **speeds** up computation as hashes are much smaller.

---
What are the three properties we want in a signature security wise? #flashcard #CS #DigitalSignatures  
	We want **non-forgeability** where an adversary can forge a signature for a document that hasn't been signed and **non-mutability** where its difficult to take an existing signature and convert it to sign another message. Together these mean the signature provides **non-repudiation** and the signer can't assert they didn't sign something.

---
