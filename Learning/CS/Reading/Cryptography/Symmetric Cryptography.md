Cryptography encompasses many areas and in general started concerned with how we transmit messages without an eavesdropping party reading them. But not it includes many more fields such as **digital signing** and **authentication**.

**AES** (Advanced Encryption Standard) is the standard in symmetric encryption today and replaced **DES** (Data Encryption Standard). These are known as *cryptosystems* and we will cover some simpler ones before stepping up to AES.

## Attacks
The science of attacking cryptosystems is called **cryptanalysis** and is performed by cryptanalysts. The cryptanalyst will know the algorithm used (which they are attacking) but they will not know which key is used with the algorithm. This assumes use of the **open design principle** as apposed to *security through obscurity* which is likely to fail for many reasons. a) Documents with sensitive info can get leaked, b) Reverse Engineering can be used.

There are **four types of cryptanalyst attacks** that can take place.

1) **Cyphertext-only attack** - Here an attacker know the cyphertext for some messages encrypted with the same key, they hope to gain the plaintext messages that were encrypted or determine the key $K$.
2) **Know-plaintext attack** - Here an attacker knows some cyphertext-plaintext pairs where each plaintext was encrypted with the same key $K$. They hope to determine $K$.
3) **Chosen-plaintext attack** - Here an attacker can choose one or more plaintexts and get the corresponding cyphertext associated with them. In the **offline chosen-plaintext attack** they must chose the messages in advance while in **adaptive chosen-plaintext** attack they can chosen interactively with access to the resulting cyphertext in between.
4) **Chosen-ciphertext attack** - Here the attacker can choose one or more ciphertext messages and get the plaintext that is associated with each one. (again with offline and adaptive versions)

Attacks are more feasible since plaintext messages have a very different form to wrongly encrypted messages. So we can detect when a message has been decrypted properly without knowing the true plaintext.

## Substitution Ciphers
One of the most basic ciphers it the **Caesar Cipher** where we shift all Latin letters along in the alphabet under modulo arithmetic so "z" wraps back around to "a". A better system is a **substitution cipher** where we simply apply an arbitrary substitution or (permutation) on the alphabet (there are $26!=4.03*10^{26}$).

However despite the large key size these ciphers are easy to break. This comes from the letter frequency in English. We can make a fairly sure guess from the frequency along (given we are decrypting plaintext), then we can fill in the rest with word guessing.

![[Pasted image 20230428143217.png]]

#### Polygraphic Substitution Ciphers and Substitution Boxes
In **Polygraphic Substitution Ciphers** we group together block of characters and treat them as characters to be decrypted together. One way of representing this is with a two dimensional table, one row specifies some part of the original message and the other part specifies the other. This is called a **substitution box** or **S-Box**.

![[Pasted image 20230428143812.png]]

We can reverse this by looking for some message in the **S-Box** then replacing it with the labels for its row and column.

## One-Time Pads
Another type of polygraphic substitution cipher is the **Vigenère cipher** which encrypts blocks of length $m$, by basically using $m$ shift ciphers in parallel each with a different shift value $k_1\dots k_m$. But this can be broken easily with statistical techniques.

The **one-time pad** is a different approach where we use a block of keys $(k_1,\dots k_m)$ for a message the same length as $n$ and with very $k_i$ value chosen at random. With this change there is not statistical analysis that can be done as each character is substituted for a different random character. But it can still be reversed if we know which switches were made.

If the pads are unknown there is no way to decipher this as any sequence of character of the same length could be encrypted into the same ciphertext with some different key.

When the pads are reused statistical methods are enabled and the security is reduced. Another problem is the *pad length has to be as long as the message*.

#### Binary One-Time Pads
A OTP can be used for binary numbers. In this case we have two characters and so perform operations modulo 2. But this is the same as XOR in binary since $1\oplus 1=0$, $1\oplus 0=1$, $0\oplus 1=1$ and $0\oplus 0=0$. So we will have a message $M$, and then a pad $P$. To encrypt we perform $$C=M\oplus P$$Then since taking away is the same ass adding for mod 2 we can perform $$M=C\oplus P=(M\oplus P)\oplus P=M\oplus(P\oplus P)=M\oplus\vec{\mathbf 0}=M$$
## Pseudo-Random Number Generators
Getting truly random numbers into a computer is hard since they are build to be deterministic. Once we have these random seeds we want to expand them to any size we want. For this a **pseudo-random number generator (PRNG)** is used which approximates the properties of a random sequence.

#### The Linear Congruential Generator
This is a random number generator where we start with a random number $x_0$ called the **seed** then we generate a sequence of number following the formula. $$x_{i+1}=(ax_i+b)\mod n$$Where $a>0$, $b\ge 0$. If $a$ and $n$ are relatively prime then the generated sequence is **uniformly distributed**. This can be used to generate uniformly distributed numbers with a prime $n$, but this isn't sufficient for cryptographic purposes.

#### Security Properties of PRNGs
For cryptographic applications we **don't want to be able to predict the next key**. Bot with *linear congruential generators* we can determine $a$ and $b$ with three consecutive numbers and then predict from then on. Another property is the **period** where we come back to $x_0$ the whole sequence will start to be generated again. Even if the mechanics behind it aren't know we can still predict the values this way.

#### A More Secure PRNG
One way to make a PRNG more secure is to encrypt each number in a deterministic sequence with a block cipher like DES. Breaking this encryption comes down to a ciphertext only attack. The period will be $2^n$ where $n$ is the block size.

