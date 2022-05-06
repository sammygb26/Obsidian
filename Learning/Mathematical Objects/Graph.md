# Graph
A graph is a mathematical object made out of two [[Set]]s the vertices and the edges. The vertices can be thought of as the set of points within the graph and the edges the conations between them. 

## Undirected Graph
In the simples of graphs say a graph $G$ will be made out of 2 sets $V$ and $E$ for vertices and edges. The elements of $V$ will be a number of symbols $v\in V$. Then $E$'s elements will be a number of sets $e$ containing 1 or 2 symbols in $V$. That is $e=\{x, y\}$ where $x, y \in V$ or $e=\{x\}$. In this case we say for two vertices $x$ and $y$ if $\{x, y\} \in E$ then $x$ and $y$ are *adjacent*. If two edges exist $a=\{{x,y}\}$ and $\{b={x,y}\}$ then $a$ and $b$ are parallel. An edge containing only one symbol is called a *loop*. Then an vertices with no connections is called *isolated*.
![[Pasted image 20220119134633.png]]
Here $V=\{1,2,3,4,5,6\}$ and $E=\{\{1,2\}, \{1,5\}, \{2,3\}, \{2,5\}, \{3,4\}, \{4,5\}, \{4,6\}\}$.

## Directed Graph
This type has a set of vertices $V$ and a set of edges $E$ but the $e$ themselves are ordered [[Tuple]]s instead of [[Set]]s. That is for an edge $e\in E$, $e=(x,y)$ for $x, y\in V$ then $e$ is an edge from $x$ to $y$.
![[Pasted image 20220119134649.png]]
## Weighted Graph
A graph is weighted when for each edge we also specify a wight to that edge. This can be useful to specify a cost for traversing a given path. Like for example in a road network we might want to specify the cost in time of moving down a road. A weight can be specified by a *weight function* $w: E \to R$.
