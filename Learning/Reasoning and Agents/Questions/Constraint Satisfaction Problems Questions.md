What parts make up a Constrain Satisfaction Problem or CSP, and what defines a solution to one? #question 
	CSPs are made out of three main parts a set of **variables**, a set of **domains** possible values the variables can have, and a set of **constraints** which have a scope and a relation. They define conditions that must be met between variables in the scope to have a valid CSP solution. A solution being just a set of assignments for the variables that fulfills all constraints simultaneously.

---
What is a binary CSP? #question 
	A binary CSP is a CSP where all the relations are binary relations that is the size of their scope is two variables.

---
How is basic search done in a CSP problem and what are the types of consistency? #question 
	We need to have **node consistency** and **arc consistency**. That is all the variables need to be some value satisfying the constraints on them while also allowing the constraints on all their neighbors that are related to them by some constrains. This means when we search we can do two things. Pick a value for a variable or reduce the possible domain of a variable. We keep doing this until we have to backtrack or we find a solution. 

---
How does the AC-3 algorithm work? #question 
	AC-3 wants arc consistency for all values, it works on a binary CSP. The way it achieves this is it check over all arcs between two variables. If there is a reduction in the domain of a variable we check all variables with cars to it as they in turn may need their domains updated. This continues until we either reach a variable that has no domain (inconsistency), we have to branch or we find a solution.

---
What is the simplest approach to CSP search? #question 
	Backtracking search is the most simple approach to finding a solution to a CSP. For a node we simply pick and new value for a random variable that hasn't been picked before. If we ever find an inconsistent assignment we go back to the last choice we did that has some choice we haven't made yet. We take this and then repeat until we either try all possible assignment or find some complete consistent assignment.

---
What is forward checking? #question 
	Forward checking is where for every assignment we make in a backtracking search we remove all possible choices form domains that are inconsistent with this choice. That is we now will never make a choice that make an immediate inconsistency.

---
What is the MRV and LCV heuristic? #question 
	These heuristics apply to a backtracking based search.
	**MRV** is  "Most Constrained Variable" and it tells us to choose the next variable to assigned as the one with fewest possible choices. The logic being that we want to be wrong the least number of times higher in the search tree. As the more back tracks we have to make to any point the more we have to repeated the choices bellow.
	**LCV** is least constraining value. It means we pick the value for our variable to be the one that will reduce the domains of remaining variables the least.