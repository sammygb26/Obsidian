![[Pasted image 20230131110738.png]]

A more modern definition is given by 

![[Pasted image 20230131110752.png]]

And so Cryptography has many uses nowadays. All these uses are enabled by the mathematics of cryptography. An important remark is 

![[Pasted image 20230131110813.png]]

In this section we will learn to appreciate the variety of applications that use cryptography with different purposes, the basic concepts of cryptography, understand types of problems cryptography addresses and understand the types of problems that need to be addressed. 

![[Pasted image 20230131110841.png]]

Symmetric Encryption both parties share the same private key while in asymmetric encryption there is a public and private key. 

# Symmetric Encryption
Here we want to make some files inaccessible to some and accessible to others. We may want *secure communications* or *file protection*.

![[Pasted image 20230131110901.png]]

$\mathcal K$ is the key-space, $\mathcal M$ s the message space and $\mathcal C$ is the cypher-space. Then we have the property that $ED=I$ under function composition.

![[Pasted image 20230131110925.png]]

They key is a **shared secret** and this only works when no-one else knows the key. We want this scheme to be secure against adversaries.  We don't wan the adversary to uncover the secret key $k$, the plaintext $m$ underlying a cipher $c$ or recover *any* bits of the plaintext $m$ underlying a ciphertext $c$.

##### Kerckhoff's principle
The architecture and design of a security system should be public.

![[Pasted image 20230131110943.png]]

Open design allows a system to be scrutinized by many users and white hat hackers. This also means the system is only cracked when the private key is found. Also with a non-public scheme individuals may know how it works and so how to decrypt a message hence there is a human weak spot.

##### Adversary's capabilities
![[Pasted image 20230131111003.png]]

So we look at how our attacker functions in order to understand how they might break out encryption. The attacks known encryption / detection algorithm but may have access too

**Ciphertext only attack** - the attacker only knows the secret
**Known plaintext attack** - some plaintext / ciphertext pairs are known (can happen if known part of a message is encrypted)
**Chosen plaintext attack** - has access to an encryption oracle - can maybe trick a user to encrypt messages $m_1,...m_n$ of his choice
**Chosen cyphertext attack** - he has access to a decryption oracle - can trick user to decrypt ciphertext $c_1,...c_n$.

This also comes to how much **computational power** we need to break a scheme. For example old schemes are outdated and can be brute forced nowadays.

##### Brute-force attack - attack on all schemes
Here we try all possible keys $k\in\mathcal K$ - request some knowledge about eh structure of plaintext keys so we know when we have correctly decrypted the cyphertext.

Making exhaustion search unfeasible can be done by making $\mathcal K$ sufficiently large. Keys should also be sampled uniformly.

### Substitution Cipher
Here we have a shared secret which is a permutation $\pi$ of the set of characters

![[Pasted image 20230131111032.png]]

Encryption we apply $\pi$ to each character

![[Pasted image 20230131111048.png]]

To decrypt we appl $\pi^{-1}$

![[Pasted image 20230131111101.png]]

The key space is fairly large $|\mathcal K|=26!=(\approx 2^{88})$ so we can use naive brute force. But we can use known words and general patter in order to decrypt the message. For example we can use word frequencies, common words. This will reveal more words and we can then complete words with most likely letters to continue decryption.

### One-Time Pad (OTP)
This is a better substitution scheme. Here we deal with strings of bits of the same length $n$. $$\mathcal M=\mathcal C=\mathcal K=\{0,1\}^2$$In encryption we simple perform $$\forall k\in \mathcal K.\forall m\in \mathcal M. E(k,m)=k\oplus m$$So this is a XOR we just flip bits

![[Pasted image 20230131111209.png]]

Decryption works the same $$\forall k\in \mathcal K.\forall c\in \mathcal C. D(k,c)=k\oplus c$$

This is a better schemes as any sequence of messages could come from any other sequence. We could construct and arbitrary key to give any ciphertext out.

## Perfect Secrecy
![[Pasted image 20230131111242.png]]

The difference in probability two messages of the same length gives the same ciphertext is negligible. So all messages have over all keys the same chance of given any ciphertext.

### OPT Perfect Secrecy
![[Pasted image 20230131111300.png]]
![[Pasted image 20230131111319.png]]

The problem here is you can only use a given key **once**. If we reuse keys we can extract some information about the original messages form the two cipher texts.

![[Pasted image 20230131111354.png]]

This comes from $k\oplus k=0$. Many secret agencies use OTPs and **reuse them!**



### Limitations of OTP
**Key-Length** - the key should be as long as the plaintext. So to encrypt a hard drive we need a harddrive worth of OTP. Getting true randomness (the key should not be guessable from an attacker). If the key is not truly random, frequency analysis might again be possible. Perfect secrecy does not capture all possible attacks. So they are secure to regular decryption but are insecure to two-time pad attacks. Given $m_1\oplus k$ and $m_2\oplus k$ we can get $m_1\oplus m_2$.

**OTP is Malleable** - If we know some section of the message, if we know the stat is say "To Bob" we can add anther "To Bob" and add in a new chosen text like "To Eve". So we can mess with parts of a message.

**Perfect Security Doesn't Capture all possible attacks**

## Key Management
We make the algorithms public so now all the secrecy is in the keys. So we must understand how they keys are generated, how the keys are stopped and where are the keys actually used (generated, stored, used, replaced).

[[Cryptography Introduction Questions]]