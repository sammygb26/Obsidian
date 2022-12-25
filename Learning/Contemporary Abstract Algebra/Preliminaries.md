### Properties of Integers
This was covered previously with **discrete mathematics** but are reiterated here at they are important to abstract algebra overall. 

##### Divisor
The idea of dividing will come up a lot. We say a nonzero integer $t$ is a divisor of $s$ if there is an integer $u$ sch that $s=tu$. We write $t\vert s$ to say $t$ divides $s$. When $t$ is not a divisor of $s$ we write $s \nmid s$.
 
##### Well Ordering Principle
This property is hard to prove so will be taken as an axiom
![[Pasted image 20221223150954.png]]

##### Division Algorithm
![[Pasted image 20221223151036.png]]
This is basically the idea of dividing from school. We divide $a$ by $b$ and we get $q$ (called the quotient) with a remainder $r$.

##### GCD
![[Pasted image 20221223152837.png]]
$\text{gdc}(a,b)=1$ therefore means $a$ and $b$ share no prime factors, or any factors other than $1$.

![[Pasted image 20221223153033.png]]

The case for relatively prime numbers is important and comes at its own corollary.

![[Pasted image 20221223154651.png]]

##### Euclid's Lemma
![[Pasted image 20221223154731.png]]
This is true as if $p$ is prim that divides $ab$ but not $a$. Then there are integers $s$ and $t$ such that $1=as+pt$. Then equally $b=abs+pbt$ and since $p$ divides both terms of the right it divides the right and therefore divides $b$.

##### Fundamental Theorem of Arithmetic
![[Pasted image 20221223161732.png]]

##### Least Common Multiple
![[Pasted image 20221223161856.png]]

### Modular Arithmetic
Again this is another part of **discrete mathematics**. We can define the $\text{mod}$ formula as such. Then $a=qn+r$ where $q$ is the quotient and $r$ is the remainder upon dividing $a$ by $n$ we write $a\text{ mod }n=r$. And so

![[Pasted image 20221223162312.png]]

An interesting aspect of modular arithmetic is that we can move the $\text{mod}$ operator down. That is $(27\cdot 36)\text{ mod }11$ is the same as $((27 \mod 11)\cdot(36\mod 11))\mod 11$. This can be used to simplify the arithmetic required to evaluate such statements. 

### Complex Numbers
Complex numbers are extensions on the regular number line. Then we define $\sqrt{-1}=i$ such that $i$ is a number where $i^2=-1$. We can write a complex number in **standard form** if it is of the form $a+bi$. We can also place the number $a+bi$ in the complex plan where we extend the number line up with the *imaginary line*.

![[Pasted image 20221223165131.png]]

In this way its distance from the origin is $r=\sqrt{a^2+b^2}=|a+bi|$. We can also get the angle $\theta$ to be the angle from the *real* number line to the line to $a+bi$. This will be $\arctan(\frac ba)$. This way $$a+bi=r(\cos\theta+i\sin\theta)$$this is called the **polar form**.

##### Properties of Complex Numbers
![[Pasted image 20221223165505.png]]

### Mathematical Induction
![[Pasted image 20221223171439.png]]

To use induction to prove that a statement involving positive integers is true for every positive integer we first verify that the statement is true for the integer 1. We then *assume* the statement is true for some $n$ and use this assumption to prove that the statement is true for the integer $n+1$. There is also the **strong form** of induction that requires integers bellow $n$ down to the min value $a$.

![[Pasted image 20221223172107.png]]

### Equivalence Relations
Many things may be considered *equivalent* in mathematics however this is true for different things in different contexts. Instead we require a general definition of an **equivalence relation**

![[Pasted image 20221223173415.png]]

When $R$ is an equivalence relation on the set $S$ usually we write $aRb$ instead of $(a,b)\in R$. Usually we replace $R$ then with symbol such as $=,\approx,\sim$ and so on. If some $a\in S$ then the **equivalence class** containing $a$ is $$[a]=\{x\in S\mid x\sim a\}$$for the equivalence relation $\sim$.

##### Partition of a Set
![[Pasted image 20221223174457.png]]

This definition of a **partition** is intertwined with the meaning of an equivalence relation.

![[Pasted image 20221223174715.png]]

### Functions (Mappings)
This will establish the terminology and notation associated with functions for this area.

![[Pasted image 20221223175001.png]]

The notation $\phi:A\to B$ means that $\phi$ is a mapping from $A$ to $B$. Then $\phi(a)=b$ or $\phi:a\to b$ means $\phi$ carries $a$ to $b$. Sometimes an elements in a set can be written multiple ways in these cases the function must be ensured to work the same no matter the input. This ensures that some **correspondence** is truly a function. To do this we assume $x_1=x_2$ then prove $\phi(x_1)=\phi(x_2)$.

![[Pasted image 20221223175530.png]]

In calculus the composition of $f$ with $g$ is written $(f\circ g)(x)=f(g(x))$ the circle will be omitted here.

##### Types of functions
![[Pasted image 20221223175940.png]]

![[Pasted image 20221223180030.png]]

##### Properties of Functions
![[Pasted image 20221223180105.png]]

[[Preliminaries Questions]]