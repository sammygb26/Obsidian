What is a graph? #flashcard #IADS #Graphs
	A graph is a mathematical objects made up of two sets. A set of vertices $V$ and a set of edges $E$. The set of vertices being a subset of the cross of the vertices ($V\times V$)

---
What are the two ways to store a graph in memory? #flashcard #IADS #Graphs 
	The two ways to store a graph in memory are an **adjacency matrix** and an **adjacency list**. The matrix for $n$ vertices is a $n\times n$ matrix where the $i,j$ cell being a 1 means there is an edge from $i$ to $j$. The list way for $n$ vertices has $n$ lists. Each $i$th list contains all the with an edge from $i$ to them.

---
What are the asymptotic properties of an adjacency list? #flashcard #IADS #Graphs 
	An **adjacency list** takes for a vertex $i$ $\Theta(out(i))$ to find if an edge exists between it and some edge. It also takes time $\Theta(out(i))$ to visit all edges out from it. The amount of space taken up is $\Theta(n+m)$ for $m$ edges. Then its also $\Theta(n^2)$ to visit all edges.
	An **adjacency matrix** takes \Theta(n^2) space to store. It takes time $\Theta(1)$ to check if there is an edge between two vertices. It takes $\Theta(n)$ to visit all edges out. It takes $\Theta(n^2)$ to visit all edges.

---
What is traversal of a graph? #flashcard #IADS #Graphs 
	This is a strategy for visiting all the vertices of a graph. The two main ones are breadth first search and depth first search.

---
How does breadth first search work? #flashcard #IADS #Graphs 
	The idea is to use a use a last in first out queue to order which vertices are explored first. This has the effect that we explore all vertices rom a single node before looking at what next to do.

---
How does depth first search work? #flashcard #IADS #Graphs 
	Depth first search works by using a first in first out stack to order which vertices are explored first. This has the effect the we completely explore a subtree before moving onto the next node.

---
What is a topological sort? #flashcard #IADS #Graphs 
	A topological sort is a description of a problem where we have many ordering constraints on elements. We need to find a sequence of elements such that all the constraints are satisficed.

---
How can topological sort be viewed as a graph solutions and what does this make the solution? #flashcard #IADS #Graphs
	If we take each element we want to sort as the vertices of a graph then we can have directed edges in place of constraints. In this case a solution would be a placement of all the vertices in a line such that all the edges pointed in the same direction.

---
How can depth first search be used to solve topological sort problem? #flashcard #IADS #Graphs 
	We can view the problem as a graph with the edges being the constraints on elements. In some traversal of the graph if we find some element that we have already seen in our current traversal then we know there is a loop hence we cannot solve the problem. Otherwise we can add the nodes to the solution in the order we return from their searches. This means the deepest element come last in the solution.

---
