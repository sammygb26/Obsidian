Here we will look at groups of functions, called **permutation groups** from a set $A$ to itself. Earlier only permutation groups were cared about but later a more abstract definition of a group came about. 

![[Pasted image 20230119174703.png]]

So a **permutation** is a function form $A$ to $A$ that is one-to-one and onto. The **permutation group** of $A$ is the set of permutations of $A$ that form a group under function composition. Groups of permutations exist for any set $A$ of objects, but we will focus on the case where $A$ is finite. Furthermore $A$ is taken to be the set $$\{1,2,3,\dots,n\}$$for some positive integer $n$. Unlike calculus where functions are defined on infinite sets and are given by formulas, in algebra, permutations of finite sets are usually given  by explicit listing of each element in the domain and its corresponding element in the range. So a permutation $\alpha$ of the set $\{1,2,3,4\}$ could be defined as:

![[Pasted image 20230119175130.png]]

A more compact way to write this would be as:

![[Pasted image 20230119175157.png]]

Here $\alpha(j)$ is placed bellow $j$ for each $j$. Composition of permutations expressed in array notation is carried out from right to left by going from the top to bottom, then again for the next set.

![[Pasted image 20230119175325.png]]

### Examples

##### Symmetric Groups $S_3$
$S_3$ denotes the set of all one-to-one functions from $\{1,2,3\}$ to itself. The $S_3$ under composition is a group with size elements.

![[Pasted image 20230120084708.png]]

![[Pasted image 20230120084731.png]]

We also have the relation $\beta\alpha=\alpha^2\beta$ and this can be used to work out relations without using the array form.

##### Symmetric Groups $S_n$
$A=\{1,2,...,n\}$, the set of permutations of $A$ is called the **symmetric group of degree $n$**. It is denotes $S_n$. The elements of this group are of the form

![[Pasted image 20230120085003.png]]

The number of elements in $\alpha$ is easy to compute. $\alpha(1)$ has $n$ different options then $\alpha(2)$ has $n-1$ options as it can't be the same as what we picked for $\alpha(1)$ is continues with $\alpha(i)$ having $n+1-i$ options. This in total give $n!$ different possible elements.

Some of these symmetric groups have many subgroups, for example $S_4$ has 30 and $S_5$ has 100.

##### Symmetries of a Square
We can associate each motion in $D_4$ with the permutation of the locations of each of the four corners of a square. For example, if we label the four corner positions as in the figure bellow and keep the labels fixed for reference we can describe a $90\degree$ rotation as:

![[Pasted image 20230120085617.png]]

Or a reflation in the horizontal axis

![[Pasted image 20230120085657.png]]

These two elements  generate the entire group (every element is a combination of $\phi$ and $\rho$)

# Cycle Notation
There is another notation commonly used to specify permutations called **cycle notation**. Cycle notation has *theoretical advantages* as properties of the cycle become apparent when we use this notation. So if we consider the permutation

![[Pasted image 20230120085959.png]]

This could also be written as

![[Pasted image 20230120090015.png]]

This notation is sometimes hard to write to instead it may be written as $$\alpha=(1,2)(3,4,6)(5)$$For another example we can consider

![[Pasted image 20230120090137.png]]

Here $\beta$ an e written as $(2,3,1,5)(6,4)$ or $(4,6)(3,1,5,2)$ as both these unambiguously specify the function $\beta$. The expression $(a_1,a_2,...a_m)$ is called a **cycle of length $m$** or an **$m$-cycle**.

Multiplication with cycles can be introduced by thinking of a cycle as a permutation that fixes any symbol not appearing in the cycle. So $(4,6)$ can be thought of as $$\begin{bmatrix}1&2&3&4&5&6\\1&2&3&6&5&4\end{bmatrix}$$Thinking about the array form we may consider the following example in $S_8$ that is $$\alpha=(13)(27)(456)(8)\hspace{32pt}\beta=(1237)(648)(5)$$Note the commas are left out as there are only single digit numbers. Then we as what is $\alpha\beta$? We can write $\alpha\beta=(13)(27)(456)(8)(1237)(648)(5)$ but we want this in **disjoint** for where all the numbers are not shared by cycles. Now we bare in mind the function composition happens right to left. So $\beta$ s performed first. Going from left to right aswell we can see for example that $1\to 7$ by the end. If we map out what each cycle does to this number starting with $7$ we get $$7\to7\to7\to1\to1\to1\to1\to3$$ This means $\alpha\beta=(173...)$. We can then go right left for each number mapping out this pass. When we repeat a number we have found a cycle. This eventually yields $$\alpha\beta=(1732)(48)(56)$$Another example may be $\alpha$ and $\beta$ as:

![[Pasted image 20230120092002.png]]

