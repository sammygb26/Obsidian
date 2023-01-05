### Terminology and Notation
We will look at **finite groups** but some terminology and notation will be useful in this discussion.

![[Pasted image 20230103124355.png]]

![[Pasted image 20230103124723.png]]

### Examples
We can take the set $U(15)=\{1,2,4,7,8,11,13,14\}$ as a group under multiplication modulo $15$. There are eight elements so $|U(15)|=8$. Then we may look at different elements t get an idea of their order. $1^1=1$ so $|1|=1$. We have $7^1=7$, $7^2=4$, $7^3=13$ and finally $7^4=1$ hence $|7|=1$. This can be done for all the numbers. Notes $13$ may be hard as it is a large number. But $13=-2\mod15$ so we can take $13^2=(-2)^2=4$ (under modulo $15$). Then we can take $13^3=(-2)^3=-8$ and then $13^4=-2\cdot(-8)=16=1$. Hence $|13|=4$.

Can can take $Z_{10}$ under addition modulo $10$. Since $1\cdot2=2$, $2\cdot2=4$, $3\cdot2=6$, $4\cdot2=8$ and finally $5\cdot2=10=0$ hence $|2|=5$. We also know no number can have a order greater than $10$ since at this point they are multiplies of $10$ and so are the identity $0$ under modulo $10$.

But then we can consider $Z$ under ordinary addition. Here every nonzero element has infinite order, since the sequence $a,2a,3a,...$ never includes $0$ when $a\neq0$.

### Subgroups
![[Pasted image 20230103130217.png]]

This comes from the observation that many of the groups we have discussed have smaller groups inside them which can be self contained under the operation. Like $SL(2,\mathbf R)$ being a subset of $GL(2,\mathbf R)$.

The notation $H\le G$ is taken to mean $H$ is a subgroup of $G$. If we want to write that $H$ is a subgroup of $G$ but not equal to $G$ we write $H<G$. This is called a **proper subgroup**. The subgroup $\{e\}$ is called the *trivial subgroup* of $G$ while any other subgroup is a *nontrivial subgroup* of $G$.

### Subgroup Tests
There are some tests that can be used to see whether a subset $H$ of a group $G$ is a subgroup of $G$. This can be done instead of directly verifying the group axioms.

##### One-Step Subgroup Test
![[Pasted image 20230103130856.png]]

We know $H$ is associative as the same operation as $G$ is used. Then we know $H$ contains $G$ as for any $x$ in $H$. We set $a=x$ and $b=x$ then we know $ab^{-1}=xx^{-1}=e$ is in $H$. We also know if $x$ is in $H$ then $x^{-1}$ is in $H$. We set $a=e$ and $b=x$ then we know $ab^{-1}=ex^{-1}=x^{-1}$ is in $H$. Then we also know $H$ is closed as if there where some $x$ and $y$ such that $xy\not\in H$ then we know $y^{-1}$ exists. Hence we set $a=x$ and $b=y^{-1}$ and so $ab^{-1}=xy\in H$ and so $H$ is closed.

This is called the **one-step subgroup test** but there are four steps involved. This is similar to the Second Principle of Mathematical Induction.

1. Identify the property $P$ that distinguishes the elements of $H$; that is, identify a defining condition.
2. Prove that the identity has property $P$. (This verifies the $H$ is nonempty.)
3. *Assume* the two elements $a$ and $b$ have the property $P$.
4. Use the assumption that $a$ and $b$ have the property $P$ to show that $ab^{-1}$ has property $P$.

##### Examples
Let $G$ be an Abelian group with identity $e$. Then $H=\{x\in G\mid x^2=e\}$ is a subgroup of $G$. Here the defining property of $H$ is the condition $x^2=e$. We know $ae=a$ hence $e^2=ee=e$ hence $e$ is in the group. Then if we assume $a$ and $b$ exist such that both have the property $x^2=e$. We want to show $ab^{-1}$ is in $H$. We know $bb=b^2=e=b^{-1}b$. Hence $b=b^{-1}$. $(ab^{-1})^2=(ab)^2=abab=aabb=e$ where the last step happens since $G$ is Abelian.

