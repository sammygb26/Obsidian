These are schemes for transmitting data securely from entity to entity. Used in eBanking, eComerce, eVoting, Blockchains etc. With these protocols we have a model of what the attacker can do.

- We assume **attacker can** : record messages, alter messages, delete messages, insert new messages, redirect messages, reorder messages, and reuse past or current messages, inject new messages.

These things are all possible in one way or another on the internet. If we have a system that is secure to all of these then we can be sure our messaging is secure. This is important as often **attackers control the network**.

An example could be a unencrypted login. Looking at the traffic will reveal the password and user information.

![[Pasted image 20230213100710.png]]

### Required System Complexity
We may suppose we have a secure transaction with a banking site. If we have some properly encrypted message. With an authentication code.

![[Pasted image 20230213100838.png]]

But a **replay** attack could allow an attacker to duplicate this transaction.

![[Pasted image 20230213100911.png]]

To achieve more complex properties we want

**Confidentiatlity** - Information isn't revealed when not authorized
**Integrity** - Data should not be altered in an unauthorized manner
**Authentication** - Ability to know with certainty the identity of a communicator
**Anonymity** - the identity of the author of an action is kept private
**Unlinkability** - An attacker should not be able t deduce whether different services are delivered to the same user
**Non-repudiation** - The author of an action should not be able to deny having triggered an action

### Cryptographic Protocols
![[Pasted image 20230213101219.png]]

We should be careful as many exploit errors are due not to design errors in primitives, but they way they are used like bad protocol design and buggy or not careful implementation.

### Logical Attacks
These don't even break crypto primitives! An example could be a communication with a symmetric encryption schemes which is **commutative**

![[Pasted image 20230213101439.png]]

Where $\{m\}_k$ denotes the encryption of message $m$ under key $k$. Like for example with a stream cipher.

![[Pasted image 20230213101728.png]]

Here $A$ sends a message to $B$. Then $B$ sends some message bac to $A$. $A$ proves they control $K_A$ by revealing $K_B$. Due to commutivity bob's encrypted message can be revealed. He can then decrypt this and get the key $B$.

But a problem with this is $I$ can intercept the message to $B$ and make up their own key. This allows the whole handshake to go the same. $A$ has no way to know the different between $K_I$ and $K_B$ encrypted messages.

### Authentication and Key Agreement Protocols
General these protocols are designed so that the **attack surface** is as small as possible. The harder variant is always used. For example in RSA we usually use different keys to encrypt and signing. Instead we can use different keys incase there is an issue with our implementation that could exploit this.

Public keys algorithms tend to be computationally more expensive that symmetric keys. Hence why we use them to send secret keys. Another reason is these long term keys are used **sparingly** to reduce attack surface. We instead use **session keys** which are forgotten after a session.

### Needham-Schroeder Public Key (NSPK)
![[Pasted image 20230213102512.png]]

Here 1) $A$ makes up a nonce $N_A$ and encrypts and sends this and her name to $B$ using $B$'s public key. Then $B$ does the same with a new nonce $N_B$ and the decrypted nonce $N_A$. Then $A$ derypts $B$'s nonce and sends the nonce back. The nonces can then be used to create a new secret key. This was *widely used*.

##### Security Requirements
**Authentication** - if Alice has complete the protocol apparently with $B$ then $B$ must have completed the protocol with Alice. No one else could have fakes this protcol. This is vulnerable to MITM attacks and recording attacks.
**Authentication** - If $B$ has completed the protocol $A$ must have completed with $B$
**Confidentiality** - Messages send encrypted with the agreed key $(k\gets h(N_A,N_B))$.

##### NSPK Lowe's attack on authentication
Here $A$ sends a message to $I$ a agent. $I$ can decrypt this message and encrypted it to $B$. Then $B$ things $A$ is making a secure channel with himself. $B$ then tries to encrypt a message and send to $A$. $I$ can't decrypt this but sends it to $A$. $A$ will decrypt this and send it to $I$ **with $I$'s key**. Hence B's nonce is sent to $I$ with $I$'s secret key. $B$'s nonce decrypted by Alice can be send to $B$ and so $B$ believed $I$ is Alice.

![[Pasted image 20230213103141.png]]

This doesn't work on the maths level of the primitives but the logical level of the protocol. A fix to this is to send $B$'s name encrypted with $A$'s key.

![[Pasted image 20230213103507.png]]

This way $A$ knows if a message is being passed on.

### Forward Secrecy
The NSL protocol is secure against an attacker that controls the network. What what if $A$ and $B$ have compromised private keys. If if $A$ or $B$ reveals their private keys. Could we still protect confidentiality?

![[Pasted image 20230213103748.png]]

That is the messages can't be encrypted years later. This is a reason why **session keys** are used and then thrown away. **Long-term** keys are used to send these session keys. *Session keys* are thrown away.

### The Station-to-Station protocol
Here where $p$ is a large prime and $g$ is a generator of $\mathbb Z^*_p$.

![[Pasted image 20230213104000.png]]

First $p$ is picket then $x$ is picket from the modular set $\mathbb Z_p$ which will be used as part of the session key. Then $g$, $p$ and $g^x$ is sent, but it is hard to retrieved $x$. $B$ then generates some $y$ from $\mathbb Z_p$ similarly. $B$ then sends $g^y$, a certificate authenticating a public key for $B$. Then $g^{yx}$ is used as a new secret key. $g^x$ and $g^y$ is signed and sent to $A$. $A$ now knows $g^y$ so can get $g^{xy}$. $A$ can then verify $B$ has signed $g^x$ and $g^y$. The **certificates** serve to ensure the identity of $A$ and $B$. It is hard to find $g^{xy}$ knowing only $g^x$ and $g^y$.

![[Pasted image 20230213104735.png]]

Secret keys are only used to identity proving. The session key is used for **all** enecryption.

### Old SSL/TLS handshake Protocol

![[Pasted image 20230213104917.png]]

A similar approach to above is used here.

### SSL/TLS Renegotiation Weaknesses
Here connection is blocked. While renegotiating during reconnecting identity isn't reauthenticated to make the system cheaper. Hence an attack could sneak in-between.

![[Pasted image 20230213105047.png]]

### Marsh Ray's Plaintext Injection Attack on HTTPS

![[Pasted image 20230213105145.png]]

Here a protcol doesn't differ between the content of messages and the actual commands. Hence the content can be changed to execute commands.

![[Pasted image 20230213105310.png]]

Automated reasoning is being attempted to be used to prove protocols are secure.