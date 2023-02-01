What is the order of a group? #flashcard #CAA #FiniteGroupsSubgroups
	The number of element in a group (finite or infinite) is called its **order**. this is denoted $|G|$ for a group $G$.

---
What is the order of an element in a group $G$? #flashcard #CAA #FiniteGroupsSubgroups 
	The order of an element in a group $G$ is the smallest positive integer $n$ such that $g^n=e$. If no such integers exists, we say that $g$ has **infinite order**. The order for an element $g$ is denotes $|g|$.

---
What is a subgroup? #flashcard #CAA #FiniteGroupsSubgroups 
	If a subset $H$ of a group $G$ is itself a group under the operation $G$, we say that $H$ is a **subgroup** of $G$.

---
What notation is used to say that H is a subgroup and a proper subgroup of G? #flashcard #CAA #FiniteGroupsSubgroups 
	If we write $H\le G$ this means that $H$ is a subgroup of $G$. If we want to write that $H$ is a **subgroup** of $G$ but not equal to $G$ we write $H<G$. This means $H$ is a **proper subgroup** of $G$.

---
What is the one step subgroup test? #flashcard #CAA #FiniteGroupsSubgroups 
	If $G$ is a group and $H$ is a nonempty subset of $G$. If $ab^{-1}$ is in $H$ whenever $a$ and $b$ are in $H$, then $H$ is a subgroup of $G$.

---
What are the steps to apply the one-step subgroup test? #flashcard #CAA #FiniteGroupsSubgroups 
	To apply the one-step subgroup test we first 
		1. Identify a property $P$ that distinguishes the elements of $H$ form others in $G$
		2. Prove that the identity has property $P$ (proving $H$ is nonempty)
		3. Then prove that for any elements with the property $P$ $ab^{-1}$ also has the property $P$.

---
What is the two-step subgroup test? #flashcard #CAA #FiniteGroupsSubgroups 
	If $G$ is a group and $H$ is a nonempty subset of $G$. If $ab$ is in $H$ whenever $a$ and $b$ are in $H$ ($H$ is closed under the operation), and $a^{-1}$ is in $H$ whenever $a$ isn't $H$ ($H$ is closed under taking inverses), then $H$ is a subgroup of $G$.

---
What are the three ways to prove a negative subgroup result? #flashcard #CAA #FiniteGroupsSubgroups 
	1. Show that the identity is not in the set
	2. Exhibit an element of the set whose inverse is not in the set
	3. Exhibit two elements of the set whose product is not in the set.

---
What is the finite subgroup test? #flashcard #CAA #FiniteGroupsSubgroups 
	This is an easier way to prove a subgroup when finite group. Let $H$ be a nonempty finite subset of a group $G$. If $H$ is closed under the operation of $G$, then $H$ is a subgroup of $G$. This comes form the property that a sequence $a^1,a^2a^3,...$ eventually will eventually repeat element. The number of $a$s in between will therefore be the identity $e$.

---
What is a cyclic group of a? #flashcard #CAA #FiniteGroupsSubgroups 
	The **cyclic subgroup of $G$ generated by $a$** is the set $\langle a\rangle=\{a^n\mid n\in Z\}$ where $a^0$ is taken to be the identity.  Then this is always a subgroup of $G$ that is the smallest subgroup that contains $a$. Every cyclic group is Abelian.

---
What is the center of a group? #flashcard #CAA #FiniteGroupsSubgroups 
	The center, $Z(G)$, of a group $G$ is the subset of elements in $G$ that commute with every element in $G$. In symbols, $$Z(G)=\{a\in G\mid ax=xa \text{ for all $x$ in $G$}\}$$This is always a subgroup of $G$.

---
What is the centralizer of a in a group G? #flashcard #CAA #FiniteGroupsSubgroups 
	The centralizer of $a$ in $G$, $C(a)$, is the set of all elements in $G$ that commute with $a$, In symbols $$C(a)=\{g\in G\mid ga=ag\}$$Every centralizer is a subgroup.

---