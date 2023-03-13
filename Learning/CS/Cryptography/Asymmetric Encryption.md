We have so far reduced the security problem to having a shared secret key. But how would we both get this key?

![[Pasted image 20230206100945.png]]

There are various ways of doing this.

# Trust Third Party (TTP)
Here we have a set of users $U_1...U_m$. Each $U_i$ has a shared secret $K_i$ with TTP. $U_i$ and $U_j$ can establish a key $K_{ij}$ with help of the TTP. $\{m\}_k$ denotes the symmetric encryption of $m$ under the key $k$. An example is **Paulson's variant of the Yahalom protocol**.

![[Pasted image 20230206101213.png]]

At the start both $A$ and $B$ have a key to communicate with the TTP $S$. For this protocol first. $A$ sent a message to $B$, it contains Alices names and $N_A$ (Number that is used ONCE). We use $N_A$ to make the communication unpredictable this stops **replay attacks** where previous messages are captured and reused later.

![[Pasted image 20230206101824.png]]

$B$ doesn't trust this as there is no proof this is $A$. $B$ so sends a message to $S$ saying this is $B$ and a nonce. Then $B$ encrypts $A$ and $N_A$ to $S$ encrypted with $K_{BS}$. With this message since $S$ has a shared key with $B$ the message can be decrypted. $S$ can create the secret key from $A$ to $B$ (unfortunately $S$ needs to know this aswell but its ok as $S$ is a TTP).

![[Pasted image 20230206101933.png]]

$S$ then sends out two messages encrypted with two keys. To $A$ the original NONCE and a new keys along with the name $B$. This tells $A$ what message has been resent. $A$ can then respond with the part of the message $A$ cannot decrypt (proving $A$ got the message from $S$).

![[Pasted image 20230206102159.png]]

$A$ then responds to $B$ with the message encrypted form $S$ along with $B$'s NONCE to prove which message was being responded to. $A$ has $K_{AB}$ and uses this to encrypt this NONCE. $B$ then receives a message from $A$ encrypted with the key from $S$ decrypting this gives the key $K_{AB}$ allowing $N_B$ to be read from the message.

### Why
This works by exploiting the secret keys both share with $S$. This encryption ensures only the needed parties can read the data. The NONCES protect the protocol against replay attacks.

# Public-key Encryption
This allows a secure secret without a trusted thirds party. The way this works is a message is sent from $A$ to $B$ saying a secret message want to be established. The idea is $B$ sends something to $A$ allowing $A$ to create a message only $B$ can read.

![[Pasted image 20230206103015.png]]

