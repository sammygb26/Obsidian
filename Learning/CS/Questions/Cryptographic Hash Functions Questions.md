What is a one-way function? #flashcard #CS #CryptographicHashFunctionsMACs
	A function $f$ is a one-way function if for all $y$ there is no *efficient* algorithm which can compute $x$ such that $f(x)=y$.

---
What is a trivial example of a function that is not a OWF? #flashcard #CS #CryptographicHashFunctionsMACs 
	This would be a constant function. There is only one $y$ and any input we pick will give it. Another example would be the successor function $succ(n)=n+1$.

---
What is an example of a OWF? #flashcard #CS #CryptographicHashFunctionsMACs 
	A classic example is multiplication of large primes. Given two primes $p$ and $q$ we can find $pq$ easily. But given $pq$ is is computationally hard to find $p$ and $q$.

---
What is an important point when it comes to the hardness of factorizing for large primes? #flashcard #CS #CryptographicHashFunctionsMACs 
	Right now it is computationally hard. But this has not been proven and so an algorithm conceivably could exist that would allow you to reverse this with less computational cost. Then quantum computers should be able to do this in **polynomial time**.

---
What does it mean for hash functions to be collision resistant? #flashcard #CS #CryptographicHashFunctionsMACs 
	Hash function are collision resistant is there is no efficient algorithm that can find two messages $m_1$ and $m_2$ such that $f(m_1)=f(m_2)$.

---
What is a trivial example of a function that is not collision resistant? #flashcard #CS #CryptographicHashFunctionsMACs 
	A constant function trivially is not CR as all values has to the same constant value.

---
Why is multiplication of primes CR? #flashcard #CS #CryptographicHashFunctionsMACs 
	Multiplication of primes is CR as all composites have a unique prime factorization.

---
What do cryptographic hash functions do? #flashcard #CS #CryptographicHashFunctionsMACs 
	Cryptographic hash function take a message or arbitrary length and convert it into a fixed size bit string in such a way that a small change to the data will (with a very high probability) change the corresponding hash value completely.

---
What mathematically must a cryptographic hash function have? #flashcard #CS #CryptographicHashFunctionsMACs 
	A CHF $H:\mathcal M\to\mathcal T$ is a function that satisfices 4 properties
	- $|\mathcal M|>>|\mathcal T|$
	- is is easy to compute the hash value for a given message
	- is is hard to retrieve a message from it hashed values OWF
	- it is hard to find two different messages with the same hash value CRF

