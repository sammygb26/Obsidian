# Stream Ciphers
We want a version of OPT that is practical (we don't need such large keys). The idea is to use pseudorandom key rather than a really random key. It will look random and it will be generated from the true key. With the generator s $G$. Hence $$G:\{0,1\}^s\to\{0,1\}^n$$with $s << n$.

Encryption and decryption ciphers will be the same will be the same as OTP.

![[Pasted image 20230202100542.png]]

We still have issues with the key being reused as OTP. Then also this schemes is **malleable**.

### RC4
This was the first implementation of a stream cipher implemented by Ron Rivest in 1987. There are two phases:

![[Pasted image 20230202100700.png]]

This was used in HTTPS and WEP. But there are weaknesses. The first bytes due to the way they were generated are biased and not very random. We could drop the first 256 bytes but this is really more of a path. It is also subject to related key attacks were similar keys give similar pads. Hence we can analyze and slowly break encryption.

##### RC4 in WEP
![[Pasted image 20230202100958.png]]

The way this worked is a key was used to encrypt a padded (with initialization vector) message. 

A problem is two-time pad attacks; Since IV is 24bits long, so the key is reused after at most $2^{24}$ frames (could use longer IV). FMS attack (related keys attack) key sonly differ in the 24 bits IV. First bytes of key stream known because standard headers are always sent.  For some IVs knowing $m$ bytes of key and keystream means you can deduce byte $m=1$ of the key. This means IVs should be generated using PRG.

# Modern Stream Ciphers
**Project eStream** Project to identify new stream ciphers suitable for widespread adoption. Organized by the EU ECRYPT network

![[Pasted image 20230202101507.png]]

This security assumes certain computational resources on the attacks part and so haven't been proven 100% secure. But perfect secrecy doesn't capture all attacks (**malleability** etc).

There is in fact a theorem (Shannon 1949) that means a cipher only satisfies perfect secrecy then the keys bust be at least as long as the plaintexts ($|\mathcal M|\le|\mathcal K|$). This means we need a new definition of security.

# Crypto Primitives
The design of crypto primitives is subtle and error prone. We rely on assumptions on computational complexity. It can be very hard to predict all kinds of attacks which could be made. Also it is better to use public crypto primitives as there are many pitfalls in implementing these algorithms. These primitives are secure under a precisely defined threat models. We need to **respect the security assumptions of the crypto primitives**. There are many attacks due to poor implementation of cryptography.

There are many **side channel** attacks. This attack isn't captured by the abstract model of the bits moving. For example measuring timing on a computer *specture*. Noise and heat movements can affect this.

# Block Ciphers
A block cipher with parameters $k$ and $l$ is a pair of deterministic algorithms ($E$, $D$) such that

![[Pasted image 20230202102323.png]]

So we break our message into blocks of size $l$ and encrypt each with our key $k$.

![[Pasted image 20230202102404.png]]

### Data Encryption Standard
This was made in the early 1970s: Horst Feistel designs Lucifer at IBM with $k=128$ and $l=128$. In 1976 NBS adopted DES as a federal standard with $k=56$ and $l=64$. But in 1997 DES was broken by exhaustive search. With only 128 bits enough computing power can break this. In 2001 NIST adopts AES to replace DES with $k=128,192,256$ bits. $l=128$. This is widely deployed in banking (ATM machines) and commerce.

### Attacks on DES
**Exhaustive search**: with a key length of 56 we only need to search $2^{56}$ we can perform this over the whole key space. Nowadays this can be done with a few FPGAs in a few days.

**Linear cryptanalysis**: found affine approximation to DES. This means can find 14 key bits in time $2^{42}$. This is done by approximating what the key could be line. Then brute force the remaining 56-14=42. So takes again time $2^{42}$. This is a fundamental weakness in DES.

*This means DES is badly broken! So we should not use this*

### Triple DES (3DES)
Goal: build on top of DES a block cipher resistant against exhaustive search attacks. This simply applies DES three times one time after the other. This is used in RFID chips.

For 3DES we pick three keys and we encrypt keys 3 times with regular DES.

![[Pasted image 20230202103220.png]]

![[Pasted image 20230202103254.png]]

Note: Decryption is used in the middle of 3DES. This is a hack to sure keys are different. Hence this allows certain standard to be met. For example then $K_1$ could be the same as $K_3$. But this is *deprecated* an insecure.

A problem with this is it takes 3 times as long as DES. This gives a key size of $3\times 56=168$ bits. This isn't 3 times as secure. We can use a **meet-in-the-middle** attack in time $2^{118}$ (not 112 due to lookup time).

### 2DES
We will use this to explain **meet-in-the-middle**.

![[Pasted image 20230202103519.png]]

We know all the messages are encrypted in the same order with respect the keys.

![[Pasted image 20230202103639.png]]

If we have a **plain-text** attack. We can iterate through the keys for $k_1$ and $k_2$ individually. Then we check if we have the same message in the middle. If we can do this efficiently (ADS) we can reduce the amount of time to decrypt ADS as possible. In this case the key space is only doubled in search time instead of squared.

![[Pasted image 20230202104001.png]]

This gives $2^{63}$ instead of $2^{112}$.

A similar attack can be done for 3DES with two intermediate values we are checking.

# Advanced Encryption Standard (AES)
The goal here is to replace 3DES which is too slow. This was adopted by NIST in 2001. The block size $l=128$ and the key size $k=128,192,256$.

![[Pasted image 20230202104229.png]]

There are many shifting's and mixing affected by the key.

![[Pasted image 20230202104256.png]]

This is better than DES but there have been attacks on it like:

**Related-key attacks** on the 192-bit and 256-bit version of AES exploited the AES key schedule

First **key-recovery attack** on full AES is 4 times faster than exhaustive search.

Existing attacks on AES-128 are still not practical but should use AES-192 or AES-256 in newer projects. As there may be beaks in the future.

This is also vulnerable to quantum computer attacks and this could break encryption in the future.

# Using Block Ciphers

![[Pasted image 20230202104536.png]]

**Bit padding** we append a set bit ('1') at the end of message and then append as many reset bits ('0') requited.

**ANSI X.923** - byte padding pad with zeros the last byte defines the number of padded bytes

**PKCS#7** - byte padding - the value of each added byte is the total number of padded bytes. The padding will be 01, or 02 02 or 03 03 03 or 04 04 04 04, etc.

### Electron Code Book (ECB) mode
This is a block cipher with ($E$, $B$). To encrypt a message $M$ under a key $K$ using ECB mode. $M$ is padded so $M'=M||P$ such that $|M'|=m\times l$. Then $M'$ is broken into $m$ blocks of length $l$. $M'= M_1\parallel M_2\parallel\dots\parallel M_m$. Each block $M_i$ is encrypted under the key $K$ using the block cipher $$C_i=E(K,M_i)\text{ for all }i\in\{1,\dots,m\}$$. The cipher text corresponding  to $M$ is concatenated of the $C_i$s $$C=C_1\parallel C_2\parallel\dots\parallel C_m$$

### Weakness of ECB
![[Pasted image 20230202104826.png]]

A problem with ECB is if any message blocks are the same they will be encrypted the same. This means it will be weak to **frequency analysis**.

![[Pasted image 20230202104848.png]]

### Cipher-block chaining (CBS) mode: encryption
($E$, $D$) is a block cipher that manipulates block size $l$.

![[Pasted image 20230202111642.png]]

$IV$ is chosen at random from block space $\{0,1\}^l$. This basically uses the previously encrypted block message to alter the other blocks. There may be problems if some section of the block is repeated or known in some way between blocks. **Decryption then works as**:

![[Pasted image 20230202111855.png]]


##### Sony PlayStation
The goal was to prevent games from being copied. So CD and full disk encryption was needed. Users were restricted to read and write on dedicated areas of the disk. Games are then loaded in a read only area of the disk. With CBS encryption need to encrypt/decrypt while disk to access game, this was what was used in PS. There was hardware which specifically encrypted / decrypted 

##### Sony PlayStation Attacks
We remove the disk and make a copy. We put the disk back in the PlayStation. Then we copy a file to the disk. Remove disk and find  area of disk that changed (this is the user encrypted file). We then copy the target data to the user area. Then we put the disk back in and ask for the user data. The PS decrypts the file and give it to the user.

### Counter (CTR) mode
Here we start with an initialization vector. We XOR with an increasing sequence of blocks. This makes each block different.

![[Pasted image 20230202105049.png]]

$IV$ chosen at random in $\{0,1\}^l$.

### Block-size is also a problem
Here we attack with block sizes that are too small.

### Key Management Problem
The confidentiality problem is now reduced to key management. We need to decide how and where keys are generated. How they are shared. Where they are stored. Where are they keys used. How are keys revoked and replaced.

![[Pasted image 20230202105219.png]]

[[Symmetric Encryption Questions]]]

