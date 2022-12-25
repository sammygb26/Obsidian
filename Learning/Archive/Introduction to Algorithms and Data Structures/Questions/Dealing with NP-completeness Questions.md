What is a vertex cover? #flashcard #IADS #ComputabilityTheory 
	The problem is given a graph to find the minimum sized set that touches every edge.

---
How might we find an approximate solution to vertex cover? #flashcard #IADS #ComputabilityTheory 
	To find an approximate solution we can remove an edge at a time removing all vertices from it and adding them to out cover. We can then remove all edges connecting to these vertices.

---
Why is approximate vertex cover never worse in size than double the optimal solution? #flashcard #IADS #ComputabilityTheory 
	For every edge we consider at least one of its edges with be in the optimal cover (by definition of the cover). The set of purple edges we add never share any edges so can never be greater in size than the cover as if it was the best cover wouldn't have enough vertices to cover all these edges. Since each edge has two endpoints added the $|C|\le2|C^*|$

---
What is the Max-3-sat problem and why must it be NP? #flashcard #IADS #ComputabilityTheory 
	Here we are given a formula of $m$ clauses. We have to find the maximum number such that an assignment of binary values makes $k$ clauses out of the $m$ true. This must be NP as if it were we could set $k=m$ and solve 3SAT in P time.

---
Why is there a $\frac78$ ratio of 3-Sat clauses being satisfied within some formula $\phi$? #flashcard #IADS #ComputabilityTheory
	We can note all the clauses in $\phi$ are made out of 3 clauses hence if we assign them all randomly there will be a $\frac12\frac12\frac12=\frac18$ chance of it being false. Hence overall each clause has a $\frac78$ chance of being right. All that remains is to de randomize this to ensure we always meat this.

---
How can we de-randomize that $\frac78$ sat solutions? #flashcard #IADS #ComputabilityTheory 
	If $Y$ is the expected number of clauses satisfied then $E(Y)=\frac78$. But this remains true if we assign values to some $x_i$ in $Y$. That is $E[Y]=\frac{E[Y|x_j=1]+E[Y|x_j=0]}2$. But if $E(Y)=\frac78$ then either both the $x+j$ assignments make the expected value the same or one is larger and one is smaller. If we continue doing this we can ensure we pick a sample that has $Y\ge\frac78$ .

---
What is exhaustive backtracking? #flashcard #IADS #ComputabilityTheory 
	This is an algorithm to find solutions to SAT the idea is we assign values as we go each time there is a choice we split. Whenever we find a solution we return it and are done but if we don't find a solution we trace back up to our last solution and try again.

---
What are heuristics and how do they help with backtracking search? #flashcard #IADS #ComputabilityTheory 
	Heuristics can be used to guide our search to assigning variables and choosing values that will maximize the chance of finding a solution. These cause in the best case a drastic increase in the speed of solutions found.

---
What is DPLL and how does it work? #flashcard #IADS #ComputabilityTheory 
	DPLL can solve SAT problems when applied to CNF formulae. It work by using a unit clause and pure literal heuristic to guide the assignment of variables. This means if we find variable which is either positive everywhere or negative everywhere we can make it true or false respectively. And if we find a clause that has just want literal we must set it to true.

---
