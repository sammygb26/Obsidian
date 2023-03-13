These are protocols that hope to ensure secure and confidential information transmission from point to point. These methods will also ensure **integrity** so that the data cannot be changed as it moves. We do not defend against directionality of travel. We don't hid who is talking to who. Which is a kind of **metadata**.

![[Pasted image 20230216100834.png]]

### Authentication Problem
The problem is we cannot tell who is sending what packets. We cannot tell the difference between a packet and a packet with a spoofed IP for example. We only get the bits that come in. We cannot **authenticate** which packet is the authentic one. One way is to use an unforgeable certificate from a Certificate Authority.

### SSL / TLS
**Secure Sockets Layer** was developed by Netscape (later Mozilla). In SSL version 3 many issues were fixed by there were still many issues. Another group developed TLS **Transport Layer Security** which has some better properties. TLS version 1.0 replaced SSL in 1999. It was published as a RFC 2246. There were still problems with TLS with TLS 1.3 coming out in 2018. This protocol works on top of TCP/IP but bellow application protocols.

##### Problems
In 1995 SSL3 was found to have predicable IV, in 1996 **MD5** was found to have some collisions (making in insecure), in 1998 **PKCS1** the padding system was found to have a vulnerability allowing the private key to be found. But there was many more attacks from 2000 - 2013 etc.

So they decided to come up with a way to get ahead of the game and prove a protocol is unique. So it is represented in a logical form we can then try to prove theorems which will prove security in some ways. **Machine-assisted proof** was used for this to ensure no mistakes were made. So TLS was represented mathematically and then we proof it's security. This is better than just testing.

A problem it we need to drop some detail to actually prove anything. If we only take out small details we can make proofs. But these proofs may not connect to reality if we took out the wrong details. This started in ~2012.

When **TLS 1.3** was released they attempted to prove it was secure. They managed but  vulnerabilities were found that allowed TLS to be broken again. Another point is even if this is perfect still need to implement it and there may be errors. It may also have to suite older machines or code which make it insecure.

### Secure Channels For the Web

![[Pasted image 20230216102703.png]]

**Context**: we have a client connecting to a server. There is some **adversary** somewhere in the network. The *threat model* is 

- It can redirect traffic to its own server (DNS rebinding)
- It can passively read all data (IP monitoring)
- It can play an active malefactor-in-the-middle (TCP hijacking)

**Security goal**  As a long as the client is honest and the adversary does not know the server's private key it shouldn't be able to 

- Inject forged data into the data stream (**integrity**)
- Distinguish the data stream from random bytes (**confidentiality**)

##### Goals of SSL/TLS
End-to End confidentiality means we want encrypted communication between client and sever. End-to-end integrity means we want to detect communication corruption between client and server. We also want required server authentication - identity of server is proved to the client. Optional client authentication - identity of client is optionally proved to server. **Modular deployment** - intermediate layer between applications and transport layer, handles encryption authentication on behalf of the client and server applications. It should be hard to implement this wrong.

### Certification
**Public key certificate** - it used to assure a their party that a public key is associated with an identity.

**Certificate fields** - The *issuer* says who made the certificate, the *subject* is who is being authenticated *www.google.com*, subjects public key parameters (RSA2048), subject's public key is also sent, validity period (incase secret key is leaked), signature parameters and a signature proving all of the above was made by the CA.

### Chain of Trust and Revocation
We have **Transitive trust** meaning if we trust $A$ and $A$ trusts $B$ we should trust $B$. Each layer trusted authority is has a authority trusted them. To check an authority we go to the layer above. This all comes back to a root which are *baked* to our browsers and we just write in the public key.

We trust the top layers as these are large companies which we trust wont do the wrong this as it would hurt them.

**Certificate revocation** - this is needed when a private key is leaked or a company is found to be a mal actor. One way it for everyone to have a string they send to their authority to say they're key is no longer secure.

**Revocation method** - we can have a list of revoked certificates posed to CA's websites. Online verification services provides by CA (OSCP stapling)

### Rogue Certificates: DigiNotar hacked in 2011
Here a CA got hacked and could issue any certificate they wanted. For example they issues google.com certificates. Then any connector will encrypt their traffic in a way the adversary can read it. This was used to attack the Gmail of the Dutch government and get all of their usernames and passwords.

http://www.onderzoeksraad.nl/uploads/items-docs/1833/Rapport_Diginotar_EN_summary.pdf

No one wanted *DigiNotar* certificates and they went out of business. They were removed from the chain of trust.

# TLS Building Blocks
There are two phases to TLS the **setup phase** and the **data transmission phase**.

![[Pasted image 20230216104952.png]]

The setup uses public key encryption which is **expensive** then **symmetric keys** are used in the main phase which is cheaper.

### TLS Overview
IN a simplified way the browser sends supported crypto, then the server response with what crypto it can do. Then certificate is sent to authenticate the web server. Then we perform a **key exchange**. We now have get a symmetric private key and can perform data transmission.

![[Pasted image 20230216105145.png]]

### Basic Key Exchange
This is called **RSA key exchange** for historical reasons. The client generates a random secret R, then it encrypts it and sends it to the web server with the public key for the server. Both then have the secret $R$.

![[Pasted image 20230216105304.png]]

**Forward secrecy** - The idea here is if the key is compromised it wont compromise message sent in the past. For this we get rid of long lived private keys as if these keys are removed we loose everything.

![[Pasted image 20230216105427.png]]

**Diffie Hellman Key Exchange** - Here pubic parameters prime $p$ and generator $g$ of $Z_p$. Then a client generates random $x$ and server generates random $y$. We then send $g^x$ to the server and $g^y$ to the server. Then each can find $g^{xy}$ the random numbers are then thrown away and we have a short term secret key $k$. 

![[Pasted image 20230216105635.png]]

**Malefactor in the Middle** - Here we have some entity in the middle which authenticates to the other pretending to be the other other. 

![[Pasted image 20230216105724.png]]

To get around this we can use **authentication** when sending the messages.

### Signed DH Key Exchange

![[Pasted image 20230216105800.png]]

They MITM doesn't have the server's secret key so cannot authenticate and sit in the middle. But this doesn't work Here a MITM may intercept the crypto transmission to the server. This can force the server to authenticate with a broken security measure. We can break the servers secret key for this *insecure* mean and then authenticate messages.

![[Pasted image 20230216110101.png]]

This can be solved by **signing the transcript**.

[[SSL TLS Questions]]