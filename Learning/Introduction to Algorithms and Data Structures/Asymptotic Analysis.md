# Asymptotic Analysis
The purpose of asymptotic analysis is to find a way to analyze an algorithm’s efficiency without getting caught up in how a given implementation works or how fast a given system is. Some algorithms fundamentally work faster for example why is [[Merge Sort]] faster than [[Insert Sort]]? 

## Comparing runtimes of Insert Sort and Merge Sort
if we take some specific implementations of Insert Sort and Merge Sort. Broadly, we want to consider 

TI(n) = time taken by [[Insert Sort]] on a list of length n 
TM(n) = time taken by [[Merge Sort]] on a list of length n

![[Pasted image 20220119184241.png]]

We can see that $T_I$ grows much faster than $T_M$ but it isn't the case the $T_I>T_M$ always for example for small values of $n$.

The way we define this idea of growing fundamentally faster is that for any **implementation** of Insert sort will eventually for large enough $n$s take more time than $T_M$ for the same $n$s. Said mathematically
$$
\forall c>0.\exists N.\forall n\ge N. T_M(n)<cT_I(n)
$$
In this case $c$ is any small number we choose. This idea is what defines little $o$

## Definition of Little $o$
For any two functions $f$ and $g$, $f$ is $o(g)$ if 
$$
\forall c>0.\exists N. \forall n \ge N. f(n)<cg(n)
$$
That is no matter how small a $c$ we choose for $g$ the (no matter how much we scale it down) it will always outpace and surpass $f$.

#### Proving some f is o(g)
To prove some $f$ is $o(g)$ (said 'o' of g). All we need to do is find values for $c$ and $N$ and then prove the final part of the definition for these values.

**Example**: is $n^2$  $o(n^3)$?
Informally we can see that $\frac{n^2}{n^3}=n\to\infty$ as $n\to\infty$ but to be concrete we need to prove the following
$$
\forall c > 0.\exists N.\forall n \ge N.n^2<cn^3
$$
If we take $N>\frac{1}{c}$ then $cn^3=cn\cdot n^2\ge cN\cdot n^2> c(\frac{1}{c})n^2=n^2$ we just want to pick some $N$ relative to $c$ that makes the end inequality always true.

#### What is o(g)
$o(g)$ is a [[Set]] of all $f$ that are $o(g)$. That is 
$$
o(g)=\{f:N\to R_{\ge0}|\forall c > 0.\exists N.\forall n \ge N.n^2<cn^3\}
$$
so $f$ is $o(g)$ technically means $f\in o(g)$ but it is convention to write $f=o(g)$. This notation means that $o(g)+o(g)=o(g)$ which really means if $f'\in o(g)$ and $f\in o(g)$ then $f'+f\in o(g)$. This reduces clutter

![[Pasted image 20220119190659.png]]
## Definition of Little $\omega$ 
$\omega$ is the duel of $o$ so it means that if $f$ is $\omega(g)$ means no matter how much we scale up $g$, $f$ will eventually overtake it. Said mathematically we would write
$$
\forall C >0.\exists N. \forall n\ge N.f(n)>Cg(n)
$$
The dual mean that $f=\omega(g) \iff g = o(f)$

## Big O
As with the previous to we only care about in the limit so something is big O of another function if it grows no faster than that other function. That is it is **asymptotically bounded above** by some multiple of that other function. We would say there is some amount we can scale up $g$ such that in the limit (after some sufficiently large value of n) $f$ will never surpass it.
![[Pasted image 20220119192415.png]]
Said mathematically $f$ is $O(g)$ when 
$$
\exists C>0. \exists N. \forall n \ge N. f(n)\le Cg(n)
$$
Then $g$ is also said to be the **asymptotic upper bound** of $f$.

# Big Omega
$\Omega$ is the dual to $O$. $f$ is $\Omega(g)$ means '$f$ grows no slower than $g$ or $g$ is the **asymptotic lower bound** for $f$. We would say there is some scaled down version of $g$ that will in the limit forever be smaller than $f$
![[Pasted image 20220119192231.png]]
Said mathematically $f$ is $\Omega(g)$ when
$$
\exists c>0.\exists N. \forall n\ge N. cg(n)\le f(n)
$$
Again $\Omega$ is the dual of $O$ so $f=\Omega(g)\iff g=O(f)$

# Big Theta
This captures the idea that two functions have the same growth rate. We say they are **asymptotically tight bound**. This happens when for two functions $f$ and $g$ it is true that $f\in O(g)$ and $f \in \Omega(g)$ this can be said as there is some scaled up version of $g$ and some scaled down version of $g$ such that beyond some value of $n$ $f$ will always remain between the two.
![[Pasted image 20220119193241.png]]
Said mathematically $f$ is $\Theta(g)$ if
$$
\exists c, C >0.\exists N.\forall n\ge N. cg(n)\le f(n)\le Cg(n)
$$
We can note also $f=\Theta(g)\iff g=\Theta(f)$

**Reading**: CLRS Chapter 3

[[Asymptotic Analysis Questions]] 