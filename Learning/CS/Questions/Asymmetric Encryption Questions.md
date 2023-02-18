Even with some perfect symmetric encryption scheme what problem still remains? #flashcard #CS #AsymetricEncryption
	We will still have the problem of key management and how we ensure two parties have the secret key without a man in the middle.

---
What is present when we have a trust their party? #flashcard #CS #AsymetricEncryption
	When we have a trusted third party we assume this TPP shakes a secret key with each user individually.

---
How does Paulson's variant of the Yahalom protcol work? #flashcard #CS #AsymetricEncryption 
	- Here $A$ can request to establish a private key with $B$ by sending its identifier and a nonce. 
	- Then $B$ can encrypt this and send it to $S$ (the authority) along with $B$'s identifier and another nonce. 
	- $S$ can decrypt and find this was $A$ establishing a session with $B$. 
	- $S$ then encrypts and sends $A$: $B$'s name and a private key $K_{AB}$ which $S$ has created.
	- $A$ also receives $B$'s nonce. A can decrypt its message find $K_{AB}$ and the forward the part of the message encrypted for $B$ along with the nonce encrypted with the private key.
	- $B$ can they decrypt their part of the message finding $K_{AB}$, $N_B$ is then decryptable proving $A$ has the private key and since $B$'s private message contains the name of $A$ we know $S$ encrypted that message for $A$.

---
Why are nonces used instead of just fixed numbers in Paulson's variance of the Yahalom protocol? #flashcard #CS #AsymetricEncryption 
	Nonces are used to prevent replay attacks.

---
What is the idea behind public key encryption? #flashcard #CS #AsymetricEncryption 
	In public key encryption there is a public and private key. An entity always keeps a private key and therefore can decrypt messages. This has a corresponding public key which can be used to decrypt messages but not encrypt them. Knowing a public key you can send someone a message but not read messages sent to them.

---
What is the mathematical of public key encryption? #flashcard #CS #AsymetricEncryption 
	We have a key generator algorithm $G:\to\mathcal K\times\mathcal K$ which gives two keys. One is the private and one is the public. Then we have the encryption algorithm taking the public key $E:\mathcal M\times\mathcal K\to \mathcal C$ and the decryption scheme taking the private key $D:\mathcal C\times \mathcal K\to\mathcal M$.

---
What is the Euler phi functions values for a prime number? #flashcard #CS #AsymetricEncryption 
	Since $\phi(p)$ is the number of numbers smaller than $p$ that don't share a factor with it by definition of $p$ being a prime $\phi(p)=p-1$.

---
For two primes what is phi(pq)? #flashcard #CS #AsymetricEncryption 
	This will be $\phi(pq)=(p-1)(q-1)$

---
What is Eulers theorem with it comes to some x in Z*? #flashcard #CS #AsymetricEncryption 
	This will be that $$\forall n\in\mathbb N,\forall x\in \mathbb Z_p^*,\text{ if gcd}(x,n)=1\text{ then }x^{\phi(n)}=1\mod n$$

---
What is the idea of intractable problems that public key encryption tries to exploit? #flashcard #CS #AsymetricEncryption 
	This kind of encryption exploits **intractable problems** these are problems for which a way to find the solution is known. But we cannot fin the solution as it would take too much compute.

---
What are some examples for intractable problems? #flashcard #CS #AsymetricEncryption 
	Some commonly used ones are **factoring**, **RSAP**, **Discrete Log** and **DHP**.

---
What is the factoring intractable problem? #flashcard #CS #AsymetricEncryption 
	Some commonly uses ones are **factoring** where we want to find the unique prime factorization of a number (hard for a prime composite for a large primes).

---
What is the RSAP intractable problem? #flashcard #CS #AsymetricEncryption 
  **RSAP** we are given a number $n=pq$ with $2\le p,q$ two primes. We are given $e$ such that $gcd(e,\phi(n))=1$. Then for $m^e\mod n$ we want to find $m$.

---
Wat is the DMP intractable problem? #flashcard #CS #AsymetricEncryption 
	**DHP** we are given a prime $p$ and a generator $g$ of $\mathbb Z_p^*$, then numbers $g^a\mod p$ and $g^b\mod p$. We want to find $g^{ab}\mod p$.