A **prng** can be sued to create a OTP (from a key) that is XORed against our message to encrypt it. Then with the same key XORed again to decrypt. We should still not use this key twice otherwise a two-time attack could be launched. This is called a **stream cipher**.

## The Advanced Encryption Standard (AES)
AES is a **block cipher** that operates on 128-bit blocks. There are 128, 196 and 256 key versions giving *AES-128, AES-196* and *AES-256*.

![[Pasted image 20230428152051.png]]

#### AES Rounds
The AES-128 proceeds in ten rounds. Each round performs an *invertible transformation* on a 128-bit array called the **state**. The initial state $X_0$ is the XOR of the plaintext $P$ and the key $K$. That is $$X_0=P\oplus K$$Then for each round $i$, $X_{i-1}$ is taken as input producing $X_i$. Then the final round produces the *ciphertext* $C$. That is $C=X_{10}$ (in the 128-bit case).

Each round is built from four basic steps:

1) **SubBytes step** - an S-box substitution step.
2) **ShiftRows step** - a permutation on the rows order
3) **MixColumns step** - a matrix multiplication (Hill cipher) step
4) **AddRoundKey step** - an XOR step with a **round key** derived from the 128-bit encryption key.
![[Pasted image 20230428152835.png]]

#### Implementation of AES
AES implementations are optimized for speed of execution and so generally precomputed **look-up** tables are used during encryption and decryption. If the tables take in an 8bit word and output a 32-bit word then AES can be implemented by combining three operations.

- XOR of two ints $y=x_1\oplus x_2$ where $x_1$, $x_2$ and $y$ are ints
- Split of an into into 4 bytes $(y_1,y_2,y_3,y_4)=x$ where $y_1,y_2,y_3$ and $y_4$ are bytes and $x$ is an int.
- Table lookup of an int indexed by a byte: $y=T[x]$, where $y$ is an int and $x$ is a byte.

#### Attacks on AES
**Timing attack** - Since AES is commonly implemented with look-up tables (see above) and recently used pieces of the tables will be stored in the CPU cache. Now this takes less time to access and so the time the CPU takes to encrypt blocks can give information about the inner workings of the algorithm.

On the same machine this can take less that a second to break the key, while on over a network this can take several hours. To defend against this **execution time should be kept constant**.

## Modes of Operation
There are different ways to use a **block cipher** there are known as its **modes of operation**. In general we have a sequence of blocks $B_1,B_2\dots$ and we want to encrypt them with the same key $K$ with an algorithm like AES.

#### Electronic Codebook (ECB) Mode
The simples mode is to encrypt each block the same. That is for a block cipher with encryption function $E_k$ and decryption function $D_k$ for a key $k$. We encrypt and decrypt with $$C_i=E_k(B_i)\hspace{8pt}\text{ and }\hspace{8pt}B_i=D_k(C_i)$$respectively. The benefit of this is that each block is encrypted and decrypted independently and so if we loose a block we can still decrypt everything.

The **disadvantage** is this approach is deterministic on the block and so the same block will always give the same output allowing for some frequency analysis exploits.

#### Cipher-Block Chaining (CBC) Mode
This avoid revealing patters as ECB mode does. Basically each block $B_i$ ($B_1\dots$) is XORed with some value, at first an *initialization vector* and then every time after the *ciphertext of the previous block* before being **encrypted**. That is with the initialization vector $C_0$ we get $$C_i=E_k(B_i\oplus C_{i-1})\hspace{16pt}B_i=D_k(C_i)\oplus C_{i-1}$$Each block is XORed with some random value which is hard to predict. And therefore the same block almost certainly has a different encryption.

A **disadvantage** is encryption cannot be done in parallel since each ciphertext depends on the previous ciphertext. On the other hand *decryption* can be done in parallel since it is still the ciphertexts that are XORed against the result of the decryption and since we have them all decryption can be done smoothly.

#### Cipher Feedback (CFB) Mode
This mode relies on the previous cipher text (or initialization vector) to make a sort of onetime pad when encrypted with $E_k$. This means $D_k$ never has to be used and with $C_0$ being th initialization vector we get $$C_i=E_k(C_{i-1})\oplus B_i\hspace{16pt}B_i=E_k(C_{i-1})\oplus C_i$$This bas basically the same properties as CBC mode but may be baster depending on the algorithm in question since $D_k$ isn't used.

#### Output Feedback (OFB) Mode
This make a OPT in a more literal way than the last sequence. Basically we start with an *initialization vector* $V_0$ and we generate a stream of vectors with $$V_i=E_k(V_{i-1})$$Given this sequence of pad vectors we perform block encryption and decryptions with $$C_i=V_i\oplus B_i\hspace{16pt}B_i=V_i\oplus C_i$$This has the benefit of working in **parallel** *once we have computed the $V_i$ OPT vectors*.

####  Counter (CTR) Mode
In this mode we again generate a sequence of $V_i$ vectors. But this time we apply make them by encrypting some ofset of the random sees $s$. That is $$V_i=E_k(s+i-1)$$so the first pad is the encryption of the key the second pad the encryption of $s+1$ and so on. Then the encryption and decryption are the same as OFB $$C_i=V_i\oplus B_i\hspace{16pt}B_i=V_i\oplus C_i$$The key thing is all encryption and decryption can be done in **parrallel** including generation of the $V_i$ vectors.