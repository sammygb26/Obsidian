Encryption we want to give **confidentiality** against interception. We also want **authenticity** which is how we can prove a message came form one user.

### One Way function 
A **OWF** is a function that is easy to compute but hard to invert.

![[Pasted image 20230203100414.png]]

That is $f$ is hard to invert. This makes it hard to compute $x$ only given $y$. When we say efficient we want the algorithm to be non-polynomial or just taking a huge amount of computation to compute.

Since a OWF $f(x)=c$ for a constant $c$ is very easy to invert it is not a OWF. The successor function $succ(n)=n+1$ in $\mathbb N$ is also not a OWF. One example of a OWF (even though no one-way function as rigorously been proven) is **multiplication of large primes**. Integer factorization is a hard problem given $p\times q$ where $p$ and $q$ are primes. This is since it is easy to compute the multiplication but take much effort to find the primes.

- No efficient algorithm is know for this. However there is a proof in quantum computing that would allow a quantum computer solve this problem in polynomial time. Hence with a powerful quantum computer this could be done.

### Collision-resistant functions
A function is CRF if it is hard to find two messages that get mapped to the same value through the function (collision).

![[Pasted image 20230203101033.png]]

Constant function are of course not collision resistant as for all $m_1$ and $m_2$, $f(m_1)=f(m_2)$. The successor function in $\mathbb N$ is CRF the predecessor of a positive number is unique hence this is CRF. We often have a function range smaller than the domain. Hence why the definition includes a computational element.

- Multiplication of primes is CRF since all composite numbers have a unique prime factorization.

There is another similar concept to **hash collisions** called a **second-pre-image attack**. Here instead of finding two values with the same hash the attacker find a hash that matches a given value. We are searching for a single value rather than a match. This means the *birthday paradox* doesn't come into play and so **second-preimage** attacks are must harder. For this reason **second-preimage** resistance is also called *weak-collision resistance* as its a harder problem to attack by default and so the defence property is weaker.

# Cryptographic Hash Functions
A cryptographic hash function takes messages of arbitrary length and return a fixed-size bit string such that any change to the data will (with very high probability) change the corresponding hash value.

![[Pasted image 20230203101355.png]]

We want to not be able to retrieve any message form its hash value. Otherwise anyone could reverse the hash (OWF). We want CRF as we want to be sure that attackers can't fabricate some other matching under hash value.

![[Pasted image 20230203101602.png]]

### Application
**Commitments** - Allows a participant to commit to a value $v$ by publishing the hash $H(v)$ of this value, be revealing $v$ only to the latter. This is done in electronic voting protocols and digital signatures. There will be other values with the same hash value but it will be hard to find meaningful values with the same hash. 

**File Integrity** - This is also use for file integrity to ensure a download is authenticated. We hash a file once we got it and check against a reference hash. If they don't match we know one is incorrect.

**Password verification** - We don't store passwords in clear text as then if there was a leak they could be used elsewhere. If we store only the hash value we just hash passwords every time we want to login.

**Key derivation** - Derive new keys or passwords from a single secure key or password.

**Building block of other crypto primitives** - Used to build MACs, block cipher, PRG

### Collisions are Unavoidable
![[Pasted image 20230203102034.png]]

Domain is much larger than the range, collisions **always** exist.

### The Birthday Attack
![[Pasted image 20230203102112.png]]

We can prove this has a higher probability of succeeding.

![[Pasted image 20230203102250.png]]

The underlying combinatorial mathematic comes down to the birthday paradox. We only need $\sqrt n$ random variable from a size of domain $n$ to ensure some match it likely.  It is the different between the change a person has a matching birthday with you and just that two people have the same birthday.

### The Merkle-Damgard Construction
This is a hash-function construction. We divide our message into $m$ blocks of a fixed size. We apply our hash function block by block and use the output of the previous block as the input to the hash for the next block.

![[Pasted image 20230203102635.png]]

This is defined by a compression function $h:\mathcal T\times \mathcal X\to \mathcal T$.

![[Pasted image 20230203102723.png]]

Some examples of this are MD%, SHA-1, SHA-2 ...

### Compression Functions from Block Ciphers
Let $E:\mathcal K\times \{0,1\}^n\to\{0,1\}^n$ be a block cipher.

![[Pasted image 20230203102917.png]]

We can chain these block ciphers together to fold together all blocks into a single small block. We get an output just as a block length instead of a encrypted message.

### SHA-256
This is a Merkle-Damgard type function. We use a compression function (Davies-Meyer). Then we have a clock cipher as SHACAL-2.

![[Pasted image 20230203103101.png]]

# Message Authentication Codes (MACs)
If we want to send a secure message say to a bank. We may send a encrypted message to a bank encrypted under a message $K_E$.

![[Pasted image 20230203103211.png]]

If $E$ is the OTP. This could be used by an attacker. As OTP is used the key may be reused and so an attacker could change the message to transfer money to another account.

![[Pasted image 20230203103359.png]]

We want **message integrity**.

![[Pasted image 20230203103419.png]]

A MAC is a pair of algorithms $S$ and $V$ defines over $\mathcal K,\mathcal M,\mathcal T$ with

![[Pasted image 20230203103456.png]]

That is the sender uses the key to give a verification of th message. We want to to be hard to **forge** a pair of message and signature without knowing the key.

![[Pasted image 20230203103617.png]]

### File System Protection
At installation time many files are signed.

![[Pasted image 20230203103646.png]]

Allowing us to verify files are not tampered.

## Block Ciphers and Message Integrity
If ($E$,$D$) s a block cipher. We build a MAC ($S$,$V$) using ($E$,$D$) as follows

![[Pasted image 20230203103755.png]]

The problem with this is we need 128bit key to verify a 128bit message. To get around this we can chain blocks together \/

#### ECBC-MAC
This can be combined with the block chaining method to verify larger messages.

![[Pasted image 20230203103849.png]]

At the end we encrypt again with a second key. For example we could remove prefixes or manipulate them to change the MAC. So this makes the scheme vulnerable to forgeries. A problem here is the sequentially (leading to the forgery problem above).

#### PMAC
![[Pasted image 20230203104136.png]]

Here $K_2$ is used to scramble the blocks in a predictable way. This can then all be passed through an XOR in the end. These are all independent of each other and so can be done *in parallel*.

#### HMAC
MAC build form cryptographic hash functions.

![[Pasted image 20230203104357.png]]

IP, OP: are publicly known padding constants.

![[Pasted image 20230203104335.png]]


# Authenticated Encryption
**Plain encryption is malleable** - The decryption algorithm never fails. Changing one bit of the $i$th block of a cipher text. Chaining one bit of the $i$th block of the cipher text

![[Pasted image 20230203104533.png]]

### Encrypt-then-MAC
1. Always compute the MACs on ciphertext, never on the plaintext
2. Use two different keys one for encryption and one for the MAC

![[Pasted image 20230203104631.png]]

This basically put up a wall in the way of message modification. We don't know what we could change as we don't know what affect this is having on the decrypted message. Not to mention finding some key that is verified.

##### Failure Cases
![[Pasted image 20230203104905.png]]

**The first case** allow crypto-analysis as the has may reveal information about the plain message. This also break down the authentication of the sent message and it could have been changed.

**The second case** means we need the main decryption key in order to decrypt.

### AES-GCM
![[Pasted image 20230203105143.png]]

The **trick**: One-time MAC is encrypted to secure for many messages. This is widely adopted for it performance is it is parallelizable.

[[Cryptographic Hash Functions Questions]]