---
What is the Discrete log intractable problem? #flashcard #CS #AsymetricEncryption 
	Here we are given some prime $p$, generator of $\mathbb Z_p^*$ and $y\in\mathbb Z_p$ we want to find $x$ such that $y=g^x\mod p$.

---
How does the Diffie-Hellman protocol work? #flashcard #CS #AsymetricEncryption 
	In the **Diffie-Hellman** protocol we exploit the hardness of DMP. We pick some very large prime and make it publicly available. Both $A$ and $B$ generate some $a$ and $b$ from $\mathbb Z_p$ respectively. Then $A$ and $B$ generate $g^a$ and $g^b$ respectively and send it to each other. $a$ and $b$ can't be revealed as discrete log is hard. Then each can raise what they received to the power of their private numbers to ensure they both have $g^{ab}$ without transmitting it.

---
What is the DHP man in the middle problem? #flashcard #CS #AsymetricEncryption 
	The problem with DHP is a man in th middle can trick both sides into establishing a secure connection by pretending to be the opposite. They will never get $A$ and $B$'s numbers but can get the private key for each.

---
What is needed in the set up of RSA? #flashcard #CS #AsymetricEncryption 
	In the set-up of RSA we have a composite $N=pq$ for large primes $p$ and $q$. Then we find $e,d\in Z$ such that $ed=1\mod \phi(n)$. Then our private key is $pk=(N,e)$ and our secret key is $sk=(N,d)$.

---
How does encryption and decryption work in RSA? #flashcard #CS #AsymetricEncryption 
	In RSA to encrypt a number $x$ we take for public key $pk=(N,e)$ $$RSA(pk,x)=x^e\mod N$$then to decrypt with secret key $sk=(N,d)$ we take $$RSA^{-1}(sk,x)=x^d\mod N$$

---
Why does RSA work? #flashcard #CS #AsymetricEncryption 
	To break RSA we know $x^e\mod N$, $d$ and $N$ and we want to find $x$. We also know $N=pq$ for large prime $p$ and $q$. We know $gcd(e,\phi(n))=1$. But his is computationally intractable to solve.

---
If we use pure RSA what is this called and what should be done instead? #flashcard #CS #AsymetricEncryption 
	Using RSA on its own is called using **raw RSA** the problem it is deterministic and so vulnerable to chosen plaintext attacks. Instead it is best used to transmit symmetric encryption keys.

---
What is the point of the ISO standard for RSA? #flashcard #CS #AsymetricEncryption 
	The point is to avoid the problems of a chosen plaintext attack that could nullify RSA due to its determinism.

---
How does the ISO standard work? #flashcard #CS #AsymetricEncryption 
	Here we have a symmetric encryption scheme $E_s$ and $D_S$ over $(\mathcal M, \mathcal C,\mathcal K)$. Then we have some random key generator $H:\mathbb Z_N^*\to \mathcal K$. We can encrypt $x$ to give $y$. Then we return $y||E_s(k,m)$. To decrypt the second part the first part $y$ must be decrypted. This can only be done with the RSA private key.

---
What is ElGamel without going into details? #flashcard #CS #AsymetricEncryption 
	ElGamel is a asymmetric encryption scheme. It takes in a message in $\mathcal M$ and returns a cipher twice the length so in $\mathcal M\times\mathcal M$.

---
What are the private and public keys in ElGamel? #flashcard #CS #AsymetricEncryption 
	The private and public keys are $G_{EG}()=(pk,sk)$ where $pk=g^d\mod p$ and $sk=d$. Due to the hardness of discrete logarithm we cannot find $sk$ from $pk$.

---
What are the encryption and decryption algorithms for ElGammel? #flashcard #CS #AsymetricEncryption 
	These are $$E_{EG}(pk,x)=(g^r\mod p), m\cdot (g^d)^r\mod p))$$here $pk=g^d\mod p$. Then $r$ is random from $\mathbb Z$. decryption works as $$D_{EG}(sk,x)=e^{-d}c\mod p$$ where $x=ec$. $-d$ comes from the private key and cancels out the $d$ used in encryption. But it also multiplies against $r$ and so it cancels out too.

---