### Definition
We have a key generation algorithm $G:\to\mathcal K\times\mathcal K$. Gives two keys. One is called the public key (can be viewed by everyone) and the other is the private key (can't be seen by anyone).  The encryption algorithm $E:\mathcal K\times\mathcal M\to\mathcal C$ which uses the public key. Then decryption $D:\mathcal K\times\mathcal C\to\mathcal M$ uses the private key.

![[Pasted image 20230206103212.png]]

So there are basically **encryption** and a **decryption** keys.

### Number Theory
![[Pasted image 20230206103321.png]]

Many of these functions are defined by **prime** numbers.

![[Pasted image 20230206103344.png]]

Then $a$ and $b$ in $\mathbb Z$ are **relative primes** if they have no common factors. Then the **Euler phi** function as

![[Pasted image 20230206103449.png]]

The number of co-primes numbers smaller than $n$ and greater than $0$. The **Euler phi** function has the properties that for a prime $p$ $$\phi(p)=p-1$$ and $p$ and $q$ primes $\phi(p\cdot q)=(p-1)(q-1)$.

We can also defined $\mathbb Z_n$ as for $n\in\mathbb N$. We defined $\mathbb Z_n=\{0,\dots n-1\}$. We then say $$\forall a\in\mathbb E,\forall b\in\mathbb Z_n, a=b\mod m\iff\exists k\in\mathbb N. a=b+k\cdot n$$So two numbers are equal if they have the same residual modular $n$. Then in **modular inversion**: the inverse of $x\in\mathbb Z_n$ is $y\in\mathbb Z_n$ s.t. $x\cdot y=1\mod n$. We denote $x^{-1}$ the inverse of $x\mod n$. Not all numbers have inverses in a given mod.

![[Pasted image 20230206104416.png]]

![[Pasted image 20230206104457.png]]

We can also defined $\mathbb Z_n^*$ as let $n\in\mathbb N$. We defined $\mathbb Z_n^*=\{x\in Z_n\mid \text{gcd}(x,n)=1\}$. We defined a group which all have some multiplicative inverse mode $n$. This defines a [[Groups]]. So $$\mathbb Z_{12}=\{1,5,7,11\}$$Then also from the definition of $\phi(n)$ we have $$|\mathbb Z_N^*|=\phi(n)$$

![[Pasted image 20230206104921.png]]

![[Pasted image 20230209100225.png]]

### Intractable problems
Asymmetric encryption's security is conditioned on problems being computationally hard. Although these are only conjectures and there is no proof they are truly this hard to solve. I one of them is proved to be hard equally they will all be.

#### Factoring
With some inputs $n\in \mathbb N$ we want to find the prime numbers $p_1,...,p_n$ such that $n=p_1,...p_m$.

#### RSAP
Here we are given some inputs $n$ such that $n=pq$ with $2\le p,q$ primes. We are given $e$ such that $\text{gcd}(e,\phi(n))=1$. Then $m^e\mod n$ we want to find $m$.

#### Discrete Log
Here we are given some input prime $p$, generator of $\mathbb Z_p^*$, $y\in\mathbb Z_p$ we want to find $x$ such that $y=g^x\mod p$.

#### DHP
Here we are given a prime $p$, generator $g$ of $\mathbb Z_p^*$, $g^a\mod p$, $g^b\mod p$. We want to find $g^{ab}\mod p$.

### How can we establish a key without TTP
The **Diffie-Hellman (DH)** protocol. We assume the DHP is hard in $\mathbb Z_p^*$. We pick some very large prime $p$ , and $g$ generator of $\mathbb Z_p^*$.

![[Pasted image 20230209101140.png]]

Bob then sends $g^b\mod p$ which only he can find since only he knows $b$.

![[Pasted image 20230209101219.png]]

Our assumption means $b$ cannot be found. Then allice does the same

![[Pasted image 20230209101252.png]]

Then both $a$ and $b$ can use this power and their own number to find some shared number.

![[Pasted image 20230209101327.png]]

No one else can find $a$ or $b$ so even though they know $g^a$ and $g^b$ they cannot find $g^{ab}$. This allows two numbers to be sent.

##### Man in the middle attack
This is a good regime but is weak to man in the middle attacks.

![[Pasted image 20230209101454.png]]

Here some attacker generated their own $a$ and $b$ in the middle.

![[Pasted image 20230209101536.png]]

The attacker uses their own $b'$ to communicate with $A$ then uses their $a'$ to communicate with $B$.

![[Pasted image 20230209101619.png]]

Each finds some number (Alice and bob get different numbers) but the attackers can find both these numbers.

![[Pasted image 20230209101716.png]]

## RSA trapdoor permutation
This assumes factorization is hard. This gives us two keys a public key and a private key. We have $pk=(N,e)$ and $sk=(N,d)$ and $N=pq$ with $p,q$ random primes and $e,d\in\mathbb Z$ with $ed=1\mod\phi(n)$ (multiplicative inverses in $\mathbb Z_{\phi(N)}$). Our ciphertext is simply numbers in $\mathcal M=\mathcal C=\mathbb Z_N$. Encryption an decryption will raise a number to the power $e$ or $d$. 

![[Pasted image 20230209102253.png]]

![[Pasted image 20230209102345.png]]

This works assuming we can't find $\phi(N)$, we can't find this as we would need to factorize $N$ to $pq$.

($G_{RSA}$, $RSA$, $RSA^{-1}$) is called raw RSA. Do not use raw RSA directly as an asymmetric cipher. This is as **deterministic** and so is vulnerable to chosen plaintext attacks. It also takes a lot of time hence it is better to perform some more sophisticated attack.

### ISO Standard
Here we build a CPA secure asymmetric cipher using ($G_{RSA}$, $RSA$, $RSA^{-1}$). We let $(E_s, D_s)$ be a symmetric encryption scheme over ($\mathcal M, \mathcal C,\mathcal K$). We let $H:\mathbb Z_N^*\to\mathcal K$, so $H$ generates random keys given some $\mathbb Z_N^*$. We build ($G_{RSA}$, $RSA$, $RSA^{-1}$)  as follows.

![[Pasted image 20230209103007.png]]

We are basically using RSA to pass along small $x$ values which can be used to get the key $k$ which can be decrypted using a block cipher.

#### PKCS1 v2.0: RSA-OAEP
This is the build a CPA secure asymmetric cipher using ($G_{RSA}$, $RSA$, $RSA^{-1}$) 

![[Pasted image 20230209103241.png]]

### ElGamal (EG)
We fix a prime $p$, and generator $g\in\mathbb Z_p^*$. We pick $p$ such that $p-1$ has many prime factors. We pick:

![[Pasted image 20230209103514.png]]

The ciphertext is pairs of numbers in $\mathbb Z_p$.

![[Pasted image 20230209103626.png]]

The number $r$ is chosen randomly. A pair of numbers is then given as

![[Pasted image 20230209103734.png]]

Both these parts depend on $r$ and with $d$ they can cancel our the $r$s from both sides to get the true message text. The public key is intertwined with $g$. Then to decrypt we take

![[Pasted image 20230209104112.png]]

The idea is decrypting with $d$ allows the $r$s in each part of the ciphertext to cancel themselves out. This gives

![[Pasted image 20230209104312.png]]

We know $g^d$ but if we cannot compute logarithms efficiently we cannot find $d$. This is also **non-deterministic** as $r$ is random by default.

This all only works under the **hardness assumption** of reversing the secret key from the public key.

[[Asymmetric Encryption Questions]]