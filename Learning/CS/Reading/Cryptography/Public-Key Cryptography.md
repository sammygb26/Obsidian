 In general data is represented in binary and so cryptosystems work to manipulate these large numbers.

## Modular Arithmetic
We want to make sure after each operation our number doesn't get too large of the number of bits the original number was stored in. We do this by taking the modulo after every potation that is dividing by $n$ and getting the remainder. This means we are working in $Z_n$ $$Z_n=\{0,1,2,\dots,n-1\}$$All operations are essentially the same with the extra modulo step afterwards.

#### Modulo Operator
We say $x\mod n$ as $x$ **modulo** $n$. There are three cases.

1) $0\le x\le n-1$, $x\in Z_n$ then $x\mod n=x$.
2) If $x\ge n$ then we take the remainder dividing by $n$. This will be the same as $x-kn$ for $k=\lfloor\frac xn\rfloor$.
3) If $x<0$ then we add $kn$ with the smallest integer $k$ to make the result positive. The means $k=\lfloor\frac xn\rfloor+1$.

#### Modular Inverses
Its hard to grasp division in $Z_n$ but we can see the idea of an inverse $x^{-1}$, since $a/b=ab^{-1}$. We say $x^{-1}$ is the inverse of $x$ is $xx^{-1}\mod n=1$. Not every number has an inverse but if $n$ is prime all numbers have inverses.

![[Pasted image 20230428164908.png]]

#### Modular Exponentiation
This is the operation $x^y\mod n$. Some successive modular powers can be seen here

![[Pasted image 20230428165127.png]]

The general rule is $x^y\mod n$ will only be $1$ if $gdc(x,n)=1$. If $gdc(x,n)\neq1$ then $x$ and $n$ share some factor greater that 1. We cannot multiply $x$ by anything and be left with 0 of that factor and so $x\mod n$ will always take up some fraction greater than or equal to that fraction.

We can generalize this idea by considering the subset of $Z_n$ that is relatively prime to $n$. That is $$Z_n^*=\{x\in Z_n\text{ such that }GDC(x,n)=1\}$$Then if $Z_n^*$ is prime we have $$Z_n^*=\{1,2,\dots,n-1\}$$Then $\phi(n)$ is called then **totient** of $n$ and is defined as $\phi(n)=|Z_n^*|$. Then **Euler's Theorem** states that for $x\in Z_n^*$ $$x^{\phi(n)}\mod n=1$$This means that we can always reduce the exponent modulo $\phi(n)$, that is $$x^y\mod n=x^{y\mod\phi(n)}\mod n$$

## The RSA Cryptosystem
This is a **public key cryptosystem** which treats the plaintext and ciphertexts as large number and performs modular arithmetic on them.

#### RSA Encryption and Decryption
First we must **generate** the public and private keys. So first we find two large prime numbers $p$ and $q$ and set $n=pq$. Now we pick some number $e$ that is relatively prime to $\phi(n)=(p-1)(q-1)$ then we calculate $d=e^{-1}\mod \phi(n)$ and then we *throw away* $p$,$q$ and $\phi(n)$. We now have 

- **Public Key** : $(n,e)$
- **Private Key** : $d$

Now encryption takes a number $M$ and compute $$C=M^e\mod n$$To decrypt the ciphertext, $C$ we perform $$C^d\mod n=M$$Step by step for the case $M$ is relatively prime to $n$ we get

![[Pasted image 20230428172443.png]]

Alternatively if $M$ is not relatively prime to $n$ then it must be relatively prime to $p$ or $q$ since $M\le n$. So when $M=ip$ (with reflected argument if $M=iq$) we know $$M^{\phi(n)}\mod q=1$$Since $\phi(n)=\phi(p)\phi(q)=j\phi(q)$. Similarly $M^{k\phi(n)}=1\mod q=1+hq$. But $k$ can be anything and since $ed=t\phi(n)=t\phi(p)\phi(q)=k\phi(q)+1$. Now $M^{k\phi(n)+1}=M+Mhq$. But $M=ip$ and so $$M^{ed}=M^{k\phi(n)+1}=M+Mhq=M+ihpq=M+ihn\text{ mod } n=M$$Thus RSA is aways correct.

