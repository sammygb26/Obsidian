# Dijkstra's [[Algorithm]]
This algorithm is concerned with a type of [[Graph]] called a weighted graph. An example of a weighted graph might be a road network where the weight of an edge (road) is the length of the edge. The weight is given by a *weight function* $w: \{x, y\} \to R$ For this [[Algorithm]] we aren't just asking the shortest path to a vertex from another vertex but instead the shortest path from every vertex to a given vertex. This algorithm assumes there are no negative weights on the paths [[Bellman-Ford Algorithm]] would be used instead.

## How it Works
We start from some vertex $s$ and we are calculating all the shortest path to every vertex in the [[Graph]] from this vertex. We keep track of all the **frontier vertices** which are vertices connected to vertices in $S$ the set of all vertices we have already found the shortest path to. We then add the vertex whose length to some vertex in $S$ plus that vertex's length to $s$ is the smallest to $S$ with the path to this new node being the path to the node in $S$ who is connect to it with the shortest path length.

This makes this a [[Greedy Algorithm]] since it always adds the best path it can find and doesn't look ahead this works out for this problem but not if we consider negative weights.

We can use [[Breadth-First Search]] to traverse an unweighted graph in the shortest path we just count the number of edges. Since with this algorithm we will find every vertex from the shortest path (since we always explore the adjacent edges first). 

## Proof of Correctness
**Specification**: The inputs will be a Graph $G = (V,E)$, weight function $w: E\to R^+$ (no negative weights) and $s \in V$ a source vertex. The outputs will be two arrays $d$ and $\pi$ of length $n=|V|$. $d[v]$ to hold the shortest-path distance $\delta(s,v)$ from $s$ to $v$, $\pi[v]$ to be $v$'s predecessor along that shortest path.

#### Steps
1. **Initialize** all $d[v]\leftarrow\infty$, $\pi [v] \leftarrow \textrm{nil}$ for all $v \in V$
2. **Initialize** $S\leftarrow\{s\}$, $d[s]\leftarrow0$.
3. *while* $S$ still has fringe edges, we update as follows:
	1. Consider the current *fringe edges* $(u,v)\in E$ with $u\in S$ with $v \in V-S$
	2. We find $v^*\in V-S$ which is the *fringe vertex* with *minimum* $d[u^*]+w(u^*,v^*)$ looking over all fringe edges.
	3. Assign $d[v^*]\leftarrow d[u^*]+w(u^*,v^*)$, the update $\pi[v^*]\leftarrow u^*$ and $S\leftarrow S\cup\{v^*\}$
	
	*This can at most happen $n-1$ times since at this point all points will be in $S$ so there will be no fringe edges*

#### Proof
We will use [[Proof by Induction]]. So we must prove the *claim* for every $u\in S$, $d[u]$ contains the shortest path value $\delta(s,u)$ in $G$ and $\pi[u]$ is the predecessor vertex to $u$ along a shortest path (there could be multiple). 

**Base case**: after initialization since $S$ only has $s$ in it then $d[s]=0$ and this is accurate since $\delta(s,s)$ will always be 0.

**Induction step**: We suppose that the claim hold for some $S$, and that $S$ has fringe edges. We look at the minimum distance edge $(u^*,v^*)$ from $S$. We would have a problem if for some other path the total distance $\delta(s,v^*)<d(u^*)+w(u^*,v^*)$.

This path p must leave $S$ at some point since out of all the edge case from $S$, $(u^*,v^*)$ is the best. Therefore there is some $(\hat{u}, x)$ which is the first time this path p crosses out of $S$. Now since $w(x,y)\ge 0, \forall x, y \in V$ the path length from $x$ to $v^*$ is $\ge 0$ so the length up to $x$ must be smaller than the minimum length to $v^*$ that is $d(\hat{u})+w(\hat{u},x)\le \delta(s,v^*)$ but this would mean $d(\hat{u})+w(\hat{u},x)<d(u^*)+w(u^*,v^*)$ but $x$ is a *fringe vertex* so this cannot be the case since the shortest path to a fringe vertex is to $v^*$ therefore we have a **contradiction** so there is no path to $v^*$ smaller than $d(u^*)+w(u^*,v^*)$

