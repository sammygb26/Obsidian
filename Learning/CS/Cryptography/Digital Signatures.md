We have a key generation algorithm giving a public and private key. Then the secret key can be used to sign a message. Providing a signature given a text. Then the public key can be used to verify a text given the public key.

![[Pasted image 20230210100619.png]]

### Digital Signatures over MACs
![[Pasted image 20230210100707.png]]

Here we want a signature to be sent with a message proving the signer has sent it.

![[Pasted image 20230210100735.png]]

We want this to be **publicly verifiable** so anyone can verify a signatures. These signature are **transferable** since they can be verified publicly. They must also provide **non-repudiation** - if Alice signs a document with her secret key, she cannot deny it later.

### Security
A good digital signature scheme should satisfy existential unforgeability.

![[Pasted image 20230210100943.png]]

That is even given messages and signed version of those messages which are even chosen. They should still not be able to get some new message signed on their own.

### Textbook RSA Signatures
$G_{RSA}=(pk,sk)$ where $pk=(N,e)$ and $sk=(N,d)$ and $N=pq$ with $p,q$ random primes and $e,d\in\mathbb Z$ with $e\cdot d=1\mod\phi(N)$. Here our messages and ciphers are $\mathcal M=\mathcal C=\mathbb Z_N$. To **sign** some message we give $$S_{RSA}(sk,x)=(x,x^d\mod N)$$where $pk=(N,e)$. Then verifying will be done as 

![[Pasted image 20230210101656.png]]

Where $sk=(N,d)$. This gives 

![[Pasted image 20230210101722.png]]

### Problems with "textbook RSA Signatured"
![[Pasted image 20230210101748.png]]

If Eve has two valid signatures $\sigma_1=M_1^d\mod n$ and $\sigma_2=M_2^d\mod n$ from Bob on messages $M_1$ and $M_2$. Then Eve can exploit the homomorphic properties of RSA and produce a new signature

![[Pasted image 20230210101919.png]]

Which is valid for the message $M_1\cdot M_2$. This may not always be useful as we need very specific messages to get meaningful output.

### How to use RSA for signature
![[Pasted image 20230210102038.png]]
So we sign as $S(sk,x)=(x,H(x)^d)\mod N$. Verifying we then simple verify by hashing the message

![[Pasted image 20230210102139.png]]

This also has the advantage of reduce the size of our message and so makes RSA easier to compute.

[[Digital Signatures Questions]]