#### The Security of the RSA Cryptosystem
In general we want to determine $d$ given $e$ and $n$ to break RSA. This can be done trivially if we know $\phi(n)$ since $e^{-1}\mod \phi(n)=d$. But to find $\phi(n)$ we need $p$ and $q$ which are kept secret *or destroyed*. Hence we need to factorize $n$ (a very large number made of very large primes). There is no efficient way do do this hence RSA is kept safe.

One issue with pure RSA is its **determinism**. For example if we have two messages $M_1$ and $M_2$ with corresponding ciphers $C_1$ and $C_2$ if $C_1=C_2$ then $M_1=M_2$, this can allow some cryptanalysis revealing values.

## The Elgamal Cryptosystem
This system uses randomization so that independent encryptions of the same plaintext give different ciphertexts. This relies on some more **number theory**. We will do arithmetic in $Z_p$ for some prime $p$. Then $g$ is called a **generator** if $\forall x\in Z_p.\exists k.g^k=x$. There are $\phi(\phi(p))$ generators for $Z_p$ and we can test for them. We can also pick $p$ to make it easier to find $g$s.

Once we have our $g$, we can compute $x=g^k\mod p$ for any value $k$ easily. But given $x$ and $g$ it is **hard** to find $k$. This is known as the **discrete logarithm** problem.

As part of the setup we choose a random large prime $p$, and find a generator $g$ for $Z_p$. We pick a random number $x$, between $1$ and $p-2$ between $1$ and $p-2$ and we compute $y=g^x\mod p$. Then we have 

- **Public key** : $(p,g,y)$
- **Secret key** : $x$

To encrypt a message $M$, we must generate a random number $k$ between 1 and $p-2$. We then calculate $$a=g^k\mod p\hspace{16pt}b=My^k\mod p$$Then the encrypted message is the pair $(a,b)$. Since this is dependent on the random number $k$. So each time a message is encrypted it will have a different value. Reusing the same random number $k$ would leak information and could allow a possible cryptanalysis attack. The decryption requires we compute $a^x\mod p$ and then compute its inverse. That is $(a^x)^{-1}\mod p$. Then we just multiply $b$ by this. The reason this works is

![[Pasted image 20230428181132.png]]

We don't need to know $k$ to decrypt, in fact we cannot know $k$ as we would have to solve the **discrete logarithm** problem. Similarly this prevents anyone but the secret key owner from knowing $x$ and so decrypting and breaking ElGammel.

#### Key Exchange
Symmetric cryptosystems require the establishment of a **secret key**. This can be one with a **one-time secure channel** like a meaning in person. But a **key exchange protocol** hopes to do this over an *insecure channel* which may have an eavesdropper. This doesn't include a insecure channel with **active tampering** as in fact no no protocol exists.

**Diffie-Hellman key exchange Protocol (DHP)** - This assume that everyone knows some $p$ prime number and $g$ generator of $Z_p$. The DH protocol consists of the steps

1) Alice picks a random positive number $x$ in $Z_p$ and uses it to compute $X=g^x\mod p$. Which she sends to Bob
2) Bob pick a random positive number $y$ in $Z_p$ and uses it to compute $Y=g^y\mod p$. Which he sends to Alice. He can also calculate $X^y=g^{xy}$.
3) Alice calculates $Y^x=g^{xy}$

Now both parties have $g^{xy}$ without either transmitting it between themselves. Neither $g^x$ can be used to find $x$ nor $g^y$ can be used to find $y$ as this would require solving the **discrete logarithm** problem. The **Diffie-Hellman Problem** is the problem of finding $g^{xy}$ given $g^x$, $g^y$, $g$ and $p$ and doesn't have an efficient solution.

This is *secure to a passive attack* but is **vulnerable to a man-in-the-middle attack** since the attacker between can establish secret keys with each individual party acting as the other and then use the two secret keys to decrypt and decrypt messages between.