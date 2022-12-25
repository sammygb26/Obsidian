# Satisfiability and NP-completeness
This will focus on the idea of **reductions** we can do in the complexity of out programs. We will look at different **NP-complete** problem to another. Something is **P** if it runs in **polynomial time** that is it is $O(n^k)$ for constant $k$ and input size $n$.
**NP** means non-polynomial so can be of the for $O(k^n)$ for constant $k$ and input size $n$.

## Reductions
A **reduction** is defined as follows. $R$ can be reduced to problem $Q$ if there is a polynomial-time computable function $f:\{0,1\}^*\implies\{0,1\}^*$ such that all instances $J$ of $R$  we have 
$$R(I)=1 \hspace{30pt} Q(f(I))=1$$
That is $R$ and $Q\circ f$ apply the same function. So we a problem to another problem that can be solved in polynomial time. This means $R$ is not harder (**in the sense of polynomial-time computation**) than $Q$. We need $R(x)\iff Q(f(I))$ otherwise we aren't solving $I$ in the sense of $R$. The $f$ function must be able to travel in both directions $\iff$ they should always give the same answer for the same problem. If $f$ is polynomial then the $f(I)$ problem is of size at most polynomial to that of $I$. Then since $Q$ solves in polynomial time and we can compose two polynomial times together to get another polynomial time. A viable algorithm for $R$ is to apply the algorithm for $f$ and then the one for $Q$ which together will run in polynomial time. 

The reason it is $\le_p$ and not $=_p$ is as we could be making $R$ harder than it needs to be like we could instead of **reducing** it be **raising** it. But it also means that for $R$ it must no harder than $Q$.

## Meaning of $R\le_PQ$ 
If we could solve problem $Q$ in polynomial-time, then I would also be able to solve $R$ in polynomial time given the function $f$ works in polynomial time. So if $R$ and $Q$ are reducible and one of them is **P** the are both **P**.

If we can reduce $R$ to $Q$ with polynomial $f$ and $R$ is **NP-complete**. This is since by definition of **NP-completeness** we can find some $g$ to reduce any **NP problem** $H$ to $R$ but then we can apply $f\circ g$ to $H$ so a problem that is solved in $R$ so if $R$ was **P** it would make $H$ **P** hence $R$ must be **NP**. That is or all **NP** are really **P**! But $Q$ must also be **NP-complete** as any function in that is **NP-complete** can also be reduced to $Q$.

## NP-Completeness
A problem $Q$ is **NP-complete** if it is **NP** and it is also true that every problem $R$ in **NP** we have $R\le_PQ$ (for $Q$ in **NP**) so $R$ reduces to $Q$. Then if $Q$ can be solved in **P** time so can all of **NP**. There is always a polynomial time reduction from a $R$ to $Q$. Hence if $R$ was solved they all would be. If we have two **NP-complete** problems then they can both be reduced to each other as they are both **NP**. Hence solving one solves them all.

The first problem solved was **SAT** **satisfiability** proof. Then we can just prove some other problem is **NP-complete** by showing some **NP-complete** problem can be reduced to it. Hence now all **NP-complete** can be reduced by chaining to our new problem.

So the first **NP-complete** was the hardest proof as all **NP** problems had to be shown to be solved by it. But any new **NP-problem** can be proved by showing the first **NP-complete** problem can be reduced to the new problem. We can also new use any **NP-complete** problem as we can reduce it to any other problem we have that must also be **NP-complete**.

## Satisfiability (SAT)
This is the problem in **propositional logic** where we have a collection of **propositional variables**. Then we reduce any logical statement to **CNF** so in this form we have a **conjunction** of **clauses** where each **clause** is a **disjunction** of **literals**, each **literal** is either a **negation of a propositional variable** or a **propositional variable**. For some **CNF** $\Phi$ we want to know if it can be satisfied meaning is there some combination of **logical variable** values that makes the whole **CNF** true. There will be $2^n$ combinations for $n$ logical variables. Each possible combination will possible solve some **CNF**. We can have up to **n** literals in a clause. There is also $k$ **CNF** where each **clause** has $k$ literals this is called $k$-SAT. The problem is 

![[Pasted image 20220214112336.png]]

This was the hardest **NP-complete** problem to prove as it had to be proved that every **NP** problem can reduce to **SAT**. Each of the **NP** problems must have some verifier that takes **Polynomial time** to check some solution. We can think of a solution to **CNF** as finding a certificate that proves it can be solved. The certificate has assignments for each logical variable and this can be checked in polynomial time against the problem length. We can write a **CNF** formula that verifies that some certificate does exist for a problem and we can make this certificate in polynomial time. So if we can solve **SAT** in polynomial time we can chain these two steps together and solve any **NP-problem** in polynomial time. **SAT** also had to be proved to be **NP** but to check **SAT** we need to enumerate over all variable in $O(2^n)$ time. The proof shows if we have some verifier that takes **NP** time we can enumerate over all possible certificates in **NP** time. So since this whole enumeration can be solved by a **SAT** if **SAT** is **P** so is all **NP**.

It could be that there is a polynomial solution to **NP** complete so it is the same as **P**. So either they are all **NP** or they are all **P**. But it has never been proven that **NP-complete** is **P**.

## Independent Sets
This is involved with the **independent set** problem. An **independent set** is a subset $I\subseteq V$ such that for every pair $u,v \in I, (u,v)\notin E$ . That is its a subset of the vertices sin a graph that aren't connected. So we need to prove for all pairs in $I$ that there is no edge $(u,v)$.

The problem is finding for some number $k\in\textbf{N}$, determine whether for some undirected graph $G=(V,E)$ whether $G$ has and **independent set** of size $k$.

We know a verifier can just enumerate over all pairs of vertices an check if there is an edge. So it is **NP** so we can solve this with **SAT**. Another **NP-complete problem** is **3-SAT** (SAT made out of CNF with clauses with 3 literals)we will prove **3-SAT** can be reduced to **independent sets**.

We can find out if an independent sets problem is solved in **NP** time. We need to prove any **3-SAT** problem can be reduced to an **independent set problem** that is a solution to the equivalent **independent set** problem guarantees there is a solution to the **3-SAT** problem.

So take a **3-SAT** problem. Then it will be made out of 3 literal clauses. For each clause we can make a triangle in our graph so in an independent set only one of these literals will be included. There will be $m$ triangles, each one can have only 1 vertex included in an independent set, so if there are $m$ independent vertices then there must be one literal we can make true in every clause, so there is a solution. All these vertices can be labeled as the literal they correspond to. Then we also know in a solution a literal and its negation cannot both be true so we connect these with an edge. If there is a solution to this graph with $m$ vertices there is a solution to the **3-SAT**. Not also that if there is more that one literal true in a **3-SAT** solution then our solution wouldn't capture this. But this would correspond to $>m$ vertices. If we can make the **3-SAT** true with less that this then it doesn't matter if more truth values are added it must be solvable. The extra solutions. 

Then we just need to show we can make this construction in polynomial time. We made a number of nodes that too $3m$ nodes. Then we added $3m$ edges. Then in the worst case there would be a blocking edge between vertices would be $3*\frac{m^2-m}{2}$ giving us $3m^2/2$ time. We could add all the triangles in $m$ time then if we could check all clashing pairs in $m^2$ time. Hence $3-SAT\le_P IndependentSet$.

[[P and NP Questions]]