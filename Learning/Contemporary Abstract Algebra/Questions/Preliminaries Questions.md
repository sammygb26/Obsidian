What is the definition of a divisor? #flashcard #CAA #Preliminaries
	We say that $t\mid s$ meaning "$t$ divides $s$" when there exists some integer $n$ such that $s=nt$.

---
What is the well ordering principle? #flashcard #CAA #Preliminaries 
	The well ordering principle says "Every nonempty set of positive integers contains a smallest number".

---
What is the divisor algorithm? #flashcard #CAA #Preliminaries 
	The divisor algorithm says that for integers $a$ and $b$ with $b>0$. Then there exist unique integers $q$ and $r$ with the property that $a=bq+r$, where $0\le r<b$. Here $r$ is the remainder and $q$ is the quotient.

---
What is the greatest common divisor? #flashcard #CAA #Preliminaries 
	The greatest common divisor of two nonzero integers $a$ and $b$ is the largest of all common divisors of $a$ and $b$. We denote this by $\text{gdc}(a,b)$.

---
When are two integers relatively prime? #flashcard #CAA #Preliminaries 
	If $a$ and $b$ are relatively prime when $\text{gdc}(a,b)=1$ then $a$ and $b$ don't share any common divisors.

---
What is the gdc theorem? #flashcard #CAA #Preliminaries 
	This say that for any nonzero integers $a$ and $b$, there exit integers $s$ and $t$ such the $$\text{gdc}(a,b)=as+bt$$Moreover, $gdc(a,b)$ is the smallest positive integer of the form $as+bt$.

---
What does the gcd theorem say for relatively prime numbers? #flashcard #CAA #Preliminaries 
	It says that if $a$ and $b$ are relatively prime, then there exists integers $s$ and $t$ such that $as+bt=1$

---
What is Euclid's lemma? #flashcard #CAA #Preliminaries
	This say that "Every integer greater than 1 is a prime or a product of primes. This product is unique, except for the order in which the factors appear. That is, if $n=p_1p_2\dots p_r$ and $n=q_1q_1\dots q_s$, where the $p$s and the $q$s are primes, then $r=s$ after renumbering the $q$s we have $p_i=q_i$ for all $i$"

---
What is the least common multiple? #flashcard #CAA #Preliminaries 
	The least common multiple of two nonzero integers $a$ and $b$ is the smallest positive integer that is a multiple of both $a$ and $b$. We will denote this integer by $\text{lcm}(a,b)$.

---
What is modular arithmetic? #flashcard #CAA #Preliminaries
	Modular arithmetic is similar to the arithmetic used on a clock when the number is above the modulo we think of it as wrapping back around to 0. This is define by "for two integers $a$ and $b$ then $a\mod b$ is defined as $r$ in the case of $a=qn+r$"

---
What are complex number simply? #flashcard #CAA #Preliminaries 
	Complex numbers are an extension of regular numbers where we consider the imaginary number $\sqrt{-1}=i$. That define $i^2=-1$.

---
How is the standard for of imaginary numbers defined? #flashcard #CAA #Preliminaries 
	This is defined for *real* numbers $a$ and $b$ the standard for of imaginary numbers is $$a+bi$$That is $a$ gives the real component and $b$ gives the imaginary component.

---
How is an imaginary number defined in polar form? #flashcard #CAA #Preliminaries 
	An imaginary number is defined in polar form when we consider it as a point in the imaginary plane (made by extending the number line with an imaginary axis). Then the imaginary number $a+bi$ sits at the point $(a,b)$. The range is $r=\sqrt{a^2+b^2}$ then the angle is $\theta=\arctan(\frac ab)$. This way $$a+bi=r(\cos\theta+i\sin\theta)$$

---
What is the closure under addition property of complex numbers? #flashcard #CAA #Preliminaries 
	This says for any complex numbers $a+bi$ and $c+di$ we have $$(a+bi)+(c+di)=(a+c)+(b+d)i$$This means a sum of complex numbers is too a complex number.

---
What is the closure under multiplication property for complex number? #flashcard #CAA #Preliminaries 
	This say that for complex number $a+bi$ and $c+di$ we have $$(a+bi)(c+di)=(ac)+(ad)i+(bc)i+(bq)i^2=(ac-bd)+(ad+bc)i$$This means that a product of two complex numbers is too a complex number.

---
What does closure under division mean for complex numbers? #flashcard #CAA #Preliminaries 
	This says that when $c+di\neq0$ we have $$\frac{a+bi}{c+di}=\frac{a+bi}{c+di}\frac{c-di}{c-di}=\frac{(ac+bd)+(bc-ad)i}{c^2+d^2}=\frac{ab+bd}{c^2+d^2}+\frac{bc-ad}{a^2+d^2}i$$This means the quotient of two complex numbers is a complex number.

---
What is complex conjugation rule for complex numbers? #flashcard #CAA #Preliminaries 
	This says $(a+bi)(a_bi)=a^2+b^2$

---
What is an inverse for a complex number? #flashcard #CAA #Preliminaries 
	We know for every complex number $a+bi$ this is an inverse $c+di$ such that $(a+bi)(c+di)=1$. That is $(a+bi)^{-1}$ exists in $\mathbb C$