Let $G$ be an Abelian group under multiplication with identity $e$. Then $H=\{x^2\mid x\in G\}$ is a subgroup of $G$. Now $e\in G$ and $e^2=e$ hence $e\in H$. If there are two elements of $H$, $a^2$ and $b^2$ such that $a,b\in G$ then we want to show $a^2(b^2)^{-1}\in H$. We know if $b\in G$ then $b^{-1}\in G$. Then since this operation must be closed we know $ab^{-1}\in G$. Hence since the operation is Abelian $a^2(b^2)^{-1}=aab^{-1}b^{-1}=ab^{-1}ab^{-1}=(ab^{-1})^2$ which must be in $H$ since we know $ab^{-1}\in G$.

### Two-Step Subgroup Test
![[Pasted image 20230103134123.png]]

This is proved by knowing the operation is associative since it is the operation of some other group. Then we know $e$ is in $G$ since for some element $x$ in $H$ (since $H$ is nonempty) we know $x^{-1}$ is also in $H$ (closed under taking inverses). Then if $a=x$ and $b=x^{-1}$ then $ab=xx^{-1}=e$ is in $H$ (closed under operation).

Proofs are similar to in the *one-step* case we just take the property $P$ and use it to prove $ab$ has the property $P$ and $a^{-1}$ has the property $P$.

##### Examples
If $G$ is an Abelian group. Then $H=\{x\in G\mid |x| \text{ is finite}\}$ is a subgroup of $G$. Since $|e|=1$ we know $e\in H$. If we take two $a,b\in H$ then we want to prove $ab\in H$. Now $(ab)^{|a||b|}=(a^{|a|})={|b|}(b^{|b|})^{|a|}=e^{|b|}e^{|a|}=e$ Hence $|ab|\le|a||b|$ and so is finite meaning $ab\in H$ (closed under operation). Then take some $x\in H$ we know $|x|=n$ for some $n\in Z^+$. Then  $e=x^{|x|}=xx^{|x|-1}=xx^{-1}$. So we know $x^{-1}=x^{|x|-1}$ but if $|x|=1$ then $x^{-1}=e$ and so is in $H$. Then otherwise $x^{|x|-1}$ can be made our of a composition of $x$'s. Each composition is in $H$ since $H$ is closed to operation hence $H$ is a subgroup of $G$.

Let $G$ be an Abelian group and $H$ and $K$ be subgroups of $H$. Then $HK=\{hk\mid h\in H, k\in K\}$ is a subgroup of $G$. First note that $e=ee$ belongs to $HK$ because $e$ is in $H$ and $K$. Then assume $a$ and $b$ are in $HK$ we want to show $ab\in HK$. By definition there exists $h_1,h_1\in H$ and $k_1,k_2\in K$ such that $a=h_1k_1$ and $b=h_2k_2$. Now since $H$ and $K$ are groups and so closed to operation $h_1h_2\in H$ and $k_1k_2\in K$. This means $ab=h_1k_2h_1k_2=h_1h_2k_1k_2\in HK$ ($HK$ closed to operation). Now if $x\in HK$ then $x=hk$ for $h\in H$ and $k\in K$. We also know $h^{-1}\in H$ and $k^{-1}\in K$ and so $x^{-1}=(hk)^{-1}=k^{-1}h^{-1}=h^{-1}k^{-1}\in HK$ by definition ($HK$ is closed to inverses).

##### Negative Results
We might ask how to prove a negative results. That a subset of a group is *not* a subgroup? Here are three possible ways

1. Show that the identity is not in the set
2. Exhibit an element of the set whose inverse is not in the set
3. Exhibit two elements of the set whose product is not in the set

