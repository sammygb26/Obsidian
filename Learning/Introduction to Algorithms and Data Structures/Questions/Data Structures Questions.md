What are the two main parts of computer memory? #flashcard #IADS #ComputabilityTheory 
	The two main parts commonly used are the stack and the heap. The stack stores local variables and object references while the heap stores objects.

---
What are data structures in relation to computer memory? #flashcard #IADS #ComputabilityTheory 
	Data structures are common ways of setting up data to make it quickly and efficiently updatable and navigable to facilitate algorithms (who need to retrieve and store data) running quickly.

---
How can we compare the performance of different data structures? #flashcard #IADS #ComputabilityTheory 
	We can do this by analyzing how well they perform asymptotically for different functions applied to them. An analysis of a data structure's performance therefore relies on algorithms that interact with it being described.

---
What is a list as an abstract data structure? #flashcard #IADS #ComputabilityTheory 
	 A list is a sequence of values each of which has an index describing its place in the overall sequence.

---
What are three common data structures used to implement a list? #flashcard #IADS #ComputabilityTheory 
	A linked list is a collection of nodes each of which hold a reference to nothing or the next element in the list.
	An array is a section of memory allocated to hold for each fixed size chuck some object stored in the list. Each element of the list is physically next to the others in memory.
	A dynamic array is the same as an array accept when it gets under and over a certain amount of memory usage is changes its size copying over all its elements.

---
What is a set as an abstract data structure? #flashcard #IADS #ComputabilityTheory 
	A set is a collection of elements who's order doesn't matter only if they are in or not in the set.

---
What are the parts of a linked list node? #flashcard #IADS #ComputabilityTheory 
	A linked list can have a reference to the next node in the list and a value. We can expand this idea by adding references to the pervious elements aswell or the start and end depending on what we need the linked list to perform quickly.

---
What time does it take asymptotically to find an element in a linked list? #flashcard #IADS #ComputabilityTheory 
	For any element in the list (with $n$ elements) we will on average have pass through $\frac n2$ nodes until we reach out value. So the time is $O(n)$.

---
What is amortized cost? #flashcard #IADS #ComputabilityTheory 
	The idea is if instead of doing for each operation a normal amount of work we ensure the time taken is low or even constant. Then once every while we perform some work to ensure we can continue operating like this. The cost over all however is amortized to be lower.

---
Why is the amortized cost for appending onto a dynamic array $O(1)$? #flashcard #IADS #ComputabilityTheory 
	Most of the time we append an element in constant time as we just need to index into the array the swap in a value. However once in a while our array will be full and we will have to allocate more memory and swap the data over. This will take $O(n)$ time for an array of size $n$. But if we always scale by a fraction say by $2$ then we can perform $n$ appends in constant time for every $n$ swaps. Hence the cost per append is $O(1)$.

---
What is a stack and a queue in terms of common functionality? #flashcard #IADS #ComputabilityTheory 
	Stacks are made made to ensure two operations take constant time append and pop (remove last element added). This makes them a FIFO data structure.
	Queues are made to ensure two operations take constant time enqueue and dequeue. The first adds to the end of the queue and the last removes something from the end.

---

How can a stack and queue be made with a linked list setup? #flashcard #IADS #ComputabilityTheory 
	A stack can be implemented with a linked list this way we always keep a reference to the last element and to add a new one we just swap the pointers within the end node around.
	A queue can be implemented in much the same way where we have a linked list and keep track of the beginning and end.

---
