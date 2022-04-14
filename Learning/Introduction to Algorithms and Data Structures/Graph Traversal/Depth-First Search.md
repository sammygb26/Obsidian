# Depth-First Search
This is a [[Graph]] exploration technique/algorithm where we explore a graph from a starting node by exploring the nodes we have found most recently first. This can work for either directed or undirected graphs. We only concern ourselves with the $\textrm{in}(v)$ and $\textrm{out}(v)$ which gives the nodes that lead to a node and the ones that it leads to.
![[Pasted image 20220206120626.png]]
This is a simple DFS algorithm along with the helper function below.
![[Pasted image 20220206120652.png]]
The behavior of depth-first search is implemented with the use of a stack where the item last added is first used.