Let $G$ be $\mathbf R-0$ the group of nonzero real numbers under multiplication. Then $H=\{x\in G\mid x=1\text{ or }x\text{ is irrational}\}$ and $K=\{x\in G\mid x\ge1\}$. Then $H$ is not a subgroup of $G$, since $\sqrt2\in H$ but $\sqrt2\cdot\sqrt2\not=2\in H$. Also, $K$ is not a subgroup, since $2\in K$ but $2^{-1}\not\in K$.
 
### Finite Subgroup Test
This is easier to use when we consider are dealing with finite groups.

![[Pasted image 20230103143215.png]]

We need only show that $a^{-1}\in H$ when $a\in H$ (from theorem *two-step subgroup test*). If $a=e$ then we are done. If $a\neq e$ we consider the sequence $a^1,a^2,a^3,\dots$. By closure, all of these elements belong to $H$. Since $H$ is finite, not all of these elements are distinct. Say $a^i=a^j$ then $a^{j-i}=e$ and since $a\neq e$, $i-j>1$. Thus $aa^{i-j-1}=a^{i-j}=e$ and therefore, $a^{i-j-1}=a^{-1}$. Then since $i-j-1\ge 1$ implies $a^{i-j-1}\in H$ by closure and we are done.

# Subgroup Examples
The next examples show how subgroup tests work. We first introduce an important notation. For any element $a$ from a group, we let $\langle a\rangle$ denote the set $\{a^n\mid n\in Z\}$. In particular, observe that the exponents of $a$ include all negative integers as well as

Since $a\in\langle a\rangle$, $\langle a\rangle$ is not empty. Then $a^n,a^m\in\langle a\rangle$. Then $a^n(a^m)^{-1}=a^{n-m}\in\langle a\rangle$. So by **one-step subgroup test** $\langle a\rangle$ is a subgroup of $G$. The group $\langle a\rangle$ is called the *cyclic subgroup of $G$ generated by $a$*. In the case $G=\langle a\rangle$, we say that $G$ is *cyclic* and $a$ is a *generator* of $G$ (a cyclic group may have many generators). Then although the list $\dots a^{-2},a^{-1},a^0,a^1,a^2\dots$ has infinitely many entries, the set $\{a^n\mid n\in Z\}$ may have only finitely many elements. Also note that, since $a^ia^j=a^{i+j}=a^{j+i}=a^ja^i$ **every cyclic group is Abelian**.

##### Examples
In $U(10)$, $\langle 3\rangle\{3,9,7,1\}=U(10)$, for $3^1=3$, $3^2=9$, $3^3=7$, $3^4=2$, $3^5=3^4\cdot 3=3...;3^{-1}=7$ since $3\cdot 7=1$. Then $3^{-2}=9$ since $9\cdot 3^2=1$.

In $Z_{10}$, $\langle2\rangle=\{2,4,6,8,0\}$. Remember, $a^n$ means $na$ when the operation is addition.

In $Z$, $\langle-1\rangle=Z$. Here each entry in the list $\dots$, $-2(-1),-1(-1), 0(-1),1(-1),2(-1),\dots$ represents a distinct group element.

In $D_n$ the dihedral group of order $2n$, let $R$ denote a rotation of $360/n$ degrees. Then $$R^n=R_{360\degree}=e,\hspace{32pt}R^{n+1}=R,\hspace{32pt}R^{n+2}=R^2,...$$Similarly, $R^{-1}=R^{n-1}$, $R^-2=R^{n-2}$,..., so that $\langle R\rangle=\{e,R,...,R^{n-1}\}$. We see that the powers of $R$ "cycle back" periodically with period $n$. Visually, raising $R$ to successive positive powers is the same as moving counterclockwise around the following circle one node at a time.

![[Pasted image 20230103152124.png]]

