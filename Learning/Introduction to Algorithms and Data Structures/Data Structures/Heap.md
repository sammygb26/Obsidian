# Heaps
A (*binary*) *heap* is a data structure that allows for the efficient calculation of a max or min element in a collection. Its characteristics allow it to easily perform a sort in $O(n\cdot ln(n))$ time. The *heap* is a binary-tree like data structure where every level of the tree is completely filled accept for the final level which is filled from the left onwards (seen in $(a)$). This means the depth of the heap is $h=\lfloor ln(n)\rfloor+1$, this will become important.

![[Pasted image 20220302170929.png]]

We store the *heap* in an *array*. We then keep track of where the heap stops in this array which is $2^h$ in size of a height $h$ such that we have $0\le A.heap-size\le A.length$. So only values of $A[i]$ where $0\le i\le A.heap-size$ are valid elements in the heap. We then arrange the elements so it is easy to calculate the children and parent given an index. This is given by 

1. $Parent(i)\hspace{5pt} return\hspace{2pt} \lfloor i/2\rfloor$
2. $Left(i)\hspace{5pt}return\hspace{2pt}2i$
3. $Reft(i)\hspace{5pt}return\hspace{2pt}2i+1$

This relationship is show in $(b)$. Hence the first element of the heap is indexed as firs tin the array. The next level is the next 2, the next the next 4 and so on. These function above can also be made very efficient via the use of bit shifting. We enforce a heap condition that a parent's children have a value strictly less than or equal to the parent (at least in a max heap the reverse is true for a min heap). 
$$
A[Parent(i)]\ge A[i]
$$
In this way the heap works to partially compute an order just enough to get a max and also ensure a new max can be easily calculated.

## Maintaining the Heap Property
Max happify is used to fix up the heap. The idea is that updating a small part of the tree is less intensive than fixing up the whole tree. The $Max-Heapify$ function takes in an index $i$. It will ensure the subheap rooted at $i$ has the *heap property* assuming that the subheaps rooted at $Left(i)$ and $Right(i)$ already comply with this property but $A[i] is some unknown value. The algorithm is given bellow (for a *max-heap*).

![[Pasted image 20220302173020.png]]

It is a recursive algorithm. The idea is that we find the greatest out of our children, then if that is smaller than us we already have a max heap so we stop. If not then we swap this greatest into our place so that locally (between the parent at $i$ and the children) the heap property is now true. This means however that we do not know if the property is true for the subtree we put the value into. Hence we apply the function again to this subtree.

The key idea is that we can at most do constant work on each level. Hence this takes time proportional to the height or $O(\lfloor lg(n)\rfloor + 1)=O(lg(n))$.

![[Pasted image 20220302173731.png]]

## Building Heap
We can apply the $Max-Heapify$ function from the bottom up in a potentially randomly ordered array to create a max heap.

![[Pasted image 20220302174207.png]]

The idea is we know the second to last layer has the required conditions for $Max-Heapify$ as the child heaps are just leaves hence they trivially comply with the heap requirement. We just move up for every element in the heap starting with the second last level (which will start at $A.lenght/2$). There are $n/2$ calls to $Max-Heapify$ each taking time $O(lg(i))$ for different values of $i$. Overall this will run in $O(n)$ time.

## Heap Insert
We can insert an element at the end of our heap that is into the position $A[A.heap-size]$. We then don't know how this particular element fits into our structure. But we can work up the heap swapping the value up if the parent is smaller.

![[Pasted image 20220302180331.png]]

Since we do this at most $h$ times each time taking $\Theta(1)$ time it will take $O(lg(n))$ time at most.

## Extract Max
We can extract the max simple by making a copy of the value stored and then swapping the last valid element into the place of the max element. This will mean we will sort this value all the way to the end of the heap in the process finding the correct choice for any conflict in which $Left$ or $Right$ is larger. Since this just does $\Theta(1)$ work with $O(lg(n))$ time used on $Max-heapify$. It will take overall $O(lg(n))$ time.

## Heapsort
To perform a heap sort all we need is heap. This gives us a partial order to the elements however we can retrieve the max in time $O(lg\hspace{3pt}n)$. We we repeat this many times getting the "next max" each time. This can be appended to a list to give a final sorted order.

![[Pasted image 20220428110340.png]]

The time taken to run $HeapSort$ can be found to be $O(n\cdot lg\hspace{3pt} n)$ just as the minimum for any sorting algorithm. This is a *in-place* sorting algorithm. And is not *stable* so doesn't keep the same relative order after sorting.