---
What is the power rule for complex numbers? #flashcard #CAA #Preliminaries 
	This say for every complex number $a+bi=r(\cos\theta+i\sin\theta)$ and every positive integer $n$ we have, $$(a+bi)^n=(r(\cos\theta+i\sin\theta))^n=r^n(\cos n\theta+i\sin n\theta)$$

---
That are the nth roots of a complex number? #flashcard #CAA #Preliminaries 
	The $n$th roots of $a+bi$: For any positive integer $n$ the $n$ distinct $n^{\text{th}}$ roots of $a+bi=r(\cos\theta+i\sin\theta)$ are $$\sqrt[n]r\left(\cos\frac{\theta+2\pi k}n+i\sin\frac{\theta+2\pi k}n\right)$$for $k=0,1,\dots,n-1$

---
What does mathematical induction say? #flashcard #CAA #Preliminaries 
	Let $S$ be a set of integers containing $a$. Suppose $S$ has the property that whenever some integer $n\ge a$ belongs to $S$, then the integer $n+1$ also belongs to $S$. Then, $S$ contains every integer greater than or equal to $a$.

---
What does mathematical strong induction say? #flashcard #CAA #Preliminaries 
	Let $S$ be a set of integers containing $a$. Suppose $S$ has the property that $n$ belongs to $S$ whenever every integer les that $n$ and greater than or equal to $a$ belongs to $S$. Then, $S$ contains every integer greater than or equal to $a$.

---
What is an equivalence relation (properties)? #flashcard #CAA #Preliminaries
	This is a generalization of $=$ allowing equality to be defined for more objects. Any relation $R$ which can be defined for a set $S$ where $(a,b)\in R$ ($aRb$) means $a$ relates to $b$ is an equivalence relation if it has three properties.
		1) $(a,a)\in R$ for all $a\in S$ (reflexive property)
		2) $(a,b)\in R$ implies $(b,a)\in R$ (symmetric property)
		3) $(a,b)\in R$ and $(b,c)\in R$ implies $(a,c)\in R$ (transitive property)

---
How is the equivalence class defined? #flashcard #CAA #Preliminaries 
	For some $a\in S$ and equivalence relation over $S$ denotes $\sim$ we define the equivalence class of $a$ as $$[a]=\{x\in S|x\sim a\}$$ That is the set of all elements in $S$ equivalent to $a$.

---
What is a partition of a set? #flashcard #CAA #Preliminaries 
	A *partition* of a set $S$ is a collection of nonempty disjoint subsets of $S$ whose union is $S$. 

---
What is the relation between equivalence classes and a partition? #flashcard #CAA #Preliminaries
	All the equivalence classes of a set $S$ under a relation $a$ form a portion of $S$. An indeed for every partition of $S$ we can define an equivalence relation over $S$ such that the equivalence classes for said partition.

---
How is a function defined? #flashcard #CAA #Preliminaries 
	A function (or mapping) $\theta$ from a set $A$ to a set $B$ is a rule that assigns to each element of $a$ of $A$ to exactly one element $b$ of $B$. Then $A$ s called the *domain* of $\phi$, and $B$ is called the range of $\phi$. If  $\phi$ assigns $b$ to $a$, then $b$ is called the *image of $a$ under $\phi$*. The subset of $B$ comprising all the images of elements of $A$ is called the image of $A$ under $\phi$.

---
How is the composition of functions defined? #flashcard #CAA #Preliminaries 
	Let $\phi:A\to B$ and $\psi:B\to C$. The composition $\psi\phi$ is the mapping from $A$ to $C$ defined by $(\psi\phi)(a)=\psi(\phi(a))$ for all $a$ in $A$.

---
What is a one-to-one function? #flashcard #CAA #Preliminaries 
	A function $\phi$ from a set $A4 is called *one-to-one* if for every $a_1,a_2\in A$ we have $\phi(a_1)=\phi(a_2)$ implies $a_1=a_2$

---
When is a function onto? #flashcard #CAA #Preliminaries 
	A function $\phi$ from set $A$ to a set $B$ is said to be onto $B$ if every element of $B$ is the image of at least on element of $A$. In symbols, $\phi:A\to B$ is onto if for each $b$ in $B$ there is at least one $a$ such that $\phi(a)=b$

---
What are the properties of functions (4)? #flashcard #CAA #Preliminaries 
	Given functions $\alpha:A\to B$, $\beta: B\to C$, and $\gamma:C\to D$, then
		1) $\gamma(\beta\alpha)=(\gamma\beta)\alpha$ (associativity)
		2) If $\alpha$ and $\beta$ are one-to-one, then $\beta\alpha$ is one-to-one
		3) If $\alpha$ and $\beta$ are onto, then $\beta\alpha$ is onto.
		4) If $\alpha$ is one-to-one and onto, then there is a function $\alpha^{-1}$ from $B$ onto $A$ such that $(\alpha^{-1}\alpha)(a)=a$ for all $a$ in $A$ and $(\alpha\alpha^{-1})(b)=b$ for all $b$ in $B$

---