In Chapter 4 we will show that $|\langle a\rangle |=|a|$; that is the order of the subgroup generated by $a$ is the order of $a$ itself. For any element $a$ of a group $G$, it is useful to think of $\langle a\rangle$ as the smallest subgroup of $G$ containing $a$. This notion can be extended to any collection $S$ of elements from the group $G$ by defining $\langle S\rangle$ as the subgroup of $G$ with the property that $\langle S\rangle$ contains $S$ and if $H$ is any subgroup of $G$ containing $S$ then $H$ also contains $\langle S\rangle$. Thus $\langle S\rangle$ is the smallest subgroup of $G$ that contains $S$. The set $\langle S\rangle$ is called *the subgroup generated by $S$*.

##### Examples
In $Z_{20}$, $\langle8,14\rangle=\{0,2,4,\dots,18\}=\langle 2\rangle$
In $Z$, $\langle 8,13\rangle=Z$
In $D_4$, $\langle H,V\rangle=\{H,H^2,V,HV\}=\{R_0,R_{180},H,V\}$
In $D_4$, $\langle R_{90}, V\rangle=D_4$
In $\mathbf R$ under addition, $\langle 2, \pi,sqrt2\rangle=\{2a,b\pi,c\sqrt 2\mid a,b,c\in Z\}$.
In $\mathbf C$ under addition, $\langle 1,i\rangle=\{a+bi\mid a,b\in Z\}$ (called "Gaussian integers")
In $\mathbf{C^\star}$ under multiplication $\langle 1,i\rangle={1,-1,i,-i}=\langle i\rangle$

### Center of a Group
![[Pasted image 20230103153902.png]]

Then for every **center of a group** we know

![[Pasted image 20230103153957.png]]

We know $e\in Z(G)$ as it is trivially true that for any $x\in G$ we have $ex=x=xe$. Now we suppose $a,b\in Z(G)$ we want to prove $ab\in Z(G)$. We know $\forall x\in G$ that $ax=xa$ and $bx=xb$. Hence $(ab)x=a(bx)=a(xb)=(ax)b=x(ab)$ hence $ab\in Z(G)$ is closed under operation. Then we assume $a\in Z(G)$ and we want to prove $a^{-1}\in Z(G)$. Now if $ax=xa$ then $a^{-1}axa^{-1}=a^{-1}xaa^{-1}$ which implies $xa^{-1}=a^{-1}x$ as was to be shown hence $a^{-1}$ is in $Z(G)$ if $a$ is (closed to inverses). 

##### Example
Now lets defined the centers of the dihedral groups. For $n\ge3$, $$Z(D_n)=\begin{cases}\{R_0,R_{180}
\}&\text{ when $n$ is even}\\
\{R_0\}&\text{ when $n$ is odd}\end{cases}$$To verify this first observe that since every rotation in $D_n$ is a power of $R_{360/n}$, rotations commute with rotations. We now investigate when a rotation commutes with a reflection. For any rotation $R$ and reflection $F$. $RF$ is a reflection we have $RF=(RF)^{-1}=F^-1 R^{-1}$ hence $RF=FR$ only when $R=R^{-1}$ this is only the case when $R=R_0$ or $R_{180}$ which only exists when $n$ is even.

### Centralizer of $a$ in $G$
Although an element from a non-Abelian group does not necessarily commute with every element of the group, there are always some elements for which is will commute. For example every element $a$ commutes with all powers of $a$. This observation prompts the next definition

![[Pasted image 20230103155647.png]]

##### Example
In $D_4$ we have the following centralizers 

1. $C(R_0)=D_4=C(R_{180})$
2. $C(R_{90})=\{R_0,R_{90},R_{180},R_{270}\}=C(R_{270})$
3. $C(H)=\{R_0,H,R_{180},V\}=C(V)$
4. $C(D)=\{R_0,D,R_{180},D'\}=C(D')$

Each of the centralizers is a subgroup of $D_4$ which is not a coincidence

##### C(a) is a subgroup
![[Pasted image 20230103160059.png]]

[[Finite Groups, Subgroups Question]]