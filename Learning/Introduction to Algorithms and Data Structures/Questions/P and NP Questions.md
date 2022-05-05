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
