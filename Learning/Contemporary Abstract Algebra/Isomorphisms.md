This comes as a definition for two groups really being the same, sharing the same structure within. Like how $D_3$ and $S_3$ are really the same group.

![[Pasted image 20230127175041.png]]

This definition means the operation table for $G$ can be found by taking the operations table for $\bar G$ and substituting all functions $a$ for $\phi(a)$. **The groups differ in notation only**. This does not take into account the notation of the group operation.

![[Pasted image 20230127175358.png]]

#### Steps to Prove an Isomorphism
1. **Mapping**: Define a candidate for the isomorphism; a function $\phi$ from $G$ to $\bar G$.
2. **One-to-one** - prove That $\phi$ is one-to-one. Assume $\phi(a)=\phi(b)$ and prove $a=b$.
3. **Onto**: Prove that $\phi$ is onto; that is, for any element $\bar g$ in $\bar G$, find an element $g$ in $G$ such that $\phi(g)=\bar g$.
4. **OP**: Prove that $\phi$ is operation-preserving, show that $\phi(a)\phi(b)=\phi(a)\phi(b)$ for all $a$ and $b$ in $G$.

##### Examples
If $G$ I the real numbers under addition then we let $\bar G$ be the positive real numbers under multiplication. Then $G$ and $\bar G$ are isomorphic under the mapping $\phi(x)=2^x$. We can prove $\phi$ is onto and one-to-one. Then we note that $$\phi(x+y)=2^{x+y}=2^x\cdot2^y=\phi(x)\phi(y)$$for all $x$ and $y$ in $G$. So $\phi$ is operation-preserving.

A negative example is that there is no isomorphism from $Q$, the group of rational numbers under addition, to $Q^\star$, the group of nonzero rational numbers under multiplication. If $\phi$ were such a mapping then there would be a rational number such that $\phi(a)=-1$ but this actually contradicts OP. $$-1=\phi(a)=\phi(\frac12a+\frac12a)=\phi(\frac12a)\phi(\frac12a)=[\phi(\frac12a)]^2$$But no squared number is $-1$ hence there is a contradiction.

# Cayley's Theorem
![[Pasted image 20230201101945.png]]

This comes from noting that if we pick any element of $g$ the function $T_g(x)=gx$ (specifically this gives the **left regular representation of $G$**) is a permutation on $G$. So we take the mapping to by $\phi(x)=T_x$. From the associativity of $G$ we can find $T_gT_h=T_{gh}$. This implies that the identity is $T_e$ and $(T_g)^{-1}=T_{g^{-1}}$. Composition itself is associative and so $\bar G=\{T_g\mid g\in G\}$ is  a group. Now it is simple to prove this is isomorphic under $\phi$.

We can write $D_4$ in disjoint cycle form as

![[Pasted image 20230201102021.png]]

# Properties of Isomorphisms
We will now give a catalog of properties of isomorphisms and isomorphic groups.

#### 6.2 Properties of Isomorphisms Acting on Elements
![[Pasted image 20230201102103.png]]

#### 6.3 Properties of Isomorphisms Acting on Groups
![[Pasted image 20230201102130.png]]

These theorems give convenient ways to prove that groups $G$ and $\bar G$ are not isomorphic.

1. Observe $|G|\neq|\bar G|$
2. Observe that $G$ or $\bar G$ is cyclic and the other is not
3. Observe that $G$ and $\bar G$ is Abelian and the other is not
4. Show that largest order of any element in $G$ is not the same as the largest order of any element in $\bar G$.
5. Show that the number of elements of some specific order in $G$ is not the same as the number of elements of that order in $\bar G$.

The **isomorphism** identity is structured such than any group theoretic theorem applying to one applies to the other.

# Automorphisms
![[Pasted image 20230201102155.png]]

For example in $C$ under addition the group isomorphism $\phi(a+bi)=a-bi$ is an **automorphism**. A more specific type of automorphism is

![[Pasted image 20230201102215.png]]

For a group $G$, we use $\text{Aut}(G)$ to denote the set of all automorphisms of $G$ and $\text{Inn}(G)$ to denote the set of all inner automorphisms of $G$.

#### 6.4 Aut(G) and Inn(G) Are Groups

![[Pasted image 20230201102302.png]]

Determining $\text{Inn}(G)$ is routine. If $G=\{e,a,b,c,...\}$, then $\text{Inn}(G)=\{\phi_e,\phi_a,\phi_b,\phi_c,...\}$. This latter list may have duplications however the the only work is deciding which distinct element give the distinct automorphisms. Determining $\text{Inn}$ unlike $\text{Aut}$ is not very involved therefore. But determining $\text{Aut}$ is. 

##### Aut$(Z_{10})$
If we want to compute $\text{Aun}(Z_{10})$, we try to discover enough information about an element of $\text{Aut}(Z_{10})$ to determine how $\alpha$ must be defined. This is simple for small groups like $Z_{10}$. To start we observe that once we know $\alpha(1)$ we know $\alpha(k)$, because 

![[Pasted image 20230201102403.png]]

We need only determine the choices for $\alpha(1)$ that make $\alpha$ an automorphism of $Z_{10}$. Since we need this set to have the same order as $Z_{10}$ that is 10. Hence we can pick

![[Pasted image 20230201102420.png]]

From now on these possibilities will be referred to as $\alpha_1,\alpha_3,\alpha_7$ and $\alpha_9$ respectively. We can they verify individually that these are true automorphisms. An we can even extract the corresponding Caley table.

![[Pasted image 20230201102437.png]]

#### 6.5  $\text{Aut}(Z_n)\approx U(n)$ 
![[Pasted image 20230201102916.png]]

Any automorphism $\alpha$ is determined by the value of $\alpha(1)$, and $\alpha(1)\in U(n)$. Now consider the correspondence between the two. We will take $T:\alpha\to\alpha(1)$. The fact that $\alpha(k)=k\alpha(1)$ means that $T$ is a one-to-one mapping. So for any $\alpha$ and $\beta$ in $\text{Aut}(Z_{10})$ with $\alpha(1)=\beta(1)$, then $\alpha(k)=k\alpha(1)=k\beta(1)=\beta(k)$. Hence $\alpha=\beta$. We also know $T$ is onto $U(n)$ as if we consider some $r\in U(n)$ then mapping $\alpha(s)=sr(\mod n)$ is an **automorphism** so in Aut, for all $s$ in $Z_n$. Then $T(\alpha)=\alpha(1)=r$ hence we reach an arbitrary element of $U(n)$. Now we verify that $T$ is operation-preserving. If we let $\alpha,\beta\in\text{Aut}(Z_n)$. We then have

![[Pasted image 20230201102943.png]]

[[Isomorphisms Questions]]