then in **cycle notation** we write $\alpha=(12)(3)(45),\beta=(153)(24)$, and $\alpha\beta=(12)(3)(45)(153)(24)$. To put $\alpha\beta$ in a disjoint cycle form we note $(24)$ fixes $1$, then $(153)$ is $1\to5$ the $(45)$ is $5\to4$ the other two fix $4$ hence $(14...)$ is given, similarly $4$ can be found to map to $1$ so our fist cycle is $(14)$. Eventually we get $\alpha\beta=(14)(253)$. It is easy to convert back to array form my noting that $(14)$ just means $1\to4$ and $4\to1$ and so on for $(253)$.

Another remark is that often missing elements left out are just mapped to themselves. So $\alpha$ above can be written as $(12)(45)$. So also

![[Pasted image 20230120092826.png]]

can be written as $\alpha=(134)$. With an identity permutation all but one are left out so its clear something exists $\epsilon=(3)=(5)$.

# Properties of Permutations
We can now look at the properties of permutations and cycles. The first theorem requires writing in permutation form.

### 5.1 Products of Disjoint Cycles
![[Pasted image 20230120093150.png]]

The proof relies on the fact that finite sets must repeat eventually, at this point we also prove the initial element has repeated and so we have a cycle. We can expand this cycle with element not yet in the cycle, this cycle has not element in common with any previous cycles as if it did then our function wouldn't be one-to-one. This eventually covers the whole permutation group.

### 5.2 Disjoint Cycles Commute
![[Pasted image 20230120093701.png]]

This comes from the fact that the elements $\alpha$ and $\beta$ chance don't overlap and so a change made by one doesn't affect the change made by the other. Hence the order doesn't matter.

### 5.3 Order of a Permutation
![[Pasted image 20230120094145.png]]

The proof for this comes from the fact that if the cycles are disjoint then it must be the case that all of them to some power are the identity as they cannot invert each other (being disjoint and so fixing element in the other cycles). Hence the first time the whole permutation is the identity is when we have the smallest number that is divided by the lengths of all the cycles (as this is their order). *This number is the least common multiple*.

![[Pasted image 20230120095336.png]]

### Example
This can be used to determine the order of $7!=5040$ element of $S_7$., we only need to consider the possible disjoint structures. For example 

![[Pasted image 20230120104943.png]]

We can then find the order of each to be the least common multiple. This gives us $7,6,10,5,12,4,3,2$ and $1$. Doing the same thing for $S_{10}$ with $10!=3528800$ would be almost as easy.

We can also determine the number of element in $S_7$ of order 12.  By theorem 5.2 and 5.3 que need only count the number of permutation with the disjoint cycle form $(a_1a_2a_3a_4)(a_5a_5a_7)$. There are $7!$ ways to order this however many are repeated with for example $(1234)=(2341)$. We can correct for this and find the number is $$(7\cdot6\cdot5\cdot4)(3\cdot2\cdot1)/(4\cdot3)=420$$elements of order 12 in $S_7$.

Similarly for $S_3$ we need only find the number of permutation sof the form $(a_1a_2a_3)$ and $(a_1a_2a_3)(a_4a_5a_6)$. There are $(7\cdot6\cdot5)/3=70$ elements of the form $(a_1a_2a_3)$. Then there are $70$ ways again to make the first cycle and $(4\cdot3\cdot2)/3$ ways to make the second (for $(a_1a_2a_3)(a_4a_5a_6)$). But this counts $(a_1a_2a_3)(a_4a_5a_6)$ and $(a_4a_5a_6)(a_1a_2a_3)$ as the same so we also divide by two. In the end this gives us $(7\cdot6\cdot5)(4\cdot3\cdot2)/(3\cdot3\cdot2)=280$ different permutations.

### Transpositions
It is often use full to write a permutation as a product of cycles of length 2, which is a permutation of the form $(ab)$ where $a\neq b$. These are also called **transpositions**.

### 5.4 Product of 2-Cycles
![[Pasted image 20230120110959.png]]

We first see that $\epsilon$ can be expressed as $(12)(12)$, so is a product of 2-Cycles. From 5.1 any permutation can be written as 

![[Pasted image 20230120111123.png]]

We can then expand this to give

![[Pasted image 20230120111141.png]]

However we can get multiple decompositions from the same cycle for example

![[Pasted image 20230120111315.png]]

##### Lemma
![[Pasted image 20230120111343.png]]

This is clearly true for $r=1$ as a two cycle is never the identity. If $r=2$ then we are done. For $r>2$ we proceed with induction, the rightmost 2-cycle is $(ab)$. Then since $(ij)=(ji)$, the product $\beta_{r-1}\beta_r$ can be expressed in one of the following forms

![[Pasted image 20230120155639.png]]

In the first case we are done as the who cancel out leaving us wit h$\beta_1...\beta_r$ which we already know to be $\epsilon$. In the other cases we replaces the right version with the left version. The rules for the bottom 3 lines allow us to **move** some a one back. This can continue must eventually reach the top case in which case we cancel out removing two. Since by induction we assumed $r-2$ $\beta$s make up $\epsilon$ then we are finished. 

