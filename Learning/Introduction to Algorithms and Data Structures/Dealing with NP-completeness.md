# Dealing with NP-completeness (Approximation)

## Vertex Cover
We can look at the example of a *vertex cover*. This is a problem in an undirected graph. The idea is to find the minimum sized set that touches every edge. This is an *np-complete* problem. Its easy to see that we can solve this in *NP* time by generating all possible answers. We can look at an approximation algorithm.

![[Pasted image 20220303124229.png]]

The idea is fairly simple we take some set of vertices $C$ then we maintain a set $E'$ of edges not covered. We then take one of these non-covered edges add both vertices $u$ and $v$ and remove all other edges containing the $u$ and $v$. Then we will have some cover by the end. This algorithm must be polynomial since we must take at most $n/2$ iterations as we add two vertices each time. The amount of work done each time is just removing edges taking polynomial time at least.

![[Pasted image 20220303124945.png]]

The purple one are added to the cover, all the edges covered are removed from then (purple and brown edges). So this will give a cover size of 6 (less than optimal).  We will argue this will always return a cover at most twice the optimum.

This is a minimize operation we don't need the exact answer in our approximation $C$ but we may want to bound it relative to some hypothetical cover $C^*$. We argue this by noting for ever edge we consider (made purple) at least one of its edges will be in $C^*$ by the definition of a cover for all edges. But the purple edges can't share endpoints since both their vertices are removed. Hence $|C^*|\ge |F|$ where $F$ is the set of purple edges. Since one or two of each of the purple edges' vertices are in $C^*$ hence at least half of all the vertices are in $C^*$. This is the size of $F$ however. Hence $|C|\le2|C^*|$.

## Max 3-Sat
In Max 3-Sat we are given some formula $\phi=C_1\land...\land C_m$ we want to determine the *maximum* number of clauses $k$ such that there is an assignment of binary values $\{x_1,...,x_n\}$ that makes $k$ clauses satisfied. We don't expect a polynomial time algorithm for 3-Sat since if we did we could use that for $k=m$ to get a polynomial time solution for the whole problem (which is *NP-complete*). The best we can do is **approximate**. We say *find* as we actual find a solution for some $k$. The algorithm will solve for $k=\frac{7}{8}m$ clauses that is we get a $\frac{8}{7}$-approximation for *Max-3-Sat*. We want to show every $\phi$ has an assignment that satisfies $\frac{7}{8}$ clauses hence why we can write the above statement (we will of course have to prove this). Our *problem* is we are trying to satisfy a high number of clauses. Each clause must have at least 3 literals that have different propositional variables hence are completely independent.

If we consider a single clause $C_j=(\mathcal l_{j,1}\lor\mathcal l_{j,4}\lor\mathcal l_{j,3})$ then this clause is satisfied by at least one literal being true. If we randomly assign propositional values to all the different propositional values behind the literals (independently). If this is true then the probability for each literal will be false is $\frac{1}{2}\cdot\frac{1}{2}\cdot\frac{1}{2}=\frac{1}{8}$  for the whole clause. This is due to the setup where each clause must have 3 independent literals. Hence we have $\frac 7 8$ probability of being true. This will make the *expected number* of satisfied clauses in $\phi$ will be $\frac 7 8m$.

If we let $Y_j$ be the binary random variable that $C_j$ is satisfied. Then $Y=\sum_{j=1}^mY_j$ is the number of clauses are satisfied by the assignment. The expected value $E[Y]$ will be $\frac 7 8m$ by *linearity of expectation*. There must be some assignment for $x_1...x_n$ which satisfies $\ge \frac78m$ clauses. This is since $Y$ has a non zero variance hence there will be some value above $\frac78m$. So we could randomly choose values for $x_1...x_n$ until we get a solution $\ge\frac78m$ but this a naïve approach an even though it has a very high probability of finding a solution for some number of guesses it isn't 0 and it could fail.

