# Graphs
A graph is a mathematical structure consisting of a set of vertices and a set of edges. That is with a set of vertices $V$ and a set of edges $E$. For a graph $G$ we have $G=(V,E)$. Th edges are tuples that is $E\subseteq V\times V$. If the graph is undirected the $(v,w)\in E\iff (w,v)\in E$. But this isn't the case in a undirected graph.

There are two main ways of representing a graph as a data structure for a computer to understand. 

An *adjacency matrix* here we have an $n\times n$ matrix for $n$ vertices, we call this matrix $A=[a_{ij}]$. Then if $a_{ij}=1$ it means there is an edge from $i$ to $j$. Of course a undirected graph will have a symmetric $A$.

![[Pasted image 20220428113524.png]]

An *adjacency list* stores for each vertex a list of elements it is adjacent to. That is there is an edge from the list owner to the vertex in the list. A vertex with no edges leading away will have an empty list. 

![[Pasted image 20220428113632.png]]

The two data structures have different run-times. 

![[Pasted image 20220428114227.png]]

Where $n$ is the number of vertices and $m$ is the number of edges. $m$ will always be smaller than $n^2$ as this is the number of elements in $V \times V$.

A *planer graph* is a graph that can be laid out on a 2d surface such that edges only touch at their endpoints. That is the edge lines don't overlap.

A *traversal* is a strategy for visiting all vertices of a graph. There are two main types [[Breadth-First Search]] and [[Depth-First Search]]. ([[Graph Traversal Techniques]])

[[Graphs Questions]]