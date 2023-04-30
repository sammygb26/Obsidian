This seeks to create a compressed representation of a message through a function that is **one-way** and **collision-resistant**.

## Properties and Applications
One of the key properties of **hash-functions** is that they are **one-way**. This means that given some message $M$ it should be *easy* to compute $H(M)$, but given some $x$ is should be *hard* to find some $M$ such that $x=H(M)$.

They must also have **ranges** *much smaller* than their **domains**. That is a hash function $h:\mathcal M\to\mathcal H$ should have $|\mathcal M|<<|\mathcal H|$. We want to provide a lot of **diffusion** so changing any part of the input sequence can change almost any part of the output!

#### Collision Resistance
A hash function, $H$, maps input strings to smaller output strings. There will always be collisions, what matters is how easy they are to find.

A hash function $H$ has **week collision resistance** if, given any message $M$ it is *computationally difficult* to find another message $M'\neq M$ such that $H(M')=H(M)$.

A hash function $H$ has **strong collision resistance** if it is *computationally difficult* to find **any** two distinct message $M_1$ and $M_2$ such that $H(M_1)=H(M_2)$.

#### The Merkle-Damgard Construction
A common type of structure used to make a hash function is a **cryptographic compression function** $C(X,Y)$. This takes in two strings one of length $m$ and one of length $n$. Then it outputs a new string of length $n$. This way we can combine message blocks to alters a state with each block with the final value being our hash value.

That is we start with some *initialization vector* $d_0$ (length $n$). We split out message up into $k$ pieces of length $m$ (padding the last one if its not big enough), $M_1,M_2,\dots M_k$. Then we compute $$d_i=C(d_{i-1},M_i)$$The final $d_k$ value is our hash value.

![[Pasted image 20230428200644.png]]

In the *Merkle-Damgard* hash function construction if an attacker finds an collision $H(M_1)=H(M_2)$ they can make arbitrary collisions $$H(M_1||P)=H(M_2||P)$$ where $'||'$ means string concatenation. For this reason **cryptographic compressors** should have **strong collision resistance**.

## Birthday Attacks
This is a kind of brute force attack which motivates the difference between **weak** and **strong** collision resistance. The basic idea comes from the *birthday paradox* where with 23 people you have a 50-50 change of two people sharing a birthday, then with 60 you have an almost 100% change, but there's 360 days is a year what gives?

The key idea is to think about the number of possible pairs rather than the number of days taken up. If you focus on matching on one day the effect goes away. 

The same thing happens with hash functions where for a $b$ output we will have $2^b$ hash options. Without the birthday attack we would expect the number of hashes we would have to check before expecting to find a collision to be on the order of $2^b$, but instead it is $2^{b/2}$. This isn't for a **single** hash but **any** pair of hashes. Hence this is an attack against **strong collision resistance** but not **weak collision resistance**.

#### Maths!
If we have hashed $i$ hashes and none of them collide then $i$ our of $m=2^b$ hashes are *taken up*, the chance of our next hash not colliding with one if these is $i/m$. So the change of our $i$th hash making a collision is $$p_i=1-\frac{i-1}m$$So the chance of this happening for the $k$th and call previous $i$ hashes is$$P_k=\prod_{i=0}^kp_i=\prod_{i=0}^k\left(1-\frac{i-1}m\right)$$now we can use the approximation $1-x\approx e^{-x}$ to get $$P_k=\prod_{i=1}^ke^{\frac{i-1}m}=\exp\left({-\frac1m\sum_{i=1}^{k-1}}i\right)=\exp\left(-\frac{k(k-1)}{2m}\right)$$Now setting $P_k=\frac12$ and solving for $k$ reveals $k\approx 1.17\sqrt m$ or that we only have to sort on the order of $\sqrt m=\sqrt{2^b}=2^{b/2}$.