#### De-Randomized $\ge\frac78$M ALGORITHM
We can look at the expectation of $Y$ given some value of $x$ that is $E[Y]=\frac{E[Y|x_j=1]+E[Y|x_j=0]}2$ but if $E[Y]$ is $\frac78$ then one of the two expectation is greater. So we need to find the $x_j$ values one by one that maximize this percentage. This will change the fixed value sin our 3-Sat but this will make it not longer abide by the 3-Sat conditions. But we only needed this in the beginning to show our expectation hence if we make sure to pick the best expectation we are above $\frac78$ anyways so this doesn't matter.

![[Pasted image 20220303140409.png]]

We can compute the expected values in polynomial time by fixing our already set values and just looping over the remaining clauses (some of which may be changed but we can calculate percentages on a case by case basis). If we reduce the number of clauses we can still assign we can reduce the expected value from $\frac78\to\frac34$ or $\frac34\to\frac12$ or $\frac12\to0$. But we will find these as we go from clause to clause. Hence we can calculate into 

![[Pasted image 20220303141615.png]]

Since we know the sum of the two expectation is greater than $\frac{7}{8}$ then either they are both $\frac78$ or one is higher one is lower. Hence we can pick the higher in this case and maximize the expected value to have to be over $\frac78$. This ends with a good solution $\textbf b$ to maximize the number of satisfied clauses. It has also be shown that if **P** and **NP** are complete then there is no better solution for this algorithm than this one.

One approximation doesn't go for another one in **NP** as the approximation ratios aren't preserved.

# Dealing with NP-completeness (exhaustive search)
Here we want a perfect result but we don't care about solving in polynomial time. We just want algorithms that work in exponential time. Then are there ways that are better than the initial brute force method in this. We will again look at solving SAT.

The basic way we could do this for *SAT* is we would just enumerate over all the options. We set each variable to either 0 or 1 in the case of SAT and so there will be $2^n$ options for out formula that may be solutions. So for each of these assignments we check over our statement and try to find a clause that is unsatisfied. So in the worst case we have to check every clause for each clause every time. In this case to check a formula $\phi$ will take $O(|\phi|)$ to check some $\phi$. But there are $2^n$ assignments so overall it take $O(|\phi|2^n)$.

## Recursive-Backtracking

Another option is *semi-brute force* called *recursive-backtracking*. Here we work with partial assignments as we build up assigning one variable at a time these partial assignments if they make any clause false we know the whole thing false. So we go backtrack to the next choice of random variable that can have another value. This is just a *tree-search* (see in [[Search]])

![[Pasted image 20220307173254.png]]

There are some extra steps we can take to reduce branching in the tree created. These are *unit clauses* where all but one variable in a clause is assigned. So this value must be true hence we should assigned it immediately. Then a *pure literal* is a value that is always positive or negative never both in all clauses (even when we reduce clauses with true values in them) then we should just set it to be always true as all this will never reduce the a clause to 0 in any case so this will reduce branching of our search tree. So we can put in some rules to take care of these cases.

![[Pasted image 20220307174336.png]]

This will give us the *Davis, Putnam, Logemann, Loveland (DPLL)* algorithm. Which takes some extra steps to solve *SAT* as efficiently as possible.

![[Pasted image 20220307174806.png]]

We check if every literal is pure, in this case it is trivial hence we return true. Then if there are any clauses in which we have no values (all the original values are false) so we return false. We then we check for all unit clauses and assign them to their corresponding value. Then we can choose some unbound variable and assign it. This can refer to a *range* of algorithms as this doesn't specify how we choose the next variable to assign. There are 5 main options

1. *Any* we don't pay attention and just pick the first one we can
2. *Variable in most clauses* here we want to have the greatest effect and so reduce the formula the most hopefully to a version we can solve quicker.
3. The variable that has the most slanted *polarity* that is the one that is seen the most in a given polarity hence it reduces the formula the most again.
4. *Any literal in the shortest clause* this basically takes the unit clause approach and we try to solve each clause in as if any clause can't be satisfied the whole thing cant.
5. The variable with the highest weighted sum of clause sizes where smaller clauses have higher weights.

These are all *heuristics* and help speed up but don't guarantee a faster time. *DPLL* is the basic algorithm used in many *SAT* solvers.