# Breadth-Frist Search
This is a [[Graph]] exploration technique/algorithm where we explore a graph from a starting node spreading out exploring the nodes closest to our starting node first and the ones deeper later. This can work for either directed or undirected graphs. We only concern ourselves with the $\textrm{in}(v)$ and $\textrm{out}(v)$ which gives the nodes that lead to a node and the ones that it leads to.
![[Pasted image 20220206120218.png]]
This is the basic BFS algorithm along with the below helper function.
![[Pasted image 20220206120256.png]]
The breadth first effect is given by the use of a queue where the nodes we find first are expanded first.