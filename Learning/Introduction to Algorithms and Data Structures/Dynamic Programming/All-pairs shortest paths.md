# All-pairs shortest paths
We want for every pair of vertices $u$ and $v$ with a weighted graph and we want to find the shortest path values (negative weights are allowed, but no negative cycles that is a cycle whose total weight is negative).
![[Pasted image 20220126121156.png]]
We know that without negatives loops it only makes sense to at most hit each vertex once in the shortest path so $n-1$ points in a path. As if there was a loop you could cut it out and reduce the distance or make no difference. S  o a vertex can only be in the graph one.

## Floyd-Warshall Algorithm
We will work with a pool of points with paths calculated for all points in.
![[Pasted image 20220126122207.png]]
So $k$ will be increased slowly to $n+1$. So $k$ is the number of vertices allowed in a path from $i$ to $j$ and we for every $i$, $j$ slowly add vertices in until we have the full path. We are calculating $D^{<k+1}$ from $D^{<k}$. Here $d_p=\sum_i^pw(e_i)$. $V_k$ starts empty but we slowly add in relaxing the graph. We are basically building up a path slowly for each pair by slowly adding vertices from the overall group.

If we note for any path from $i$ to $j$ in the one $D^{<k}$ ($D^{<k}[i,j]$) each path can at most have $k$ in it once when we move to $D^{<k+1}$. So there are two cases either $k$ isn't used in which case it is the same as before ($D^{<k+1}[i,j]=D^{<k}[i,j]$) or it is used once in which case $D^{<k+1}[i,j]=D^{<k}[i,k]+D^{<k}[k,j]$ (note its not a strictly allowed vertex but can be used here as an endpoint). Hence $D^{<k+1}[i,j]=min(D^{<k}[i,k]+D^{<k}[k,j], D^{<k}[i,j])$. This given the recurrence relation
![[Pasted image 20220126150152.png]]
The $D$ matrix of $d$ values for the path between the $i$, $j$ vertices.
![[Pasted image 20220126151524.png]]
The base case is needed as for it there is no previous generated distances and there are only edges.

## Code
![[Pasted image 20220126152013.png]]

In practice we could just keep two arrays $D^{\textrm{curr}}$ and $D^{\textrm{next}}$. This is made possible by the recursion only going down one level. So this allows saving in space-complexity. This can be updated to find paths by making the following changes
![[Pasted image 20220126152746.png]]
The $\Pi$ array stores the index to the next vertex in the shortest path from $i$ to $j$ then it can be seen that this array will also then contain the path from the next vertex to $j$ also. $\Pi$ is then called the predecessor array. It can also be $null$ if there is no path from $i$ to $j$.

## Runtime
We can note the first part (1) will take $O(n^2)4$ time. Then the triple loop will do work for $n+1$ by $n$ by $n$ by $O(1)$ hence since the time incise takes constant time it will take $O(n^3)$ time. Then since we will have to do these loops no matter what it will take $\Theta(n^3)$ overall.
