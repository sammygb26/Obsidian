
What is informed search? #flashcard #RA #InformedSearch
	Informed search is a search strategy where we  order frontier nodes based on an evaluation function that is an estimate of how desirable they are.

---

What is best first search? #flashcard #RA #InformedSearch 
	Here we have an evaluation function that is equal to a heuristic calculated for each node f(n)=h(n). An example of this heuristic could be distance to our goal state.

---

What are the properties of best first search? #flashcard #RA #InformedSearch
	It could get stuck in an infinite loop so it isn't complete. It could be mislead so time complexity in the worst case is $O(b^m)$. Then it might expand all the frontier before it finds the right path so spatial complexity would be $O(b^m)$. Its not optimal since it may get mislead by its heuristic to find a suboptimal solution.

---

What is A* search? #flashcard #RA #InformedSearch
	Here we have an evaluation function that is equal to some heuristic plus the cost to get to that node we are evaluating $f(n)=g(n)+h(n)$.

---
What are the properties of A* search? #question #RA #InformedSearch
	A* is complete unless there are infinitary many nodes where f < f(G), this can happen when we have an action cost of 0. It has a time-complexity of $O(b^m)$ but only in the worst case. Then it has space-complexity of $O(b^m)$ since it could explore all other nodes first but this is the worst case. Then it will always find an optimal solution if the heuristic is admissible.

---

What is an admissible heuristic? #flashcard #RA #InformedSearch
	A heuristic is admissible if for every node the heuristic is smaller than the actual distance to a goal state. This ensures that A* search will find the most optimal solution.

---

What is heuristic dominance with A* search? #flashcard #RA #InformedSearch
	This is the effect that if we have two admissible heuristic the the one which will perform better will be the greater one as it will be closest to the true cost.

---
