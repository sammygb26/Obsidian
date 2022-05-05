# Data structures
**Data Structures** are ways of storing an representing data in memory to make it easy to work with. Computer memory on a simple level consists of words that have a location in memory. We can also store the addresses in a single word.

We have memory in two parts. The stack and the heap in many languages. We keep constant length values in the stack that are named in our program. Then objects in the heap. Objects can be stored as references to their location in the heap and so we can interact with objects in the stack. We can then use these addresses to traverse this data and read the right data.
![[Pasted image 20220211131237.png]]

## Passing by Reference
We can pass by reference by instead of passing while object we just pass a pointer to that object. Then no matter where we alter the object from we will alter the same object.

## Performance
We want to compare different data structures. We do this with [[Asymptotic Analysis]] where we compare how efficient different function are on the list. For example get, set, append, delete.

### What are data structures?
When we have data, we need to decide how it is stored or represented. This will change with the kind of data and so what we might want to do with it or do to it. Again this is important to understand if you want to be a good programmer.

## Lists
A list is a common required data type that will require similar functionality over implementations. It is a collection of element in a set order that where you can add element where you like as well as remove element. And get elements from any index. Different implementations such as Fixed-[[Array]]s, [[Dynamic Array]]s and [[Linked List]]s all have different asymptotic characteristics.

## Sets
A [[Set]] is a collection of entries whose order doesn't matter. We can loop over all entries in a set and we can query if an element exists within a set.

## Dictionary
A [[Introduction to Algorithms and Data Structures/Data Patterns/Dictionary]] is a collection of elements that aren't organized by some order but instead can be referenced by another element called a key. The dictionary given a key will return an element. If we implement a dictionary as a list we will have to check over all the elements until we find a matching key this will take on average $O(n)$ time. This can be reduced in our list is sorted as we can do a binary search taking $O(ln(n))$ time.

There are many data structures that are common like [[Array]], [[Heap]], [[Linked List]], [[Tree]]
All of these are valid and all have drawbacks and strengths.

[[Data Structures Questions]]