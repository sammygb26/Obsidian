What is a heap? #flashcard #IADS #Heap
	A binary heap is a data structure allow for efficient calculations of a max or min element multiples times of a collection. The tree structure ensures a balanced tree with the only condition on the children being they are less than their parents. We ensure the tree is always filled meaning we always fill up the children going left to right then only start on a new level when the above is filled.

---
How can a heap be encoded into an array? #flashcard #IADS #Heap 
	A heap can be encoded into an array with the root of the heap at 0 then each layer down takes the next $2^l$ spaces where $l$ is the level. Since the heap structure is filled this can be ensured.

---
How can a parent and left and right child indices be found form one another? #flashcard #IADS #Heap 
	It depends of if the root is at 0 or 1. If its 0 then the parent will be $\lfloor i/2\rfloor$ for a child node $i$. Then for a parent node $i$ the left child will be $2i+1$ and the right child will be $2i+2$.

---
How is the heap property maintained while making small changes to a heap? #flashcard #IADS #Heap 
	When single items are removed we can perform move the last element to the roots place. We can them perform a max-happify on the root. This checks out of a parent and its children which is larger. If its the parent we do nothing, if its one of the children we switch the parents place with that child and then perform a max happify on the child.

---
What is the runtime of max-heapify and so heap extract max? #flashcard #IADS #Heap 
	It takes time proportional to the depth of the heap as the last node must be at most sorted through ever level. Hence since the depth if $O(lg\hspace{3pt}n)$ for $n$ values max-heapify will run in $O(lg\hspace{3pt}n)$ time. Extract max takes the same amount of time as we just remove the top element and replace it with the last element in the heap. This means again we most likely reduce it to the lowest values again taking $O(lg\hspace{3pt}n)$ time.

---
How does heap insert work? #flashcard #IADS #Heap 
	We swap a value into the end of the tree then we can work it up the tree checking if its parent is greater than it. If not we swap and check with the parent above that. This can at most continue until we reach the root. So it takes $O(lg\hspace{3pt}n)$ time.

---
How does build-max-heap work? #flashcard #IADS #Heap 
	The idea is we can use max heapify over and over again starting from the smallest sub heaps. This way we can combine two sub heaps and the next value when we max-heapify further up and since there is only one value that can be out of place max-heapify functions. This continues until we reach the root node. This runs overall in $O(n)$ time.

---
How does heap sort work and what is its runtime? #flashcard #IADS #Heap 
	Heap-sort works by performing build max heap. Then heap extract max $n$ times. Hence it takes $O(n\cdot lg\hspace{3pt}n)$ time.

---