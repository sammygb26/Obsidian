What is the definition of a group isomorphism? #flashcard #CAA #Isomorphisms
	An isomorphism $\phi$ from a group $G$ to a group $\bar G$ is a one-to-one mapping from $G$ onto $\bar G$ that preserves the group operation. That is $$\phi(ab)=\phi(a)\phi(b)\hspace{32pt}\text{for all }a,b\in G$$

---
When are two groups isomorphic? #flashcard #CAA #Isomorphisms 
	Two groups $G$ and $\bar G$ are isomorphic if there is an isomorphism from $G$ to $\bar G$ (or visa versa). This is written as $$G\approx\bar G$$

---
What are the steps to prove an isomorphism? #flashcard #CAA #Isomorphisms 
	1. **Mapping**: Need to define a candidate for the isomorphism (a function $\phi:G\to\bar G$)
	2. **One-to-one**: prove $\phi$ is one-to-one that $\phi(a)=\phi(b)$ implies $a=b$.
	3. **Onto**: prove $\phi$ is onto, pick some arbitrary $\bar g\in \bar G$ and prove there is some $g\in G$ such that $\phi(g)=\bar g$
	4. **OP**: Prove that $\phi$ is operation preserving. That is $\phi(ab)=\phi(a)\phi(b)$

---
What is Cayley's theorem? #flashcard #CAA #Isomorphisms 
	Every group is isomorphic to a group of permutations.

---
Why is Cayley's theorem true? #flashcard #CAA #Isomorphisms 
	We can make a permutation function for each element in some group $G$. This function $T_g(x)=gx$. Because a group operation never goes to the same element twice this is onto and one-to-one since $G$ and $\bar G$ are the same size. Then we can prove $T_gT_h=T_{gh}$. Which means $\phi(gh)=\phi(g)\phi(h)$ and so making a permutation function for each element of $G$ gives a permutation group isomorphic to $G$.

---
How do identities change under an isomorphism? #flashcard #CAA #Isomorphisms 
	The identity in $\bar G$ is the the same as in $G$ under the isomorphism. That is $$\bar e=\phi(e)$$

---
How does raising an element to a power affect its version under an isomorphism? #flashcard #CAA #Isomorphisms 
	We say $\phi(a^k)=[\phi(a)]^k$

---
How does the commutativity of element of a group change under an isomorphism? #flashcard #CAA #Isomorphisms 
	It doesn't if $ab=ba$ then $\phi(a)\phi(b)=\phi(b)\phi(a)$.

---
How is the cyclicity of a group related to the cyclicity of a group it is isomorphic with? #flashcard #CAA #Isomorphisms 
	They are the same that is $$G=\langle a\rangle\iff\bar G=\langle\phi(a)\rangle$$

---
How does order change under an isomorphism? #flashcard #CAA #Isomorphisms 
	It doesn't. $|a|=|\phi(a)|$

---
How doesn't the size of two isomorphic groups compare if they are finite? #flashcard #CAA #Isomorphisms 
	If two groups are isomorphic and finite then they have the same number of elements.

---
If some function is an isomorphism between groups what is its inverse with relation to those groups? #flashcard #CAA #Isomorphisms 
	If $\phi:G\to\bar G$ is an isomorphism from $G$ to $\bar G$ the $\phi^{-1}$ is an isomorphism from $\bar G$ to $G$.

---
If a group is Abelian what can be said about the groups it is isomorphic to? #flashcard #CAA #Isomorphisms 
	It can be said that these groups are also Abelian.

---
If a group is cyclic what can be said about groups it is isomorphic to? #flashcard #CAA #Isomorphisms 
	It can be said that these groups are also cyclic.

---
If some group has a subgroup what can be said about some other group which is isomorphic to the original group? #flashcard #CAA #Isomorphisms 
	For a group $G$ with a subgroup $S$. If $G$ is isomorphic to $\bar G$ under $\phi$. Then $S$ is isomorphic to $\bar S=\phi(S)$ (image of $S$) and $\bar S$ is a subgroup of $\bar G$.

---
What are some ways to prove two groups are not isomorphic with each other? #flashcard #CAA #Isomorphisms 
	1. Observe $|G|\neq |\bar G|$
	2. Observe $G$ or $\bar G$ is cyclic but the other is not
	3. Observe $G$ or $\bar G$ is abelian but the other is not
	4. Show the largest order of an element in $G$ is not he same as in $\bar G$.
	5. Show the number of element of some order is not the same in $G$ ad in $\bar G$

---
What is an automorphism? #flashcard #CAA #Isomorphisms 
	An **automorphism** is an isomorphism from a group $G$ to itself.

---
What is the inner automorphism induced by a? #flashcard #CAA #Isomorphisms 
	If $G$ is a group, let $a\in G$. Then function $\phi_a$ defined by $\phi_a(x)=axa^{-1}$ for all $x$ in $G$ is called the *inner automorphism of $G$ induced by $a$*.

---
What is Aut(G)? #flashcard #CAA #Isomorphisms 
	This is the set of all automorphisms  on the set $G$.

---
What is Inn(G)? #flashcard #CAA #Isomorphisms 
	This is the set of all inner automorphism on the set $G$.

---
What can be said about the sets Aut(G) and Inn(G)? #flashcard #CAA #Isomorphisms 
	It can be said that these are both **groups** under function composition.

---
What can be said about Aut(Z_n)? #flashcard #CAA #Isomorphisms 
	It can be said that $Aut(Z_n)\approx U(n)$. That is the set of all automorphism on the group $Z_n$ is isomorphic to the group $U_n$.

---
