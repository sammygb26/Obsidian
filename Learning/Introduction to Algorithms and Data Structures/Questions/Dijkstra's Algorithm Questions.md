What is the aim of Dijkstra's algorithm? #flashcard #IADS #DijkstrasAlgorithm 
	This algorithm attempts to find the shortest path between all nodes and one selected node when this distances of weight between nodes is positive.

---
How does Dijkstra's Algorithm function? #flashcard #IADS #DijkstrasAlgorithm  
	It takes a greedy approach. We expand a set of vertices in the graph we have already found the shortest path to by adding a new vertex that has the next shortest path length to our selected vertex. Where the path length is equal to the length of an edge to some node in the set we have found solutions to plus the path length to the node we are connecting to.

---
What data structure is used to make the selecting of the next fringe vertex fast? #flashcard #IADS #DijkstrasAlgorithm 
	A heap is used since we can order vertices by their total path distance to our starting vertex then since we will only ever need to reduce ones value we can save time keeping track of which vertices will be added in what order.

---
What is meant by the term relaxing the graph? #flashcard #IADS #DijkstrasAlgorithm 
	This is when we add a new vertex to the set of vertices we have found the fastest path to and we add in the new connections from this vertex to our fringe reducing the cost to many vertices that were either unreachable or more expansive after the relaxing.

---
What is the time-complexity of Dijkstra's algorithm for n and m (number of vertices and number of edges)? #flashcard #IADS #DijkstrasAlgorithm 
	This would be O((n+m)lg(n))

---
