# P and NP
We have looked at efficient algorithms but there is a whole class that is believed to be not even be solve in polynomial time (**P**) $\Theta(n^k)$ for constant $k$ and size $n$. There are **NP** problems that have solutions of the order $\Theta(k^n)$ or at least we haven't found a **P** solution to them yet. **NP** can mean non-deterministic polynomial, meaning we can solve an **NP** problem in when given an input form a non-deterministically.

## Classes of Algorithms
We say something is **polynomial time** if we have a deterministic algorithm $A$ the solves the problem (and is correct for every instance of the problem) and there is fixed $r\in R$ such that for every instance $J$, the algorithm runs in the time at most $O(|J|^r)$. We say a problem is **polynomial time** if we can find an algorithm that solves it. We won't care for the size of $r$ only that this class of solution exists. **NP** problems have not been found to have a  polynomial time. But it hasn't been proven that there is any **NP** time that isn't **P**.

## Cycles and Graphs
We take two graphs $G=(V,E)$. An **Euler tour (ET)** of a given graph is a cycle in the graph which traverses every **edge** exactly once (though it can use vertices more than once). A **Hamiltonian cycle (HC)** of a graph is a simple cycle of the graph which visits every **node** only once. They sound similar but **ET** is in **P** and **HC** has not been proven to be in **P**.

![[Pasted image 20220215113008.png]]

**Euler** proved that any **connected** graph which only has even-degree vertices has an **Euler tour** to be possible. We can check if a graph is connected in $\Theta(m+n)$ time. A vertex is **even** if it has an even number of edges connected to this. So this can also be checked in $\Theta(m+n)$ time. This is known from **graph theory**. This is a **discission** problem as there is a **yes** or **no** answers. We will be looking at **discission** problems.

**Hamilton Cycle** problem is believed to be **NP-complete** and have no **P** solution.

## Verifying versus Finding
We think mainly about **decision problems** when talking about **P** and **NP**. For examples "Does this graph have an Euler tour?", "Does this graph have a Hamiltonian Cycle?" or "Is there edit distance between these two sequences less than 5?" (so we cast edit distance into Y/N). If we can answer a finding question in **P** time we can necessarily find a yes in **P** time as we just run the **P** algorithm then to a polynomial time check.

## Guess and Check
We use **guess and check** to understand the complexity of a **NP** problems. This is how we know something is **NP**. A guessed solution must be of **polynomial time** to the input size. We can check where a guessed solution is correct in **polynomial time** as well. We consider the solution **non deterministic** that is we get it from somewhere (like a non deterministic FSM). We treat the solution as a certificate that shows there is a solution. A certificate isn't a solution the certificate is internal. The guess part is what makes it non deterministic. We must just prove we can check a solution in polynomial time for it to be in **NP**. A certificate for an **Euler Tour** would be a list of edges, then a **Hamilton Cycle** would have a list of edges so both are **NP**.

A **P** problem must be **NP** as the *certificate* we need might as be empty we can generate it all in **P** time.

## Polynomial Time Problems
All algorithmic problems we have looked at **inputs** comes in a prescribed form. If we allow any form we can pad out the input size and then engineer the algorithm around it to get any complexity we want. We want problems that **aren't silly**. We have to be careful with numbers. For example if we describe a number as a **unary** value then we could always represent it in base 2 or 10 and have its true size be log of the **unary size**. Some algorithms we have already looked at have taken this unary approach. For example coin change. This means technically that coin change isn't a polynomial time algorithm in a sensible encoding. We would consider them **pseudo polynomial** algorithms. The sensible format is called an **encoding**, we want **numbers in a base format** and we want **edges in a binary format**.

![[Pasted image 20220215114554.png]]
## Decision Problems
A computational problem $Q$ is a **decision problem** if it can be described in terms of a collection of **potential solutions** $S$ where $Q(J)=1$ if there is a solution in $S$ which solves the instances $J$ and $Q(J)=0 otherwise.

The **complexity class** **P** is the class of decision problems $Q$ for which there is a polynomial-time algorithm to compute $Q$ exactly on all input instances.

## Complexity class NP
Consider a decision problem $Q$ with its collection of **possible solutions** $S$. We say that a two-parameter algorithm $A$ is a **verifier** for $Q$ iff for all instances $J$ of $Q$ there is some $y\in S$ such that
$$
A(J,y)=1\iff Q(J)=1
$$
It doesn't matter at all what the certificate is we just say there is some certificate $y$ (the guess). The idea of **some** comes back to NDFSMs  and allows us to define **NP problems**.

The **complexity class NP** is the class of decision problems $Q$ (wrt a collection of potential solutions/certificates $S$) for which there is a verifier $A=A(J,y)$ which runs in the time polynomial to the size $|J|$ of the instance. There is also **NP-complete** problems which are hardest of all **NP** problems.

## Reductions
A problem $R$ can be **reduced** to a problem $Q$ if there is a polynomial-time computable function $f:\{0,1\}^*\to \{0,1\}^*$ such that for all instances $J$ of $R$
$$
R(J)=1\iff Q(f(J))=1
$$
That is $R$ and $Q\circ f$ solve the problem equivalently their solutions never differ. When we reduce a problem $R$ to $Q$ we say polynomial $R$ is at least as hard as $Q$ that is $R\le_P Q$. It means if we can solve $Q$ in polynomial time we can also solve $R$.

A problem is **NP-complete** if it lives in **NP** but also every other **NP** problem can be represented as this new problem.

[[P and NP Questions]]