### 5.5 Always Even or Always Odd
![[Pasted image 20230120160615.png]]

This simply comes from the previous lemma. Both $\beta$ and $\gamma$ formulations have $s$ and $r$ components. Since we can use the socks shoes property and the fact that a 2-Cycle is its own inverse to show that $$\epsilon=\gamma_1\gamma_2...\gamma_s\beta_r...\beta_2\beta_1$$There are $s+r$ 2-Cycles making up this identity. But we know the total number of 2-Cycles must be even as it is equal to the identity. Hence $s$ and $r$ are either both even or both odd.

### Even and Odd Permutations
![[Pasted image 20230120161051.png]]

This comes from the theorem above as if a permutation can be expressed with an  even number of 2-cycles then all other expression must also be two cycles. The same logic holds for the odd case. 

### 5.6 Even Permutations For a Group
![[Pasted image 20230120161550.png]]

### Alternating Group of Degree $n$
![[Pasted image 20230120161619.png]]

### Theorem 5.
![[Pasted image 20230120161846.png]]

This comes by proving there are equal numbers of even and odd permutations. Hence the group of all even ones is half the size of the total number of element $n$.

The word **degree** for symmetric and alternating groups comes from the study of *polynomials* over $n$ variables. A **symmetric** polynomial in the variables $x_1,x_2,...,x_n$ is one that is unchanged under any transposition of two of the variables. An *alternating* polynomial is one that changes signs under any transposition of two variables. So for example $x_1x_2x_3$ is unchanged with any transposition of two of the three variables. But $(x_1-x_2)(x_1-x_3)(x_2-x_3)$ changes signs when any two variables are transposed.

Every **symmetric** group is made out of transpositions, so **symmetric** polynomials (being unchanged by transpositions) are unchanged by members of the symmetric group. Equally since the **alternating** group is the product of an even number of transpositions, the alternating polynomials are those that are unchanged by members of the symmetric group.

# Examples

### Rotations of a Tetrahedron
The 12 rotations of a regular tetrahedron can be conveniently described with the elements of $A_4$. The top row bellow illustrates the identity

![[Pasted image 20230120192812.png]]

![[Pasted image 20230120194604.png]]

The first element is the identity, then the next three are all $180\degree$ edge rotations. The second row is all the $120\degree$ face rotations about exes joining a vertex to the center of the opposite face. The third row is $-120\degree$ (or $240\degree$) face rotations. The four rotations in the second row can be obtained from those in the first row by left-multiplying the four in the first row by $(123)$, similarly this can be done using $(132)$ for the third row.

### Encryption Using Permutation
One of the first encryption methods is the Caesar cipher, use by Julius Caesar to send messages to his troops. The way words are encrypted is by replacing each word with a word three to the right on the alphabet, wrapping around. So "ATTACK AT DAWN" becomes "DWWDFN DW GDZQ".

But any **permutation** can be used as a cypher. For example $$\alpha=\begin{bmatrix}1&2&3&4\\3&4&2&1\end{bmatrix}$$here we break the message up into 4 letter sequences ignoring spaces. So We get "ATTA CKAT DAWN" then we permute each block giving "ATAT TACK NWDA". Then we can use $\alpha^{-1}$ to decrypt. The encryption gets better when we break a length $n$ message into a single $n$ block and permutation. We could also increase this further and use junk  letters inbetweener.

### Rubik's Cube
The Rubik's Cube is made from 48 cubes called "facets", this is a classic group theory puzzle. The set of all cube positions forms a group of permutations of order 4325200327438985600.

### A Check-Digit Scheme Based on $D_5$
In [[Preliminaries]] we looked at a check digit for identification numbers. The best method use $X$ to allow the representation of $10$ as a single digit then make the dot product $0\mod 11$.

But another method was devised that used the dihedral group of order 10 that detect all single-digit errors and all transposition errors involving adjacent digits without the necessity of avoiding certain numbers or introducing a *new character*.

The way this method works is to treat the digits of the number as elements of $D_{10}$. Then for a sequence $a_1a_2.a_{n-1}$ we pick $a_n$ such that $$\sigma(a_1)\sigma^2(a_2)...\sigma^{n-1}(a_{n-1})\sigma^n(a_n)=0$$Where $\sigma$ represents applying $a_1$ once to $e$ (with $\sigma^2$ being twice and so on). Since $\sigma^i(b)\neq b\sigma^i(a)$ if $a\neq b$, all single-digit errors are detected. Also $$a\sigma(b)\neq b \sigma(a)\hspace{32pt}\text{if }a\neq b$$as can be check case by case. It follows that all adjacent errors involving adjacent digits are detected.

[[Permutation Groups Questions]]

