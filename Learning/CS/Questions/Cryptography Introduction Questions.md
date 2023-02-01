What is cryptography? #flashcard #CS #CryptographyIntroduction
	Cryptography is the scientific study of techniques for securing (against internal or external attacks) digital information, transactions, and distributed computations. But it does **not solve all security problems**!

---
What is symmetric encryption? #flashcard #CS #CryptographyIntroduction 
	In **symmetric encryption** both parties have some secret key $k$. There is an encryption and decryption algorithm that takes some message to a cypher and back again. Somehow both parties bust get the key in order to decrypt the message.

---
What is symmetric encryption mathematically? #flashcard #CS #CryptographyIntroduction 
	Mathematical we have $E:\mathcal K\times \mathcal M\to\mathcal C$ as our encryption algorithm. Then we have our decryption algorithm $D:\mathcal K\times\mathcal C\to\mathcal M$. Here $\mathcal M$ is the message space, $\mathcal C$ the cypher space and $\mathcal K$ the key-space.

---
What is Kerckhoff's principle? #flashcard #CS #CryptographyIntroduction 
	This says that we shouldn't use **security through obscurity** any encryption and decryption techniques should be made public as this makes them more secure by having more eyes verifying them.

---
What assumptions do we need to make to tell if a cryptographic scheme is secure? #flashcard #CS #CryptographyIntroduction 
	We have to assume the capabilities of the attacker. For example RSA is secure against attacks from regular computer but may be vulnerable to quantum computer attacks. Our scheme will be vulnerable  to some kinds of attacks and not others.

---
What are the four kinds of attacker capabilities in general we may expect? #flashcard #CS #CryptographyIntroduction 
	**Cypher text only** (attacker only has access to encrypted messages), **Known plaintext attack** (some or all of some encrypted messages is known by the attacker), **chosen plane text attack** (attacker has a way to encrypt messages he wants), **chosen cyphertext attack** (has access to a decryption oracle), **computational resources** (unlimited, polynomial or realistic).

---
What is a brute force attack on encryption? #flashcard #CS #CryptographyIntroduction 
	This is just trying every possible key combination until a decrypted message is found.

---
How does a substitution cypher work? #flashcard #CS #CryptographyIntroduction 
	A substitution cypher is simply a permutation on the set of characters. So it maps each character to some different character. Its inverse gives the decryption algorithm.

---
How can a substitution cypher be broken? #flashcard #CS #CryptographyIntroduction 
	A substitution cypher can be easily broken as the permutation doesn't change letter frequencies or simple word shapes. So to decrypt it we can whittle down the many of the mappings. Then use word completion to get a good permutation.

---
How does a OTP work mathematically? #flashcard #CS #CryptographyIntroduction
	In an OTP we have $\mathcal M=\mathcal C=\mathcal K=\{0,1\}^n$ that is the message, cypher and key are all of the same length and are binary sequences. To encrypt and decrypt we simply perform and XOR with the key.

---
Why is OTP secure? #flashcard #CS #CryptographyIntroduction 
	The key things is any cypher or message can with some key be decrypted into another other message or sequence. This means we cannot analyze the message to gleam the key.

---
What is the definition of perfect secrecy? #flashcard #CS #CryptographyIntroduction 
	A cipher ($E,D$) over ($\mathcal M,\mathcal C,\mathcal K)$ stratified perfect secrecy if for all messages $m_1,m_2\in\mathcal M$ of same length ($|m_1|=|m_2|$), and all ciphertexts $c\in\mathcal C$ $$|P(E(k,m_1)=c)-P(E(k,m_2)=c)|\le\epsilon$$where $k\gets^r\mathcal K$ and $\epsilon$ is some "negligible quantity". This means the message only changes the probability of leading to some cypher texts negligibly.

---
Why does OTP have perfect secrecy? #flashcard #CS #CryptographyIntroduction 
	For any message  and cyphertext there is only one key. Hence each have the same probability of giving $c$ for any $m$. Hence the difference is trivially 0.

---
What problem can arise if an  OTP key is used more than once? #flashcard #CS #CryptographyIntroduction 
	If an OTP is used more than once then we will have for the same key $m_1\oplus k$ and $m_2\oplus k$. Then we can construct $(m_1\oplus k)\oplus(m_2\oplus k)=m_1\oplus m_2$. Which depending on the message and its known parts can be used to reverse the other message.

---
What is a major limitation on OTP in terms of size? #flashcard #CS #CryptographyIntroduction 
	To encrypt a message of length $n$ we need a key of length $n$. Hence to encrypt a hard drive we need another hard drive just for the key!

---
What problem occurs if an attacker know some message sequence with OTP? #flashcard #CS #CryptographyIntroduction 
	If an attacker knows some message sequence for an OTP encrypted message then they can work out the part of the key corresponding to that sequence. This allows them to replace that part of the message with whatever they would like. This means this encryption scheme is malleable.

---
What problem can arise when it comes to key generation? #flashcard #CS #CryptographyIntroduction 
	We must ensure key generation is truly random otherwise attackers may be able to spot patterns, predict keys and break encryption.

---