---
What are some applications of hash functions? #flashcard #CS #CryptographicHashFunctionsMACs 
	**Commitments** (signing some message but not revealing publicly; voting), **file integrity** (can send a hash of a file with a file, if they don't match we know one is incorrect), **password verification** (passwords stored as hashes to avoid leaks), **key derivation** (can derive new keys or passwords from a single secure password), **building block of crypto primitives**.

---
Can collision be avoided with hash functions? #flashcard #CS #CryptographicHashFunctionsMACs 
	No they cannot since the domain will always be much larger than the range by design.

---
What is the birthday attack on hash functions? #flashcard #CS #CryptographicHashFunctionsMACs 
	The idea is it is far easier to find a pair of matching hashes than a hash that matches some specific value. We can square root the time we need to take to find hashes by generating hashes and then just checking if we have generated some similar has before. If we can store the hashes in a computationally tractable way we can perform this attack.

---
What is the Merkle-Damgard hash function construction? #flashcard #CS #CryptographicHashFunctionsMACs 
	Here to hash a function we break it up into $m$ blocks. We then initialize with a IV and each hash for a block is used as the IV for th next block. This construction will be CRF is the hash function used in the construction is CRF.

---
How can a block cipher be turned into a hash function? #flashcard #CS #CryptographicHashFunctionsMACs 
	For any block cipher we can use the output as an IV and then combine this with the next block repeating for the whole function.

---
What are message authentication codes? #flashcard #CS #CryptographicHashFunctionsMACs 
	Message authentication codes are tags that can be send along with messages once the message is received they can be checked against the message to ensure it unchanged.

---
What kind of attack can MACs avoid? #flashcard #CS #CryptographicHashFunctionsMACs 
	MACs can avoid OTP malleability attacks this is as even if an adversary knows some portion of a message and can change it they cannot know the MAC and therefore cannot update it to authenticate the fake message.

---
What is a MAC as an algorithm? #flashcard #CS #CryptographicHashFunctionsMACs 
	A MAC is a pair of algorithms $S$ and $V$ such that $S:\mathcal K\times\mathcal M\to\mathcal T$ and $V:\mathcal K\times\mathcal M\times\mathcal T\to\{T,F\}$ where we can **consistency** and $$V(k,m,S(k,m))=T$$and $F$ otherwise.

---
What does unforgeability mean for a MAC? #flashcard #CS #CryptographicHashFunctionsMACs 
	Unforgeability means it is hard for a computer to find a valid pair $(m, S(k,m))$ without knowing $k$.

---
How can MAC be used for file system protection? #flashcard #CS #CryptographicHashFunctionsMACs 
	The idea is files are kept with a values $t$. Then the key is derives form the user password. Without knowing the password it will be hard to change the files.

---
How can a bloc cipher be used to create a MAC simply? #flashcard #CS #CryptographicHashFunctionsMACs 
	We can simply encrypt the block and then check if the decrypted version is the same as our message. This problem with this is the MACs will have to be as long as the message.

---
What is a useful way to use a block-cipher as a MAC in ECBC-MAC? #flashcard #CS #CryptographicHashFunctionsMACs 
	We can encrypt each block in sequence and XOR the previous block with the next block. In the end we encrypt again with a second key.

---
Why do we encrypt the message with a second key in ECBC-MAC right at the end? #flashcard #CS #CryptographicHashFunctionsMACs 
	This means changing and of the last byte of information has a more abstract effect on the final output. This makes it hard to forge the MAC by messing around with this footer.

---
What is PMAC and why does it make sense? #flashcard #CS #CryptographicHashFunctionsMACs 
	In ECBC-MAC we process all blocks sequentially to hash them. But this can take a lot of time. In PMAC we mutate the key for each of the blocks, encrypt they separately and then perform a big XOR of all blocks at the end. This makes the computation parallelizable and to more time efficient.

---
What is HMAC? #flashcard #CS #CryptographicHashFunctionsMACs 
	HMAC is a MAC function built out of hash functions. We use a fixed IV and publicly known IP and OP padding vectors. We perform Merkle-Damgard hashing for the entire message initialized with a hash of k XOR IP and IV. Then hash this again with k XOR OP and IV kicking of the hashing (performed only for one pre-hashed block).

---
What is the need for authenticated encryption? #flashcard #CS #CryptographicHashFunctionsMACs 
	The problem is many encryption schemes are malleable and chaining a part of the message only changes a limited amount of the cipher.

---
How does authenticated encryption solve the problem of malleability? #flashcard #CS #CryptographicHashFunctionsMACs 
	If we send a MAC along with our encrypted message any change to the message will completely change the mac. This can allow us to provide **confidentiality**, **integrity** and **authenticity**.

---
Why should you always encrypt then-MAC instead of the alternatives? #flashcard #CS #CryptographicHashFunctionsMACs 
	The alternatives are we MAC and Encrypt or MAC-then -encrypt. The first case allows cryptanalysis on the hashed text. The second case means  we need the main decryption key to authenticate. 

---
With an Encrypt-then-MAC authenticated encryption scheme how does encryption and decryption work? #flashcard #CS #CryptographicHashFunctionsMACs 
	In this scheme we always encrypt our messages. Then MAC the cyphertext and send both . To derypts we can MAC the ciphertext and check it against the sent MAC. Then  We can decrypt the ciphertext if it is correct. If not we throw it away.

---
What is AES-GCM? #flashcard #CS #CryptographicHashFunctionsMACs 
	This is Galois Counter mode. We use a Galois field based one-time MAC for authentication. Then **AES** based counter mode for encryption. A one-time MAC is encrypted for many messages. This is widely adopted as it has high performance and is parallelizable.

---
