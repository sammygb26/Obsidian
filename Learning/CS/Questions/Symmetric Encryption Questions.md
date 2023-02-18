What is the idea behind stream ciphers? #flashcard #CS #SymmetricEncryption 
	Stream ciphers use the key to generate a stream of pseudo random numbers. These can then be used as keys to encrypt and decrypt a message.

---
What is the key generator function for a stream cipher? #flashcard #CS #SymmetricEncryption 
	The key generator for a stream cipher will be $$G:\{0,1\}^s\to \{0,1\}^n$$where $s<<n$.

---
How will the encryption and decryption work in a stream cipher? #flashcard #CS #SymmetricEncryption 
	We can use the steam of keys as a generated OTP. Hence encryption with a PRNG $G$ works as $$E(k,m)=G(k)\oplus m=c$$then decryption will work as $$D(k,c)=G(k)\oplus c=m$$

  ---
What are some downsides of stream ciphers? #flashcard #CS #SymmetricEncryption 
	Stream ciphers are subject to two-time pad attacks and are malleable like OTP.

---
What is RC4? #flashcard #CS #SymmetricEncryption 
	RC4 is a basic stream cipher.

---
How does RC4 work? #flashcard #CS #SymmetricEncryption 
	RC4 first using a key initializes to 2048 bit long stream. This is then uses to encrypt 256 bytes.

---
What is a major problem with a bare implementation of RC4? #flashcard #CS #SymmetricEncryption 
	The fist bytes in RC4 are **biased** and so can give away the key somewhat. To get around this the first 256 bytes are dropped. RC4 is also weak to **related key attacks** where similar keys generate similar outputs hence we can use search to find keys.

---
How does WEP's implementation of RC4 work? #flashcard #CS #SymmetricEncryption 
	WEP has a 24-bit initialization string which is combined with the key and then input into RC4 to generate keys to be used like an OTP. The **IV** allows this method to be used over an over again.

---
What are some problems with RC4 in WEP? #flashcard #CS #SymmetricEncryption 
	WEP only uses 24 buts for the initialization vector. This means the key is reused after at most $2^{24}$ frames. To fix this **longer IVs must be used**

---
How does the Fluhrer, Mantin and Shamir (FMS) related keys attack on WEP work? #flashcard #CS #SymmetricEncryption 
	Here the first bytes of a key stream can be recovered as common headers are used. This gives $m$ bytes. Then due to a weakness in the scheduling of the keys we can recover the $m+1$ byte of the key. This can be solved by using a **PRGN** to generate keys.

---
What is the eStream project? #flashcard #CS #SymmetricEncryption 
 The eStream project is a program to identify new stream ciphers suitable for widespread adoption.

---
What is the trouble with the perfect secrecy definition? #flashcard #CS #SymmetricEncryption 
	**Perfect secrecy** doesn't capture all possible attack and therefore even algorithms that do comply with it work poorly in the real world.

---
What does Shannon's theorem about perfect secrecy say? #flashcard #CS #SymmetricEncryption 
	Shannon's theorem says that for a cipher to satisfy perfect secrecy it must have $|\mathcal M|\le|\mathcal K|$. That is the number of messages must not be greater than the number of keys.

---
What are crypto primitives? #flashcard #CS #SymmetricEncryption 
	Crypto primitives are pre-made implementations of the basic encryption algorithms. They provide a error free implementation that has been checked over.

---
What must we be careful about when using crypto primitives? #flashcard #CS #SymmetricEncryption
	We should be careful to respect the assumptions of the primitives as otherwise we could create poor implementations that aren't secure despite the use of these primitives.

---
What is confusion and diffusion? #flashcard #CS #SymmetricEncryption
	These are properties of encryption schemes. Confusion means changing one part of the key will change many parts of the cyphertext while diffusion means changing one part of the message will change many part of the message. 

---
What are the main differences between a stream cipher and a block cipher? #flashcard #CS #SymmetricEncryption 
	Stream ciphers encrypt a byte at a time where a block cipher encrypt larger sections of a message. Then stream ciphers don't implement and diffusion while block ciphers do. Both implement confusion.

---
What is a block cipher defines as with parameters k and l? #flashcard #CS #SymmetricEncryption 
	We define it as a pair of deterministic algorithms $E$ and $D$ such that $$E:\{0,1\}^k\times\{0,1\}^l\to\{0,1\}^l$$ $$D:\{0,1\}^k\times\{0,1\}^l\to\{0,1\}^l$$here $k$ is the key length and $l$ is the block size.

---
What are some examples of block ciphers (with k and l)? #flashcard #CS #SymmetricEncryption
	3DES: $l=64, k=168$
	AES: $l=128$,$k=128,192,256$

