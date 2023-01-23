What is a permutation of a set? #flashcard #CAA #PermutationsGroups 
	A **permutation** of a set $A$ is a function from $A$ to $A$ that is both one-to-one and onto.

---
What is a permutation group? #flashcard #CAA #PermutationsGroups
	A **permutation group** of a set $A$ is a set of permutations of $A$ that form a group under function composition.

---
How are permutations written in array form? #flashcard #CAA #PermutationsGroups 
	One top row we enumerate all elements of the set. Then bellow we write the resulting element achieved by applying the permutation to the top element.

---
How are permutations multiplies in array format? #flashcard #CAA #PermutationsGroups 
	We need to remember when functions are compose the operations flow right to left. So to find say what element $1$ not leads to we follow its path for the right array then use this element to index into the left array. The element reached by this will be the aliment achieved by applying both permutation to $1$. We do this for all elements to gain the array form of the composed permutation.

---
What is cycle notation? #flashcard #CAA #PermutationsGroups 
	In cycle notation we write out a permutation as the collection of independent cycles. So $\alpha=(1,2)(3,4,6)(5)$ means $1 has the cycle $1\to2\to1$ and so on for the rest (5 is permuted to itself).

---
How can two cycle notation permutations be composted? #flashcard #CAA #PermutationsGroups 
	We bear in mind that composition moves from the right to the left. Each cycle either permutes a value or leaves it the same. So we do this for all cycles for a given value moving from right to left. We then use this values as the next entry in the cycle (if it changes). We continue this until the first element it repeated giving us a cycle. We then move onto some element not in this cycle or finish.

---
What theorem is true will relation to permutations on finite groups and cycles? #flashcard #CAA #PermutationsGroups 
	Every permutation of a finite set can be written a a cycle or as a product of disjoint cycles.

---
What can be said about the disjoint cycles order? #flashcard #CAA #PermutationsGroups 
	Disjoint cycles commute as they share no element their actions do not interfere with one another.

---
What is the relation between the order of a permutation and the size of its cycles? #flashcard #CAA #PermutationsGroups 
	The order of a permutation is the least common multiple of the lengths of its cycles.

---
How can the relation between cycles and order be used to examine large symmetric groups? #flashcard #CAA #PermutationsGroups 
	We can know the order and even how many permutations have some order by looking at the possible ways to break up the permutations into cycles. Then for each archetypal cycle combination we can count the number of different permutations that would give this cycle. This can be done combinatorial with care to divide by repeated.

---
What is a transpositions (in permutations)? #flashcard #CAA #PermutationsGroups 
	A **transposition** is a permutation cycle of length 2. That is it takes one object to another. It is written as $(ab)$ where $a\neq b$. They are also called 2-Cycles.

---
What is the relation between permutations and 2-Cycles? #flashcard #CAA #PermutationsGroups 
	Every permutation in $S_n$, $n>1$, is a product of 2-cycles.

---
What is the symmetric group Sn? #flashcard #CAA #PermutationsGroups 
	With $A=\{1,2,\dots,n\}$, the set of permutations of $A$ is called the **symmetric group of degree $n$**.

---
What important lemma connects the number of two cycles that make up the identity permutation? #flashcard #CAA #PermutationsGroups 
	If $\epsilon=\beta_1\beta_2\dots\beta_r$ where $\beta$'s are 2-cycles, then $r$ is even.

---
What does the always even or always odd theorem say? #flashcard #CAA #PermutationsGroups 
	If a permutation $\alpha$ can be expressed as a product of an even (odd) number of 2-cycles, then every decomposition of $\alpha$ into a product of 2-cycles must have an even (odd) number of 2-cycles. In symbols, if $$\alpha=\beta_1\beta_2\dots\beta_r\hspace{16pt}\text{and}\hspace{16pt}\alpha=\gamma_1\gamma_2\dots\gamma_s,$$where $\beta$'s and the $\gamma$'s are two cycles, then $r$ and $s$ are both even or both odd.

---
What is a even / odd permutation? #flashcard #CAA #PermutationsGroups 
	Since a permutation can either be expressed as an odd number of 2-cycles or an even number (but never both). It is even if it can be expressed in an even number and odd if not.

---
What is the Alternating Group of degree n? #flashcard #CAA #PermutationsGroups 
	The alternating group of degree $n$ ($A_n$) is the subset of $S_n$ made up of only even permutations.

---
What is the order of the alternating group of degree n? #flashcard #CAA #PermutationsGroups 
	The symmetric group of degree $n$, $S_n$, will have order $n!$ (the number of possible permutations). The alternating group of degree $n$ has only the even permutations. Its order is $n!/2$.

---
What permutation group represents the symmetries of a tetrahedron? #flashcard #CAA #PermutationsGroups 
	A tetrahedron has the symmetry group $A_4$ that is the Alternating Group of degree $4$.

---
