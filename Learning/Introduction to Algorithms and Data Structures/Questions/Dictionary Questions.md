What is a dictionary? #flashcard #IADS #Dictionary
	A dictionary is a common datatype pattern. The idea is we have some data stored according to some key. The key can be any object or type we would like. The difficulty comes in making it efficient to lookup and query the dictionary.

---
What are the two main implementations of a dictionary? #flashcard  #IADS #TheMasterTheorem 
	These are the list implementation where we just have a list of key value pairs in a standard array. This takes time $O(n)$ to find any item. If we can order the keys it can take $O(lg\hspace{3pt}n)$ with binary search.
	The other is a hash table. The idea here is we convert our key into a simple value that can only be stored in a certain bin. Navigating to this bin can take time $O(1)$  so can be very efficient.

---
What is a hash function? #flashcard  #IADS #TheMasterTheorem 
	The idea behind a has function is it takes some object key that we have to an integer value within a certain range. We can then to find a keys place just hash it and use the has as a pointer within an array. Each of these locations is called a bin

---
What is a hash collision? #flashcard  #IADS #TheMasterTheorem 
	If we are hashing a large or infinite set of keys to a small range we can have two keys get the same value. So when we try to place a value in the bin is already taken and we **collide** with value already stored.

---
What is the probing approach to solving a hash collision? #flashcard  #IADS #TheMasterTheorem
	The idea is her include some second argument to our hash function that will modify the has value such that it point to some other bin. Once the value is moved our we can update where these values are stored. A problem with this is our hash table can run completely out of bind and there is nothing to do in that case.

---
What is the bucket list solution to solving hash collisions? #flashcard  #IADS #TheMasterTheorem 
	The idea here is we keep a linked list of key value pairs in any bin. When we get a new value we just put it at the back of the bin. The problem here is we can loose our speed when more and more items are stored in these lists.

---
	What is the load of a hash table? #flashcard  #IADS #TheMasterTheorem 
		The load on a hash table is defined as the number of entries with the load factor being $\frac{\text{\#entries}}{\text{\#bins}}$

---
What is perfect hashing? #flashcard  #IADS #TheMasterTheorem 
	Perfect hashing is a technique where we can precompute a hash function to work perfectly with a set of keys. This way we can always immediately lookup the location of a key when hashed and there is never any collisions. One way to do this is to use a second hash function we can pick after the first to sort the keys perfectly into place (as this can be done for small numbers of keys).

---
