What does **P** and **NP** mean? #flashcard #IADS #PnNP
	**P** is the set of problem for which there exists some algorithm that will solve problem instances in *polynomial* time. **NP** is *non-deterministic polynomial* we can non-deterministically solve the problem in polynomial time that is given a solution we can verify it is a solution in polynomial time. So **P** is a subset of **NP** since if we can solve a problem instance in polynomial time we can defiantly also verify that same answer.

---
What are decision problems? #flashcard #IADS #PnNP
	Here the answer is a simple yes or no for example does there exist a Hamilton Cycle I a particular graph. The answer is a 1 if there is and 0 if not. 

---
What is the **complexity** of a problem? #flashcard #IADS #PnNP
	the complexity of a problem is through of as the complexity (time or space) of the algorithms used to solve that problem. There is not complete proof any complexity for a problem is the best solution we may have just not found the true solution.

---
What is a **reduction**? #flashcard #IADS #PnNP
	A reduction occurs when we can find a polynomial time function that takes a problem instance for some $R$ and reduces it to a problem for some $Q$ but they always give the same answer. This way if $Q$ is solvable in *polynomial* time then so is $R$ as we can make a new polynomial time algorithm that is the composition of $f$ and $Q$.

---
What does $R\le_P Q$ mean? #flashcard #IADS #PnNP
	This means $R$ is no more complex polynomial then $Q$ that is $R$ can be reduced to $Q$ polynomials so if $Q$ is polynomial so is $R$. But equally if $R$ is **NP-complete** then so must $Q$ be or there is a **P** solution to **NP**.

---
What does it mean to be **NP-complete**? #flashcard #IADS #PnNP
	Something is **NP-complete** when all **NP** problems can be reduced to it. This was first proven for SAT and then after that if SAT can be reduced to some other problem type then by extension there is a reduction form any **NP** to this other problem so it must be in **NP**.

---
What is the satisfiability **SAT** problem? #flashcard #IADS #PnNP
	**SAT** is a decision problem where the instance is a set of propositional variables connected with negations conjugations and disjunctions. The answer should be 1 when there is some combination of assignments to the propositional variables that makes the whole expression true.

---
Why is SAT **NP**? #flashcard #IADS #PnNP
	**SAT** must be NP as if we are given some combination of propositional variable assignment to ($\top$ and $\bot$) then it will take time proportional to the length of the input sequence to find out what the final value is. This can be done character by character hence is polynomial bounded.

---
How can we make a 2 variable clause into 3CNF? #flashcard #IADS #PnNP 
	A 2 variable clause will be of the form $C_k=(l_1\lor l_2)$ we can replace this with two 3-CNF clauses adding in a dummy variables $y_k$ this will give $C_{k1}^*=(l_1\lor l_2\lor y_k)$ and $C_{k2}^*=(l_1\lor l_2\lor \bar{y_k})$. This way no matter the value of $y_k$, $(l_1\lor l_2)$ has to be true just as with the original clause.

---
How can we make a k clause with k>4 variable into a 3CNF form? #flashcard #IADS #PnNP 
	We will introduce $k-3$ dummy variables $y_1,y_2,...,y_{k-3}$ for this. Then we will make $k-2$ clauses as follows. We make $C_1=(l_1\lor l_2\lor y_1)$ then $C_2=(\bar{y_1}\lor l_3\lor y_2)$ and in general for $2\le j\le k-3$  we have $C_j=(\bar{y_{j-1}}\lor l_{j+1}\lor y_j)$ and $C_{k-2}=(\bar{y_{k-3}}\lor l_{k-1}\lor l_k)$. This way if we have all dummies true then one of the last two variables must be true and if all dummies are false then the first two variables must be true. For any combination of assignment for the variables any true variable followed by a false one will leave some literal needing to be true. Hence no matter the assignment we will need to make at least one literal true just as in the original clause.

---
How can 3-SAT be encoded as a vertex cover problem? #flashcard #IADS #PnNP 
	We can make a vertex for every positive and negative literal in each clause. So for 6 clauses we will have 3 * 6 = 18 literals. For each clause we make a triangle this way the minimum vertex cover must have one vertex from each triangle. We can then make edges between all the negated literals this way ensuring either $a$ is true or $\bar a$ is true.

---
