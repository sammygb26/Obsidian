To establish secure communication with cryptography we need to somehow verify we have some public key for sure. If we used the wrong public key then the real own of the public key could decrypt the message. Then also for verifying we need to know the public part of the key.

![[Pasted image 20230210102950.png]]

### Different Options
1. **Public announcements** - participant broadcasts the public keys but this doesn't defend against forgeries as at this point there is no cryptographic verification.
2. **Publicly available directories** - participants public keys on public directories.
3. **Public-key authority** - participants contact the authority for each public key (*but this creates a bottleneck in the system*)
4. **Public-key certificates** - CAs issues certificates to participants of their public key. This will be as reliable as the public key authority by avoids a bottle neck (: - this creates a hierarchy of CA accrediting each other.

### Public Key Certificates
![[Pasted image 20230210103302.png]]

A certificate consists of a **public key**, a **subject** identifying the owner of the key and a **signature** by the CA on the key and the subject binding them together. We assume the CA is trusted.

##### X.509 Certificates

![[Pasted image 20230210103526.png]]

X.509 defines a framework for the provision of authentication services. This is used by many applications such as TLS.

### Securing the Network

![[Pasted image 20230210104125.png]]

**HTTPS** creates a secure form of the internet. We trust our browser to be secure when the website we are visiting has a verified certificate for the URL. This gives a public key allowing traffic to the network to be encrypted. We can then similarly encrypt and send our public key allowing secure communication back.

![[Pasted image 20230210104158.png]]

### Browser Root Certificates
There are some signatures build in which can accredit lower down certificates.

### Chain of Trust
Having a CA sign all certificates is not practical so instead a root CA signs certificates for level 1 CAs, level 1 CAs sign certificates for level 2 CAs and so on.

![[Pasted image 20230210104058.png]]

### Self-Signed Certificates

![[Pasted image 20230210104617.png]]

Some can be self signed and we choose whether or not to trust them.

### Lenovo Superfish Scandal
Here laptops came with preloaded browsers with modified root signatures which allowed adds to take hold.

Scandals can also happen when countries controlling CAs force them for fake signatures. In this case higher level authorities will remove the offending CA. 

### Revocation
A certificate need to be revoked if the corresponding private key has been compromised. Certificate revocation lists CRLs are the solution adopted in X.509. Online certificate status protocols OCSP stapling is the modern solution to this problem.

[[Public Key Infrastructure]]

