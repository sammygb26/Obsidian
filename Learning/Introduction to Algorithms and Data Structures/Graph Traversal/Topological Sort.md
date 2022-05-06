This is a task in which we are given a list of constraints on the order of some tasks. For example

![[Pasted image 20220428203537.png]]

We can set this up as a directed graph problem. We define the *topological order* of a graph to be a linear order of the vertices such that the direction of the edges is all in the same direction. The exact order doesn't matter but we constrain that some tasks must happen at some point before others. There can be many *topological orders* for some graphs. We can modify [[Depth-First Search]] to solve this problem.

![[Pasted image 20220428203729.png]]

We want to know which graphs have topological orders. If a graph has a cycle then it cannot have a topological order as every vertex of the cycle will have to be moth ahead an behind the other members of the cycle. These are called *directed acyclic graphs* and they all have some topological order. 

For this algorithm we will explore the graph in a depth first manor. We can mark vertices white if they aren't visited, grey if they are visited but we haven't finished their exploration and black if we have fully explored them (when the depth exploration returns). 

If we consider some moment during the execution of $dfsFromVertex(G,v)$
If some $w$ is white and reachable from $v$ then $w$ will be black before $v$ as its exploration will terminate before $v$'s. Then if $w$ is grey, then $v$ is reachable from $w$ as $v$ is being explored from $w$ (this would mean there is a cycle). If we make the order such that $v\prec w$ is when $w$ becomes black before $v$.

![[Pasted image 20220428210621.png]]

This is the algorithm that ensures that for a single vertex. We can combines this with the bellow algorithm to get a full topological sort for a function.

![[Pasted image 20220428210526.png]]

[[Graphs Questions]]