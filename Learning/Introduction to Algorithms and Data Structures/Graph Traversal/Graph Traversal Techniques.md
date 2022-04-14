# Graph Traversal Techniques
Graph traversal techniques change the order in which a graph is explored this gives different properties to the nodes explored first and which one we use will depend on what our task is.

There are two flavors of graphs **directed** and **undirected**. In directed we can only explore in one direction for a given edge while in directed we can explore in either direction. We consider a graph **connected** if for any nodes $A$ and $B$ there is a path between them. A **sink** is a node which edges only flow into and  so it can never reach any other node.

## Storing Graphs
The way we store a graph will change the asymptotic properties of how that graph works. These results are gleams through [[Asymptotic Analysis]] of the data structures and access algorithms used.

**Adjacency Matrix** -> This is a data structure where we have for $n$ nodes a $n\times n$ matrix of binary values (other values can be used in the case of an unweighted graph). To look up a edge for a node $a$ to some $b$ we simply index in the matrix taking $O(1)$ time.
![[Pasted image 20220206121734.png]]