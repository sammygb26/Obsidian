What are cyclic groups and generators? #flashcard #CAA #CyclicGroups
	A group $G$ is **cyclic** if there is an element $a$ in $G$ such that $G=\{a^n\mid n\in Z\}$This element  is the **generator** of $G$. We writ $G=\langle a\rangle$.

---
When is a group not cyclic? #flashcard #CAA #CyclicGroups 
	A group $G$ is not cyclic if none of it's element are generators of $G$. That is $$\forall a\in G.G\neq\langle a\rangle$$

---
What is the criterion for a^i=a^j say? #flashcard #CAA #CyclicGroups 
	Let $G$ be a group, and let $a$ belong to $G$. If $a$ has an infinite order, then $a^i=a^j$ iff $i=j$. If $a$ has a finite order, say $n$ then $\langle a\rangle=\{e,a,a^2,\dots,a^{n-1}\}$ and $a_i=a^j$ iff $n$ divides $i-j$. That is they are the same modulo $n$.

---
What is the order of an element related to the group it generates? #flashcard #CAA #CyclicGroups 
	For any group element $a$, $|a|=|\langle a\rangle|$

---
What can be say about k when a^k=e? #flashcard #CAA #CyclicGroups 
	If $|a|=n$ and $a^k=e$ then we know $n\mid k$, $n$ divides $k$.

---
What is the relationship between |ab| and |a||b| when ab=ba in a finite group? #flashcard #CAA #CyclicGroups 
	If $a$ and $b$ belong to a finite group and $ab=ba$, then $|ab|$ divides $|a||b|$.

---
What does the a^i=a^j criterion theorem say multiplication by a in \<a\>? #flashcard #CAA #CyclicGroups 
	It says that multiplication by $a$ in $\langle a\rangle$ is essentially addition modulo $n=|a|$. This makes $Z_n$ and $Z$ prototype cyclic groups which give the properties of **all** cyclic groups.

---
How is the group \<a^k\> related to \<a\> (theorem)? #flashcard #CAA #CyclicGroups 
	Let $a$ be an element of order $n$ in a group and let $k$ be a positive integer. Then $\langle a^k\rangle=\langle a^{\text{gcd}(n,k)}\rangle$ and $|a^k|=n/\text{gcd}(n,k)$. That is when we generate a subgroup of a cyclic group the gcd of the order of group and the power of the generator define the smallest step giving the group.

---
How does the order of an element in a cyclic group relate to the overall group? #flashcard #CAA #CyclicGroups 
	In a finite cyclic group, the order of an element divides the order of the group.

---
What is the criterion for \<a^i\>=\<a^j\> and |a^i|=|a^j|? #flashcard #CAA #CyclicGroups 
	Let $|a|=n$. Then $\langle a^i\rangle=\langle a^j\rangle$ iff $\text{gcd}(n,j)=1$, and $|a|=|\langle a^j\rangle|$ iff $\gcd(n,j)=1$.

---
What are the generators of Z_n? #flashcard #CAA #CyclicGroups 
	An integer $k$ in $Z_n$ is a generator of $Z_n$ iff $\text{gcd}(n,k)=1$.

---
What is the Fundamental Theorem of Cyclic Groups? #flashcard #CAA #CyclicGroups 
	Every subgroup of a cyclic group is cyclic. Moreover, if $|\langle a\rangle>=n$, then the order of any subgroup $\langle a\rangle$ is a divisor of $n$; and, for each positive divisor $k$ of $n$, the group $\langle a\rangle$ has exactly one subgroup of order $k$ - namely, $\langle a^{n/k}\rangle$.

---
What does the Fundamental Theorem of Cyclic groups say about the subgroups of Z_n? #flashcard #CAA #CyclicGroups 
	For each positive divisor $k$ of $n$, the set $\langle n/k\rangle$ is the unique subgroup of $Z_n$ of order $k$; moreover, there are the only subgroups of $Z_n$.

---
How does the Euler Phi Function connect to the umber of element of each order in a cyclic group? #flashcard #CAA #CyclicGroups 
	If $d$ is a positive divisor of $n$, the number of elements of order $d$ in a cyclic group is $\phi(d)$ where $\phi(d)=|U(d)|$.

---
What properties of the Euler Phi function make it easier to calculate? #flashcard #CAA #CyclicGroups 
	1. If $p$ is primer then $\phi(p^n)=p^np^n-1$
	2. Then for relatively prime $m$ and $n$, $\phi(mn)=\phi(m)\phi(n)$.

---
What is a subgroup lattice? #flashcard #CAA #CyclicGroups 
	The relationships among subgroups of a group can be graphed. If some group is a subgroup of another we draw a line between the groups.

---