Another way of saying that simple is for there to be a better path there would need to be a way to get to $v^*$ in a better way that comes from a point not in $S$ since we have already check all points in $S$ connected to $v^*$. But then we would have to leave $S$ to do so and so there is some smaller path out of $S$ than the path we found. This is the contradiction.

## Recovering Shortest Path
**Helping Facts**: 
	* No shortest path from $s$ to any $v$ will contain a cycle; this is since if there is one it could be removed and the path would at least be the same length.
	* Every shortest path has at most $n-1$ edges; this is since if there are no cycles and a path can at most go through all vertices then there are $n$ vertices and so $n-1$ edges between them.
	* If $p=v_0,v_1,...v_k$ is the shortest path to $v_k$ then if $p=v_1,v_1,...v_i$ is a prefix of this path then it is the shortest path to $v_i$. This is since if it weren't the shortest path to $v_i$ we could replace this section of the path to $v_k$ with the shorter one hence the path to $v_k$!

The third point above means for some point $v_k$ it's path will end with $\pi(v_k)\to v_k$. But we know the path to $\pi(v_k)$ is a prefix of this path which will by the same logic end in $\pi(\pi(v_k))\to\pi(v_k)$. Extending this we can build the path backwards by recursively querying $\pi$ until we  reach $s$.

## Efficient Implementation
For an efficient implementation we just have to be able to find the next path to add quickly. The way this is done is through the use of a min-[[Heap]]. We keep a heap of the *fringe vertices* which are adjacent to vertices in $S$ but not in $S$. The value by which we store them is the distance of the current shortest path to them. We may have to **reduce** this value if we explore a vertex adjacent to a *fringe vertex* that offers a shorter path to it. However is find as it will only move up our min heap so will at most take the depth of the heap $ln(n)$ time at the most.

#### Helper functions
Initialization is simple we just have to make sure we are setting up the algorithm in a way that maintains the loop invariant. All the distances are initialized to $\infty$ which comes in useful later.

![[Pasted image 20220119180402.png]]

Relax is just for when we add some vertex $u$ then for all adjacent $v \notin S$ we need either add new fringe vertices to our heap or reduce existing vertices.

![[Pasted image 20220119180530.png]]

Then the implementation is just initializing, inserting $s$ and setting the min distance to it to be 0. We then put it in as a fringe vertex and while we still have fringe vertices we pop of the min from the heap then for adjacent vertices we relax the system.

![[Pasted image 20220119181012.png]]

#### Min-[[Heap]]s
This all relies on min-heaps their properties when it comes to [[Asymptotic Analysis]] are the same as a max-heap. The only thing of note is reduce which takes in a element of the heap and a new value for it. If we are reducing a value in a min-heap however it must move up the heap not down. So this can at most take the depth of the heap which is $ln(n)$.

![[Pasted image 20220119181334.png]]

#### Running-time [[Asymptotic Analysis]]
Initialization will take $O(n)$ time at most since it is initializing arrays of size $n$. Then setting up the heap with initial values is done for one item ones so takes $O(1)$ time. We know a vertex $v$ can only be added to the heap once since $d(v)$ must be $\infty$ for this to happen but it is immediately changed afterwards. Since $v$ is only added once it can only be removed once as well. Each time some $v$ is added it can take at most $O(lg(n))$ time since we are inserting it into a heap. Then relax (not counting insert items) will take $O(1)+T_\textrm{reduce}=O(1)+O(lg(n))$. Since we only call relax once per vertex since we only call it when the endpoint of a vertex joins $S$. So all the reduce times will take $O(m lg(n))$ time. So the overall time is 
$$
O((n+m)(1+lg(n)))
$$

[[Dijkstra's Algorithm Questions]]