---
What is DES? #flashcard #CS #SymmetricEncryption 
	DES is the **data encryption standard**. It is an old block cipher with $k=56$ and $l=64$ which was eventually broken by exhaustive search.

---
What are two main attacks on DES? #flashcard #CS #SymmetricEncryption
	The two main attacks are **exhaustive search** and **linear cryptanalysis**.

---
Why is exhaustive search a problem for DES? #flashcard #CS #SymmetricEncryption 
	DES only uses a 56 bit key. Therefore it is computationally tractable to brute force find the key with say 120 FPGAs.

---
Why is Linear Cryptanalysis a problem for DES? #flashcard #CS #SymmetricEncryption 
	With linear Cryptanalysis a linear affine approximation of DES is used to find 14 of the key. This reduces the bits that need to be guessed to $2^{43}$.

---
What is 3DES? #flashcard #CS #SymmetricEncryption 
	3DES is an improvement over DES that stacks 3 DES encryptors together with different keys (with the one in the middle reversed).

---
How does 3DES work algorithmically? #flashcard #CS #SymmetricEncryption 
	3DES is 3 DES encrypts stacked together with the middle one flipped that is $$E_{3DES}((k_1,k_2,k_3),M)=E_{DES}(K_1, D_{DES}(K_2,E_{DES}(K_3,M)))$$where $K_1,K_2,K_3$ are all keys for DES.

---
How does 3DES's runtime compare to DES? #flashcard #CS #SymmetricEncryption 
	It is three times as slow.

---
How does a brute force attack on 3DES compare to DES? #flashcard #CS #SymmetricEncryption 
	There are 3-times as many bit so we need to guess 168. But with a meet-in-the-middle attack this can come down to time $2^{118}$.

---
How does a meet in the middle attack work? #flashcard #CS #SymmetricEncryption 
	The idea here is we are trying to break two encryption schemes (or more) used is series. For if we have a matched $m$ and $c$ pair instead of guessing both keys. We use one to decrypt $c$ and one to encrypt   $m$. We can do these in parallel and simple look for a match in the intermediate state.

---
What is AES? #flashcard #CS #SymmetricEncryption 
	This is the **advanced encryption standard**. It is a block cipher with $l=128$ and $k=128,192,256$.

---
How does AES work? #flashcard #CS #SymmetricEncryption 
	Our key is expanded to a number of block keys. Each of these can be combined with 128 bit chucks. Which are split into a 4x4 byte grid. This grid is then substituted, shifted and mixed for each f the block keys. So for 128-bits this happens 10 times.

---
What are some weaknesses of AES? #flashcard #CS #SymmetricEncryption 
	AES is weak to **related key attacks** on the 192 and 256 bit versions. Then it is also vulnerable to a **key-recovery attack**.

---
What recommendations are given for using AES? #flashcard #CS #SymmetricEncryption 
	128-bit version is still safe but it is safer to use 192 and 256 bit versions.

---
What are the options to encrypt blocks that are not of size l? #flashcard #CS #SymmetricEncryption 
	We can use** bit padding** basically filling the message with 0s till the end. Then ANSI X.923 **byte padding** where we pad with 0s and then the last byte says how many pads there were. Finally  PKCS#7 byte padding uses bytes where the value of the byte defines the number of padded bytes of that number. So 01, 02 02, 03 03 03

---
What is Electronic Code Block mode for block ciphers? #flashcard #CS #SymmetricEncryption 
	In ECB mode we simply encrypt encrypt each block of the message in the same way. Then decrypt in the same way.

---
Why is ECB mode for block ciphers weak? #flashcard #CS #SymmetricEncryption 
	ECB mode has no protection against frequency analysis and the same algorithm is used for every block giving many examples of the algorithm working.

---
What is cipher block chaining for block ciphers? #flashcard #CS #SymmetricEncryption 
	Here we use the output encryption of one block XORed with the next block. This means all blocks values are intertwined and each is hard to decrypt.

---
What is a problem with CBC mode for block ciphers? #flashcard #CS #SymmetricEncryption 
	This must run each block in series so can be slow for large amounts of data.

---
How was the encryption of PS2 disk broken? #flashcard #CS #SymmetricEncryption 
	In the PS2 the disks had two parts a user section which could be requested and a hidden section. The PS2 could decrypt this hidden section. The issues is that the user section is encrypted with the same key. so the user could copy hidden files to their section and then request its decryption.

---
What is CTR counter mode for block ciphers? #flashcard #CS #SymmetricEncryption 
	Here an initialization vector is combined with the key at each step. The key doesn't remain the same as we increment the IV for each block hence frequency analysis is not possible.

---
