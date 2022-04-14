# Merge Sort
In this algorithm we start with a list of size $n$ we then break it in half and recursively sort each sub list. This goes on until we have singletons which are then merged together in the correct order. Eventually all the lists are merged and we get a sorted list
![[Pasted image 20220120230158.png]]
Merging the lists isn't as computationally hard since we can just move along the two lists picking the smallest from each list. This way we are guaranteed to build a list form the smallest from each list first since they are already sorted.

#### Worst case
When $n$ is a power of 2 the number of layers of subsists is $lg(n)$ then for every layer of merging we have to compare at most $n$ elements hence the overall time is $O(n\cdot lg(n))$.

#### Best and average
Since to merge two list of size $m$ it will take at least $m$ comparisons that is to check one list is smaller than all the elements in the other list. For $2^k$ size lists for each level or merger it will take $\frac{n}{2}$ comparisons at least. With $lg(n)$ levels it will therefore take $\frac{n}{2}\cdot lg(n)$ comparisons in the best case. That is $O(n\cdot lg(n))$



