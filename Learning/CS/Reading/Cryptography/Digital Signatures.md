The key idea with **digital signatures** it to provide *authenticity* by binding the identity of some entity to a message. This is done with a *private key* producing a **signature** for the method. A third party with the *public key* can they compare the the signature for a given document revealing if the entity really did verify said document.

![[Pasted image 20230428213301.png]]

Two important properties are:

- **Nonfungibility** : It should be difficult for an attacker to forge a signature for a message $m$ that hasn't been signed.
- **Nonimmutability** : It should be difficult for an attacker, Eve to take a signature $S$ for a message $M$ and convert the signature to verify a different message $N$.

Given these two properties the scheme also achieves **nonrepudiation** - that it is difficult to claim that one didn't sign a given signature.

## The RSA Signature Scheme
The key thing that makes RSA signature possible is that RSA is a **homomorphic** encryption scheme. This means that the two keys $e$ and $d$ along with $n$ can be used either to encrypt or decrypt a message. So we can use RSA the normal way $C=M^e\mod n$ then $M=C^d\mod n$ but we can also use it in reverse; as we do in *signing*. We make a signature $S$ for a message $M$ as follows $$S=M^d\mod n$$Then to check this signature one only needs to decrypt it with the *public key* and check if it matches the message. $$\text{Is it true that }M=S^e\mod n?$$This achieves **nonfungibility** since making a to make a signature you would have to compute $M^d\mod n$ without knowing $d$, this essentially breaks down to knowing $d$ just as is required to break regular RSA encryption.

**Nonimmutability** isn't assured however since if we have two messages and there signatures as $$S_1=M_1^d\mod n\hspace{16pt}S_2=M_2^d\mod n$$Then we can actually make a new signature as $S_1\cdot S_2$ that would be $$S_1\cdot S_2\mod n=(M_1\cdot M_2)^d\mod n$$and so is the signature for $M_1\cdot M_2$. However this isn't an issue as usually the value is hashed before we sign it. This way to find a message pair whose hash values multiply to give the hash value of the message we are faking a signature for would essentially boil down to  finding a hash collision and so we can trust it security as much as we trust our hash function.

## The Elgamal Signature Scheme
This works quite differently than the standard but it still relies of the difficulty of the **discrete logarithm**. Basically as before we have a large random prime $p$ and a generator of $Z_p$. Then we compute a (secret) random number $x$ from 1 to $p-2$ and computes $y=g^x\mod p$. Then $(y,p,g)$ is published.

To sign a message a **one-time** random number $k$ is used to compute $$a=g^k\mod p\hspace{8pt}\text{ and }\hspace{8pt}b=k^{-1}(M-xa)\mod(p-1)$$The pair $(a,b)$, is Alice's signature on the message $M$. Then checking this boils down to asking $$\text{Is it true that }y^aa^b\bmod p=g^M\bmod p?$$The maths works out as

![[Pasted image 20230428221057.png]]

Basically $k$ is brought up to cancel our the $k$ inherent in the public key as likewise is $-xa$. Since the random number $k$ is used the inverse is also random and so $b$ cannot be distinguished form a random number.

If $k$ is reused then we will have the following produced $$b_1=k^{-1}(M_1-ax)\bmod(p-1)\hspace{8pt}\text{ and }\hspace{8pt}b_2=k^{-1}(M_2-ax)\bmod(p-1)$$with the same $a=g^k\bmod p$ for the two different messages then $$(b_1-b_2)k\bmod(p-1)=(M_1-M_2)\mod(p-1)$$Therefore since both $b_1-b_2$ and $M_1-M_2$ are easily computed $k$ can be found revealing the secret key!

## Using Hash Functions with Digital Signatures
There are many reasons to use hashed values instead of entire messages when signing. 1) It is **computationally easier** to sign say a 256 bit hash than a message that is god knows how long 2) For RSA in particular using the true message would lead to a mutability attack. Using *hashes* in general for signatures reduces the chance of **mutability attacks**.

But now the scheme is only as secure as the hash and the signing scheme as if a **hash collision** can be found $H(M)=H(N)$ then getting a signature for $M$ will allow a message $N$ to be signed.

For this reason the risk of **birthday attacks** are heightened. As an example of this Eve could generate many messages which are agreements $M_1\dots M_k$ to buy Alices car for 1000 at the same time she can make many agreements $N_1\dots N_m$ that agree to buy the car for 10,000. If Eve can find two agreements such that $$H(M_i)=H(N_j)$$then she can propose $M_i$ to Alice, get allice to sign it and then charge the amount in $N_j$ which is also signed.