What is tree search? #flashcard #RA 
	This is a way of searching for a solution where we keep track of a changing collection of frontier nodes (different from states since we keep track of details about them) we explore more states from these states through actions until we find the goal state. We can then retrace our steps to get a solution.

---
What are the properties of tree search strategies? #flashcard #RA 
	Completeness -> Does the strategy find the solution
	Time-complexity -> How does the time taken to find a solution compare with the size characteristics of the problem.
	Space-complexity -> How does the space used while finding a solution compare with the size characteristics of the problem.
	Optimality -> Does our strategy find the best solution.

---
What is graph search and why is it needed? #flashcard #RA 
	Graph search is a type of tree search where we ignore state we have already been in this reduces the time and space complexity of our solution since there is no need to visit states we haven't already visited.

---
Explain the differences between BFS, DFS, DLS and IDS? #flashcard #RA 
	First they are Breadth First search, depth first search, depth limited search and iterative deepening search.  BFS searches in a First in First out way this has the effect it explores each state that can be reaches form a a given state then goes on to look at the states that can be reached form the later states. DFS searches in a last in first out way that has the effect it exhausts the all the states that can be reached going from one state to a state that can be reached after that and so on. DLS is DFS but with a limit set so the search is limited to a number of levels below the root of the tree before we turn back. IDS is just a series of DLS searches to deeper and deeper levels until we find the goal.

---
What are the properties of BF, DF, DL, and ID searches? #flashcard #RA 
	![[Pasted image 20220121145629.png]]

---
