# Unsolvable Problems
We will look at a class unsolvable problem *the halting problem*. Then we can reduce other to this hence proving them to be unsolvable.

## Functions
Functions can be described un many ways. 

**Mathematics Way** - Originally mathematicians like *Euler* was something that could be written down as a formula. $f(n)=n!+n^2+5$ is an example of a function defined on natural numbers. In the 19th centenary there was a shift starting with *Dirichlet* where a function was conceived as an abstract object an *infinite lookup table*. This is what today mathematicians have in mind when they talk about functions. So this

![[Pasted image 20220329100812.png]]

Is a function. But there is an uncountable infinity of these function defeminations so what do we mean by supposing they exist?

**Computer Science Way** - CS-educated people think of function differently. It is defined by a *piece of code*. 

![[Pasted image 20220329101109.png]]

Hence this defines a factorial function. By this definition we much be able to write down and compute a function (like in the original mathematics definition). In this way we must be able to compute this function, so what is a incomputable function? We can generally look at the second mathematics one.

## The Halting Problem
This is a classic example of an incomputable problem. Say a RM computation *halts* if we eventually emerge at an exit. We also know that RM and their memory states can be encoded in natural numbers $(n,m)$ (as in a universal machine). A *halting tester* is a machine that takes as inputs $m$ and $n$ and tells us whether the machine $m$ halts when we run on initial memory state $n$.

![[Pasted image 20220329101528.png]]

We need it to say that our tester gives a definite answer either way. It would be easy without this was we could just simulate our program in a universal machine and it would halt when the machine halts. But not when the simulation kept running (object machine doesn't halt) hence we will never know either way. The theorem is *there is no such register machine*. 
$$
h(m,n)=\text{(0 if a machine halts on input n, 1 otherwise)}
$$
If this function was computable we could construct a halting tester easier. Hence this function must not be computable.

## Proof
If we suppose a halting tester exists. We can loop the *halts* output hence we will not halt if the object does halt. Hence either the object halts or the tester halt. Then we need to test if itself halts or not. For a machine to run itself we must encode itself then we also need the state but we may like just a single number. 

![[Pasted image 20220329102418.png]]

This is the *SELF-APP* where we take in an input $A$ (encoding RM machine) then the rest can be 0. Afterwards the registers are set up so that $B$ encodes the machine state again hence the Halting Tester machine is testing if it itself halts.

We could then package this whole machine $P$ and if $p$ is the numerical code for $P$ and we input $p$. Hence a computation is trying to analyze its own halting behavior. But we have *tied* the halts end hence if it does hault it doesn't hault and if it does hault it doesn't. This is a contradiction hence the machine cannot exist.

## Russell's Paradox
This is a predecessor to the above problem. We can define $R$ as the set of all sets that don't contain themselves. Then we can ask if $R$ contains itself. But $R$ can only contain itself iff it doesn't contain itself. *Russell's analogy:* A village barber (a man) shaves exactly those men in the village who don't shave themselves. Does the barber shave himself? The problem is the idea of self reference where we apply something to itself along with a negation. This causes a paradox.

## World of (Un)solvability
![[Pasted image 20220329104051.png]]

So we have a polynomial time area, then above a 'wider class' NP containing SAT problems and reductions to SAT. We can also see names of games where the problem is finding a perfect move. So any n-candy crush being in NP means candy crush optimal strategies can be found in NP time. Then solvable contains other games so we could find some program that can solve n-go or n-chess but not in NP time. Other problem have also been shown to be unsolvable like the halting problem i.e. the halting problem can be reduced to them.

## Diophantine Equations
We can consider what *integer solutions* ($x,y,z\in Z$). Give integer solutions to equations. So
$$
x^2+y^2+z^2=42
$$
What solutions are there. Since all squares must be positive we can do a *bounded search* and find a solution if it exists. Then take 
$$
x^2+y^3+z^2=42
$$
But cubes can be negative and positive hence we don't know the range of values we will have to look through. There has only recently solved in 2019 with the solution.

![[Pasted image 20220329105108.png]]

Hence these problems can be wildly harder. We also can't tell from the equation purely. The more general problem is deciding given a multivariable polynomial equation, we want to know if there is a solution. It has been proven there is no such solution and this is similar to the halting problem as we do an unbounded search and don't know how long it will run.

## Post's word problem
This is another unsolvable problem. We consider strings over a finite alphabet $\{a,b\}$ for example. We want to know if given two sets of strings $A$ and $B$ (the strings are made out of the alphabet) if there is some string that can be formed by both a combination of those in one set and the other (where we can take the same element multiple times).

[[Unsolvable Problems Questions]]
